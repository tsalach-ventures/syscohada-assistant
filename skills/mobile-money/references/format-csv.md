# Formats CSV pris en charge par `scripts/rapprocher.py`

Le script lit des fichiers CSV encodés en UTF-8 ou Windows-1252, avec séparateur point-virgule, virgule,
tabulation ou barre verticale (détection automatique). Les intitulés de colonnes sont reconnus sans tenir
compte des accents ni des majuscules.

## Relevé mobile money (`--releve`)

| Champ | Obligatoire | Intitulés reconnus | Remarque |
| --- | --- | --- | --- |
| date | Oui | Date, Date opération, Date transaction | JJ/MM/AAAA, AAAA-MM-JJ, avec ou sans heure |
| montant | Oui | Montant, Amount, Montant (FCFA), Valeur | Positif = entrée, négatif = sortie, sauf si une colonne sens existe |
| reference | Non | Référence, Ref, ID transaction | Sert au rapprochement par référence |
| libelle | Non | Libellé, Description, Détails, Motif, Bénéficiaire | Les numéros de téléphone sont masqués dans la sortie |
| frais | Non | Frais, Fees, Commission | Montant des frais prélevés en plus du montant de l'opération |
| sens | Non | Sens, Direction, Entrée/Sortie, Débit/Crédit | Valeurs reconnues : entrée, crédit, reçu / sortie, débit, paiement, retrait |
| solde | Non | Solde, Balance, Solde après opération | Permet le contrôle du solde final |

Hypothèse importante : la colonne montant n'inclut pas les frais. Si l'export de l'opérateur inclut les frais
dans le montant, ne pas renseigner de colonne frais (ou la neutraliser) pour éviter un double comptage.

Les montants acceptent les espaces, points ou virgules comme séparateurs de milliers (« 1 180 000 »,
« 1.180.000 »), les parenthèses pour les négatifs et les suffixes FCFA, XOF ou XAF.

## Pièces (`--pieces`, optionnel)

| Champ | Obligatoire | Intitulés reconnus |
| --- | --- | --- |
| reference | Oui | Référence, Numéro facture, Facture, Pièce |
| montant | Oui | Montant TTC, TTC, Total TTC, Net à payer, Montant |
| date | Non | Date, Date facture, Date pièce |
| tiers | Non | Tiers, Client, Fournisseur, Nom, Raison sociale |
| type | Non | Type, Nature (valeurs : client, fournisseur) |

## Règles de rapprochement

1. Un mouvement est rapproché d'une pièce de même montant exact (en valeur absolue) et de type cohérent :
   entrée ↔ client, sortie ↔ fournisseur.
2. La date du paiement doit être comprise entre 3 jours avant la pièce (`--tolerance-jours`) et 60 jours
   après (`--fenetre-jours`).
3. Priorité aux pièces dont la référence apparaît dans la référence ou le libellé du mouvement, puis à l'écart
   de dates le plus faible. Chaque pièce n'est utilisée qu'une fois.
4. Sans pièce : les libellés contenant « frais » ou « commission » sont classés en frais (compte 6317,
   montant TTC tant qu'aucune facture conforme de l'opérateur ne permet de déduire la TVA en 4454) ; ceux
   qui évoquent un dépôt, un retrait ou un virement sont classés en transfert interne probable (compte 585) ;
   le reste est « non rapproché » et appelle une question à l'utilisateur.

Note : Compte 6317 (Frais sur instruments de monnaie électronique) selon la nomenclature officielle SYSCOHADA révisé, paramétrable en 6318 si le plan de comptes interne de l'entité n'a pas éclaté le compte 631. Option du script : `--compte-frais 6318`.

## Sortie

Fichier CSV (séparateur point-virgule) : date, référence, libellé masqué, montant, statut, pièce retenue,
tiers, écart en jours, compte de contrepartie proposé, commentaire. Le résumé affiché indique les totaux par
statut, les pièces sans paiement et, si la colonne solde existe, le solde final et le solde d'ouverture
implicite à comparer au compte 552.
