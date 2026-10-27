---
name: mobile-money
description: >
  Rapproche les relevés mobile money (Orange Money, MTN MoMo, Moov Money, Wave…) avec la comptabilité SYSCOHADA
  (compte 55, instruments de monnaie électronique) et propose les écritures correspondantes. Cette skill
  s'utilise quand l'utilisateur demande « rapprochement mobile money », « comptabiliser mes transactions
  Orange Money / Wave », « relevé MoMo », « compte 552 », ou fournit l'export CSV d'un portefeuille
  électronique d'entreprise dans l'espace OHADA.
metadata:
  version: "0.1.1"
---

# Rapprochement mobile money (SYSCOHADA)

Rapprocher un relevé de portefeuille mobile money avec les pièces de l'entité, classer chaque opération et
préparer les écritures. Travail en lecture seule.

## Règles comptables

- Compte 55 « Instruments de monnaie électronique » ; utiliser 552 « Monnaie électronique – téléphone
  portable » pour les portefeuilles mobile money. Le compte est débité des chargements et crédité des
  règlements ; son solde est débiteur ou nul, jamais créditeur à la clôture.
- Ouvrir un sous-compte par portefeuille si l'entité en a plusieurs (ex. 5521 pour un opérateur, 5522 pour un
  autre) : subdivisions propres à l'entité, à valider avec son expert-comptable.
- Transferts entre banque (521), caisse (571) et portefeuille (552) : passer impérativement par le compte
  585 « Virements de fonds », qui doit être soldé (solde nul) à chaque arrêté.
- Frais et commissions d'opérateur : 6317 « Frais sur instruments monnaie électronique », sous le 631
  « Frais bancaires ». Les opérateurs sont des prestataires de services de paiement agréés par la BCEAO :
  ne pas utiliser le 628 (télécommunications).
  Note : Compte 6317 (Frais sur instruments de monnaie électronique) selon la nomenclature officielle SYSCOHADA révisé, paramétrable en 6318 si le plan de comptes interne de l'entité n'a pas éclaté le compte 631.
- TVA sur ces frais : déductible en 4454 uniquement sur facture mensuelle officielle de l'opérateur
  mentionnant son NCC ; sur simple relevé ou reçu, passer le montant TTC en charge en 6317.

## Procédure

1. Obtenir l'export du relevé (CSV) et, si possible, la liste des factures clients et fournisseurs de la
   période (CSV).
2. Exécuter le script de rapprochement depuis le dossier de cette skill :

   ```bash
   python3 scripts/rapprocher.py --releve <releve.csv> --pieces <pieces.csv> --sortie rapprochement.csv
   ```

   Colonnes, formats et options : `references/format-csv.md`. Si une colonne n'est pas reconnue, relancer
   avec `--col-date`, `--col-montant`, etc. Si l'entité n'a pas éclaté le compte 631, ajouter
   `--compte-frais 6318`. Sans fichier de pièces, omettre `--pieces` : le script classe
   alors seulement les frais, les transferts probables et le reste.
3. Lire le résumé et le fichier de sortie. Présenter un tableau par statut : rapproché, frais, transfert
   interne probable, non rapproché.
4. Préparer les écritures des lignes rapprochées, des frais et des transferts avec la skill `ecritures`
   (journal MM). Pour chaque ligne non rapprochée, poser une question précise (qui, pourquoi, quelle pièce).
5. Contrôler le solde : le solde final du relevé doit égaler le solde du compte 552 (ou du sous-compte) après
   écritures. Expliquer tout écart ou le signaler comme point ouvert.
6. Lister les pièces restées sans paiement : ce sont des relances possibles.

## Garde-fous

- Ne jamais initier, valider ni exécuter un paiement, un transfert ou un retrait : préparer uniquement.
- Les relevés contiennent des données personnelles (numéros de téléphone, noms). Ne pas les recopier sans
  nécessité ; le script masque les numéros dans les libellés.
- Ne pas déduire l'identité d'un payeur à partir d'un numéro de téléphone.
- Ne pas considérer un rapprochement « montant et date » comme certain : le présenter comme proposition.

## Exemple

`examples/releve-exemple.csv` et `examples/pieces-exemple.csv` (données fictives) : 7 opérations, 3
rapprochées, 3 lignes de frais, 2 transferts internes probables, 1 opération non rapprochée, 1 facture sans
paiement.
