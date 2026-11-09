# Formats des fichiers CSV

Formats que la méthode de rapprochement (`methode-rapprochement.md`) sait lire. Les intitulés de colonnes
se comparent sans accents ni majuscules.

## Lecture

- Encodage : UTF-8 (avec ou sans BOM) ou Windows-1252.
- Séparateur : point-virgule, virgule, tabulation ou barre verticale, déterminé d'après la ligne d'en-tête.
- Dates : JJ/MM/AAAA, JJ/MM/AA, JJ-MM-AAAA, JJ.MM.AAAA ou AAAA-MM-JJ, avec ou sans heure (HH:MM ou
  HH:MM:SS ; « T » accepté entre la date et l'heure).
- Montants : espaces, points ou virgules comme séparateurs de milliers (« 1 180 000 », « 1.180.000 ») ;
  signe moins ou parenthèses pour les négatifs ; suffixes FCFA, XOF ou XAF ignorés. Quand points et virgules
  coexistent, le dernier des deux est le séparateur décimal. Avec un seul type de séparateur, il est décimal
  seulement s'il n'apparaît qu'une fois et n'est pas suivi d'exactement 3 chiffres (« 12,50 » vaut 12,5 ;
  « 1,180 » vaut 1 180).
- Colonne indispensable introuvable : demander à l'utilisateur l'intitulé à utiliser, sans deviner.

## Relevé mobile money

| Champ | Obligatoire | Intitulés usuels | Remarque |
| --- | --- | --- | --- |
| date | Oui | Date, Date opération, Date de l'opération, Date transaction, Date de transaction | Voir les formats de date ci-dessus |
| montant | Oui | Montant, Amount, Montant (FCFA), Montant FCFA, Montant XOF, Valeur | Positif = entrée, négatif = sortie, sauf si une colonne sens existe |
| reference | Non | Référence, Ref, ID transaction, Transaction ID, Numéro transaction, ID | Sert au rapprochement par référence |
| libelle | Non | Libellé, Description, Détails, Détail, Contrepartie, Motif, Bénéficiaire | Numéros de téléphone masqués dans tout résultat |
| frais | Non | Frais, Fees, Fee, Commission, Commissions | Frais prélevés en plus du montant de l'opération |
| sens | Non | Sens, Direction, Entrée/Sortie, Débit/Crédit, Nature | Valeurs reconnues : voir la méthode, section 1 |
| solde | Non | Solde, Balance, Solde après, Solde après opération, Nouveau solde | Permet le contrôle du solde final |

Hypothèse importante : la colonne montant n'inclut pas les frais. Si l'export de l'opérateur inclut les frais
dans le montant, ignorer la colonne frais pour éviter un double comptage, et le dire à l'utilisateur.

## Pièces (optionnel)

| Champ | Obligatoire | Intitulés usuels |
| --- | --- | --- |
| reference | Oui | Référence, Ref, Numéro, Numéro facture, Facture, Pièce |
| montant | Oui | Montant, Montant TTC, TTC, Total TTC, Amount, Net à payer |
| date | Non | Date, Date facture, Date pièce, Date de facture |
| tiers | Non | Tiers, Client, Fournisseur, Nom, Raison sociale |
| type | Non | Type, Nature, Sens (valeurs commençant par client ou fournisseur) |
