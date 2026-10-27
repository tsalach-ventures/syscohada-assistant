#!/usr/bin/env python3
"""Rapprochement d'un relevé mobile money avec une liste de pièces (factures).

Lecture seule : le script lit deux fichiers CSV et écrit un rapport CSV. Il n'initie aucun paiement,
ne se connecte à aucun service et n'envoie aucune donnée.

Usage :
    python3 rapprocher.py --releve releve.csv [--pieces pieces.csv] [--sortie rapprochement.csv]

Colonnes attendues : voir ../references/format-csv.md (les intitulés usuels sont reconnus
automatiquement ; --col-<champ> permet de forcer un intitulé).
"""

import argparse
import csv
import re
import sys
import unicodedata
from datetime import datetime
from decimal import Decimal, InvalidOperation

DATE_FORMATS = [
    "%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M", "%d/%m/%Y",
    "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%d",
    "%d-%m-%Y %H:%M:%S", "%d-%m-%Y", "%d.%m.%Y", "%d/%m/%y",
]

SYNONYMES_RELEVE = {
    "date": ["date", "date operation", "date de l'operation", "date transaction", "date de transaction"],
    "reference": ["reference", "ref", "id transaction", "transaction id", "numero transaction", "id"],
    "libelle": ["libelle", "description", "details", "detail", "contrepartie", "motif", "beneficiaire"],
    "montant": ["montant", "amount", "montant (fcfa)", "montant fcfa", "montant xof", "valeur"],
    "frais": ["frais", "fees", "fee", "commission", "commissions"],
    "sens": ["sens", "direction", "entree/sortie", "debit/credit", "nature"],
    "solde": ["solde", "balance", "solde apres", "solde apres operation", "nouveau solde"],
}

SYNONYMES_PIECES = {
    "date": ["date", "date facture", "date piece", "date de facture"],
    "reference": ["reference", "ref", "numero", "numero facture", "facture", "piece"],
    "tiers": ["tiers", "client", "fournisseur", "nom", "raison sociale"],
    "montant": ["montant", "montant ttc", "ttc", "total ttc", "amount", "net a payer"],
    "type": ["type", "nature", "sens"],
}

MOTS_TRANSFERT = ["transfert vers banque", "transfert banque", "virement", "depot", "retrait",
                  "cash in", "cash out", "alimentation", "rechargement compte"]
MOTS_FRAIS = ["frais", "commission", "fees"]
# Compte 6317 (Frais sur instruments de monnaie électronique) selon la nomenclature officielle SYSCOHADA
# révisé, paramétrable en 6318 si le plan de comptes interne de l'entité n'a pas éclaté le compte 631
# (option --compte-frais).
COMPTE_FRAIS_DEFAUT = "6317"
COMMENTAIRE_FRAIS = "TTC en charge ; TVA en 4454 seulement sur facture mensuelle conforme (NCC)"
ENTREE = {"entree", "credit", "in", "recu", "reception", "encaissement", "+"}
SORTIE = {"sortie", "debit", "out", "envoi", "paiement", "retrait", "decaissement", "-"}


def normaliser(texte):
    """Minuscules, sans accents, espaces réduits."""
    texte = unicodedata.normalize("NFKD", str(texte or ""))
    texte = "".join(c for c in texte if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", texte).strip().lower()


def lire_csv(chemin):
    """Lit un CSV (UTF-8 ou Windows-1252), détecte le séparateur et renvoie (entêtes, lignes)."""
    contenu = None
    for encodage in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            with open(chemin, encoding=encodage, newline="") as f:
                contenu = f.read()
            break
        except UnicodeDecodeError:
            continue
        except OSError as err:
            sys.exit(f"Erreur : impossible de lire {chemin} ({err}).")
    if not contenu or not contenu.strip():
        sys.exit(f"Erreur : le fichier {chemin} est vide.")
    try:
        dialecte = csv.Sniffer().sniff(contenu.splitlines()[0], delimiters=";,\t|")
        separateur = dialecte.delimiter
    except csv.Error:
        separateur = ";"
    lecteur = csv.DictReader(contenu.splitlines(), delimiter=separateur)
    lignes = [ligne for ligne in lecteur if any((v or "").strip() for v in ligne.values())]
    return lecteur.fieldnames or [], lignes


def trouver_colonnes(entetes, synonymes, forcees):
    """Associe chaque champ logique à un intitulé de colonne du fichier."""
    index = {normaliser(e): e for e in entetes}
    colonnes = {}
    for champ, candidats in synonymes.items():
        if forcees.get(champ):
            if forcees[champ] not in entetes:
                sys.exit(f"Erreur : colonne « {forcees[champ]} » introuvable. Colonnes lues : {entetes}")
            colonnes[champ] = forcees[champ]
            continue
        for candidat in candidats:
            if candidat in index:
                colonnes[champ] = index[candidat]
                break
    return colonnes


def lire_date(valeur):
    valeur = (valeur or "").strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(valeur, fmt)
        except ValueError:
            continue
    return None


def lire_montant(valeur):
    """Convertit « 1 180 000 », « 1.180.000 », « -5 900 FCFA », « (2 500) » ou « 12,50 » en Decimal."""
    texte = str(valeur or "").strip()
    if not texte:
        return Decimal("0")
    negatif = texte.startswith("-") or (texte.startswith("(") and texte.endswith(")"))
    texte = re.sub(r"[^\d.,]", "", texte)
    if not texte:
        return None
    if "." in texte and "," in texte:
        decimal_sep = "." if texte.rfind(".") > texte.rfind(",") else ","
        milliers = "," if decimal_sep == "." else "."
        texte = texte.replace(milliers, "").replace(decimal_sep, ".")
    elif "," in texte or "." in texte:
        sep = "," if "," in texte else "."
        morceaux = texte.split(sep)
        if len(morceaux) > 2 or len(morceaux[-1]) == 3:
            texte = texte.replace(sep, "")
        else:
            texte = texte.replace(sep, ".")
    try:
        montant = Decimal(texte)
    except InvalidOperation:
        return None
    return -montant if negatif else montant


def masquer_numeros(texte):
    """Masque les suites de 8 chiffres ou plus (numéros de téléphone) en gardant les 2 derniers."""
    def remplacer(m):
        chiffres = re.sub(r"\D", "", m.group(0))
        return "X" * (len(chiffres) - 2) + chiffres[-2:]
    return re.sub(r"\+?\d(?:[ .]?\d){7,}", remplacer, texte or "")


def contient(texte, mots):
    texte = normaliser(texte)
    return any(mot in texte for mot in mots)


def charger_releve(chemin, forcees, masquer):
    entetes, lignes = lire_csv(chemin)
    cols = trouver_colonnes(entetes, SYNONYMES_RELEVE, forcees)
    manquantes = [c for c in ("date", "montant") if c not in cols]
    if manquantes:
        sys.exit(f"Erreur : colonnes {manquantes} introuvables dans le relevé. Colonnes lues : {entetes}. "
                 "Utiliser --col-date / --col-montant.")
    mouvements, erreurs = [], []
    for numero, ligne in enumerate(lignes, start=2):
        date = lire_date(ligne.get(cols["date"]))
        montant = lire_montant(ligne.get(cols["montant"]))
        if date is None or montant is None:
            erreurs.append(f"ligne {numero} : date ou montant illisible")
            continue
        if "sens" in cols:
            sens = normaliser(ligne.get(cols["sens"]))
            if sens in SORTIE:
                montant = -abs(montant)
            elif sens in ENTREE:
                montant = abs(montant)
        frais = lire_montant(ligne.get(cols["frais"])) if "frais" in cols else Decimal("0")
        libelle = (ligne.get(cols["libelle"]) or "").strip() if "libelle" in cols else ""
        mouvements.append({
            "ligne": numero,
            "date": date,
            "reference": (ligne.get(cols["reference"]) or "").strip() if "reference" in cols else "",
            "libelle": masquer_numeros(libelle) if masquer else libelle,
            "libelle_brut": libelle,
            "montant": montant,
            "frais": abs(frais or Decimal("0")),
            "solde": lire_montant(ligne.get(cols["solde"])) if "solde" in cols else None,
        })
    return mouvements, erreurs


def charger_pieces(chemin, forcees):
    entetes, lignes = lire_csv(chemin)
    cols = trouver_colonnes(entetes, SYNONYMES_PIECES, forcees)
    manquantes = [c for c in ("montant", "reference") if c not in cols]
    if manquantes:
        sys.exit(f"Erreur : colonnes {manquantes} introuvables dans les pièces. Colonnes lues : {entetes}.")
    pieces, erreurs = [], []
    for numero, ligne in enumerate(lignes, start=2):
        montant = lire_montant(ligne.get(cols["montant"]))
        if montant is None:
            erreurs.append(f"pièce ligne {numero} : montant illisible")
            continue
        type_piece = normaliser(ligne.get(cols["type"])) if "type" in cols else ""
        pieces.append({
            "ligne": numero,
            "date": lire_date(ligne.get(cols["date"])) if "date" in cols else None,
            "reference": (ligne.get(cols["reference"]) or "").strip(),
            "tiers": (ligne.get(cols["tiers"]) or "").strip() if "tiers" in cols else "",
            "montant": abs(montant),
            "type": "client" if type_piece.startswith("client") else
                    "fournisseur" if type_piece.startswith("fournisseur") else "",
            "utilisee": False,
        })
    return pieces, erreurs


def candidates(mouvement, pieces, fenetre, tolerance):
    entree = mouvement["montant"] > 0
    type_attendu = "client" if entree else "fournisseur"
    trouvees = []
    for piece in pieces:
        if piece["utilisee"] or piece["montant"] != abs(mouvement["montant"]):
            continue
        if piece["type"] and piece["type"] != type_attendu:
            continue
        ecart = None
        if piece["date"] is not None:
            ecart = (mouvement["date"].date() - piece["date"].date()).days
            if ecart < -tolerance or ecart > fenetre:
                continue
        ref = normaliser(piece["reference"])
        ref_trouvee = bool(ref) and ref in normaliser(mouvement["reference"] + " " + mouvement["libelle_brut"])
        trouvees.append((0 if ref_trouvee else 1, abs(ecart) if ecart is not None else 9999, piece, ecart))
    trouvees.sort(key=lambda t: (t[0], t[1]))
    return trouvees


def rapprocher(mouvements, pieces, fenetre, tolerance, compte_frais=COMPTE_FRAIS_DEFAUT):
    resultats = []
    for mvt in sorted(mouvements, key=lambda m: (m["date"], m["ligne"])):
        base = {
            "date": mvt["date"].strftime("%d/%m/%Y"),
            "reference": mvt["reference"],
            "libelle": mvt["libelle"],
            "montant": mvt["montant"],
            "piece_reference": "",
            "piece_tiers": "",
            "ecart_jours": "",
        }
        trouvees = candidates(mvt, pieces, fenetre, tolerance) if mvt["montant"] != 0 else []
        if trouvees:
            _, _, piece, ecart = trouvees[0]
            piece["utilisee"] = True
            entree = mvt["montant"] > 0
            resultats.append({**base, "statut": "rapproche",
                              "piece_reference": piece["reference"], "piece_tiers": piece["tiers"],
                              "ecart_jours": "" if ecart is None else ecart,
                              "compte_contrepartie": "411" if entree else "401",
                              "commentaire": "référence retrouvée" if trouvees[0][0] == 0 else "montant et date"})
        elif contient(mvt["libelle_brut"], MOTS_FRAIS) and mvt["montant"] < 0:
            resultats.append({**base, "statut": "frais", "compte_contrepartie": compte_frais,
                              "commentaire": COMMENTAIRE_FRAIS})
        elif contient(mvt["libelle_brut"], MOTS_TRANSFERT):
            resultats.append({**base, "statut": "transfert_interne_probable", "compte_contrepartie": "585",
                              "commentaire": "à confirmer : mouvement entre trésoreries de l'entité"})
        else:
            resultats.append({**base, "statut": "non_rapproche", "compte_contrepartie": "",
                              "commentaire": "aucune pièce de même montant dans la fenêtre"})
        if mvt["frais"]:
            resultats.append({**base, "montant": -mvt["frais"], "statut": "frais",
                              "compte_contrepartie": compte_frais,
                              "commentaire": "frais prélevés sur l'opération ; " + COMMENTAIRE_FRAIS})
    return resultats


def ecrire_sortie(chemin, resultats):
    champs = ["date", "reference", "libelle", "montant", "statut", "piece_reference", "piece_tiers",
              "ecart_jours", "compte_contrepartie", "commentaire"]
    with open(chemin, "w", encoding="utf-8-sig", newline="") as f:
        ecrivain = csv.DictWriter(f, fieldnames=champs, delimiter=";")
        ecrivain.writeheader()
        for r in resultats:
            ecrivain.writerow({**r, "montant": format(r["montant"], "f")})


def fmt(montant):
    signe = "-" if montant < 0 else ""
    entier = f"{abs(montant):,.0f}".replace(",", " ")
    return f"{signe}{entier}"


def main():
    parser = argparse.ArgumentParser(description="Rapprochement relevé mobile money / pièces (lecture seule).")
    parser.add_argument("--releve", required=True, help="Export CSV du relevé mobile money")
    parser.add_argument("--pieces", help="CSV des factures clients et fournisseurs (optionnel)")
    parser.add_argument("--sortie", default="rapprochement.csv", help="Fichier CSV de résultat")
    parser.add_argument("--fenetre-jours", type=int, default=60,
                        help="Écart maximal entre la pièce et le paiement, en jours (défaut 60)")
    parser.add_argument("--tolerance-jours", type=int, default=3,
                        help="Avance maximale d'un paiement sur la pièce, en jours (défaut 3)")
    parser.add_argument("--compte-frais", default=COMPTE_FRAIS_DEFAUT,
                        help="Compte des frais d'opérateur (défaut 6317 ; 6318 si le 631 n'est pas éclaté)")
    parser.add_argument("--sans-masquage", action="store_true",
                        help="Ne pas masquer les numéros de téléphone dans les libellés")
    for champ in sorted(set(SYNONYMES_RELEVE) | set(SYNONYMES_PIECES)):
        parser.add_argument(f"--col-{champ}", dest=f"col_{champ}", help=f"Intitulé exact de la colonne {champ}")
    args = parser.parse_args()

    forcees = {c: getattr(args, f"col_{c}") for c in set(SYNONYMES_RELEVE) | set(SYNONYMES_PIECES)}
    mouvements, erreurs = charger_releve(args.releve, forcees, not args.sans_masquage)
    pieces, erreurs_pieces = charger_pieces(args.pieces, forcees) if args.pieces else ([], [])
    resultats = rapprocher(mouvements, pieces, args.fenetre_jours, args.tolerance_jours, args.compte_frais)
    ecrire_sortie(args.sortie, resultats)

    par_statut = {}
    for r in resultats:
        compte = par_statut.setdefault(r["statut"], [0, Decimal("0"), Decimal("0")])
        compte[0] += 1
        if r["montant"] > 0:
            compte[1] += r["montant"]
        else:
            compte[2] += r["montant"]
    print(f"Relevé : {len(mouvements)} opérations lues ; pièces : {len(pieces)}.")
    for statut in ("rapproche", "frais", "transfert_interne_probable", "non_rapproche"):
        if statut in par_statut:
            nb, entrees, sorties = par_statut[statut]
            print(f"  {statut:<28} {nb:>3} ligne(s)  entrées {fmt(entrees):>12}  sorties {fmt(sorties):>12}")
    restantes = [p for p in pieces if not p["utilisee"]]
    if restantes:
        print(f"Pièces sans paiement retrouvé : {len(restantes)} (ex. {', '.join(p['reference'] for p in restantes[:5])}).")
    mouvements_nets = sum((m["montant"] - m["frais"] for m in mouvements), Decimal("0"))
    soldes = [m for m in sorted(mouvements, key=lambda m: (m["date"], m["ligne"])) if m["solde"] is not None]
    print(f"Variation nette du portefeuille (mouvements - frais) : {fmt(mouvements_nets)}")
    if soldes:
        final = soldes[-1]["solde"]
        print(f"Solde final du relevé : {fmt(final)} ; solde d'ouverture implicite : {fmt(final - mouvements_nets)}")
        print("Comparer le solde final au solde du compte 552 (ou de son sous-compte) après écritures.")
    for message in erreurs + erreurs_pieces:
        print(f"Avertissement : {message}")
    print(f"Détail écrit dans {args.sortie}")


if __name__ == "__main__":
    main()
