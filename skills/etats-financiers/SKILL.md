---
name: etats-financiers
description: >
  Construit le compte de résultat SYSCOHADA révisé (rubriques TA à RS, soldes XA à XI) à partir d'une balance,
  calcule les soldes significatifs de gestion et vérifie le système comptable applicable (normal ou minimal de
  trésorerie). Cette skill s'utilise quand l'utilisateur demande « compte de résultat SYSCOHADA », « états
  financiers OHADA », « marge commerciale », « valeur ajoutée », « EBE », « passer de la balance aux états
  financiers », « système minimal de trésorerie » ou prépare une clôture d'exercice.
metadata:
  version: "0.1.1"
---

# États financiers SYSCOHADA révisé

## Système applicable (AUDCIF 2017)

- Système normal : Bilan, Compte de résultat, Tableau des flux de trésorerie et Notes annexes (article 8).
- Système minimal de trésorerie (SMT), possible si le chiffre d'affaires annuel hors taxes ne dépasse pas
  60 millions de FCFA (négoce), 40 millions (entreprises artisanales et assimilées) ou 30 millions (services)
  (article 13).
- Entités cotées en bourse ou faisant appel public à l'épargne : états financiers IFRS en plus des états
  SYSCOHADA (article 8). Utiliser alors aussi la skill `passage-ifrs`.

Avant tout calcul, vérifier le système applicable à partir du chiffre d'affaires et de l'activité.

## Procédure (compte de résultat)

1. Demander la balance de l'exercice (compte, intitulé, solde débiteur, solde créditeur) et, si possible,
   celle de l'exercice précédent.
2. Contrôler la balance : total des débits = total des crédits ; signaler les comptes absents du plan
   (skill `plan-comptable`).
3. Affecter chaque compte des classes 6, 7 et 8 à sa rubrique selon `references/compte-de-resultat.md`.
   Lister les comptes non affectés ou ambigus au lieu de les forcer.
4. Calculer les rubriques puis les soldes XA à XI selon la convention du modèle en liste : produits en
   positif, charges en négatif, chaque solde étant une somme.
5. Présenter le tableau : Réf | Libellé | Exercice N | Exercice N-1.
6. Contrôle croisé : XI doit égaler le résultat de la balance (total des produits des classes 7 et 8 moins
   total des charges des classes 6 et 8). Tout écart est signalé avec les comptes en cause.
7. Commenter en trois lignes au plus : niveau de marge commerciale, valeur ajoutée, EBE, points d'attention.

## Soldes significatifs de gestion

Les soldes du compte de résultat correspondent aux comptes 132 à 138 du plan : marge commerciale (132),
valeur ajoutée (133), excédent brut d'exploitation (134), résultat d'exploitation (135), résultat financier
(136), résultat des activités ordinaires (137), résultat hors activités ordinaires (138).

## Hors périmètre (v0.1)

Bilan, tableau des flux de trésorerie, notes annexes et liasse fiscale nationale : signaler la limite. Ces
états sont prévus dans une version ultérieure.

## Garde-fous

- Ne jamais présenter les états comme définitifs : ils doivent être arrêtés par l'entité et, le cas échéant,
  certifiés par un commissaire aux comptes.
- La table de correspondance a été arbitrée lors d'une relecture par un expert-comptable (octobre 2026).
  Signaler tout sous-compte propre à l'entité et le rattacher à la rubrique de son compte parent.
