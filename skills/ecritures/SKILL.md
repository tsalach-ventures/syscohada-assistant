---
name: ecritures
description: >
  Prépare des écritures comptables SYSCOHADA équilibrées à partir d'une opération, d'une facture, d'un reçu ou
  d'un relevé. Cette skill s'utilise quand l'utilisateur demande « passer une écriture », « comptabiliser cette
  facture », « saisir une vente », « écriture de TVA », « journal des achats », « journal entry OHADA », ou
  fournit une pièce à enregistrer pour une entité de l'espace OHADA.
metadata:
  version: "0.1.1"
---

# Écritures comptables SYSCOHADA

Produire des écritures en partie double conformes au plan SYSCOHADA révisé, prêtes à être relues puis
saisies dans le logiciel comptable de l'entité.

## Informations à réunir

- Date de l'opération et date de la pièce.
- Nature de l'opération, tiers concerné, mode de règlement (comptant, crédit, banque, caisse, mobile money).
- Montants HT, TVA et TTC ; devise (XOF, XAF ou autre).
- Pays de l'entité et régime de TVA (assujettie ou non, TVA déductible ou non).

Si une information manque, poser une question courte. Si l'utilisateur veut avancer malgré tout, produire
l'écriture en écrivant l'hypothèse retenue juste au-dessus du tableau.

## Procédure

1. Qualifier l'opération : activité ordinaire ou HAO, charge ou immobilisation, comptant ou à crédit.
2. Choisir les comptes avec la skill `plan-comptable` ; ne jamais inventer un numéro.
3. Calculer HT, TVA et TTC. En XOF et XAF, arrondir au franc (pas de décimales).
4. Présenter l'écriture en tableau :

   | Date | Journal | Compte | Intitulé du compte | Libellé | Débit | Crédit |
   | --- | --- | --- | --- | --- | --- | --- |

5. Contrôler avant de répondre :
   - total des débits = total des crédits ;
   - chaque compte existe dans la référence ou est une subdivision déclarée par l'entité ;
   - la TVA n'est portée en récupérable (445x) que si elle est déductible, sinon elle s'ajoute au coût ;
   - le sens des comptes de tiers est cohérent (client au débit à la facturation, fournisseur au crédit).
6. Si l'utilisateur veut importer les écritures, fournir un bloc CSV : séparateur point-virgule, dates au format
   JJ/MM/AAAA, montants sans séparateur de milliers.
7. Terminer par deux listes courtes : « Hypothèses retenues » et « À faire valider par l'expert-comptable ».

## Journaux

Codes indicatifs, à remplacer par ceux de l'entité : AC (achats), VT (ventes), BQ (banque), CA (caisse),
MM (monnaie électronique), OD (opérations diverses).

## TVA

- Ne jamais supposer un taux. Le demander, ou rappeler que le taux dépend de l'État et de la loi de finances
  en vigueur. Repère vérifié pour la Côte d'Ivoire : taux normal de 18 % ; taux réduit de 9 % pour certains
  produits et intrants agricoles et d'élevage depuis la loi de finances 2026.
- Comptes : 4431 (TVA facturée sur ventes), 4432 (sur prestations de services), 4452 (TVA récupérable sur
  achats), 4451 (sur immobilisations), 4454 (sur services extérieurs et autres charges), 4441 (TVA due),
  4449 (crédit de TVA à reporter).
- Frais d'opérateur mobile money : 6317 par défaut (6318 si le plan interne de l'entité n'a pas éclaté le
  631) ; leur TVA n'est déductible (4454) que sur facture mensuelle conforme de l'opérateur, sinon le montant
  TTC reste en charge. Détail dans la skill `mobile-money`.

## Exemples

Voir `references/exemples.md` : achat et vente avec TVA, encaissement et paiement par mobile money,
facture mensuelle d'un opérateur avec TVA, alimentation d'un portefeuille depuis la banque via le compte 585.

## Hors périmètre (v0.1)

Paie et déclarations sociales, liasse fiscale nationale, retenues à la source spécifiques : signaler la limite
et orienter vers l'expert-comptable.

## Garde-fous

- Préparer uniquement des écritures : ne jamais initier, valider ni exécuter un paiement ou un virement.
- Ne pas inventer de pièce, de montant, de tiers ni de numéro de compte.
- Signaler les opérations sensibles (cessions d'immobilisations, dons, abandons de créances, restructurations)
  et recommander une validation avant saisie.
