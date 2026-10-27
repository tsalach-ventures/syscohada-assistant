---
name: plan-comptable
description: >
  Référentiel du plan comptable SYSCOHADA révisé (OHADA). Cette skill s'utilise quand l'utilisateur demande
  « quel compte utiliser », « numéro de compte SYSCOHADA », « plan comptable OHADA », « imputation comptable »,
  « classe 6 / classe 4 », ou veut vérifier qu'un compte existe ou qu'une imputation est correcte dans un pays
  de l'espace OHADA (Côte d'Ivoire, Sénégal, Cameroun, Gabon, RDC…). Also triggers on "OHADA chart of accounts".
metadata:
  version: "0.1.1"
---

# Plan comptable SYSCOHADA révisé

Choisir et vérifier les comptes du Système comptable OHADA révisé (SYSCOHADA). Base juridique : Acte uniforme
relatif au droit comptable et à l'information financière (AUDCIF), adopté le 26 janvier 2017 à Brazzaville,
applicable aux comptes personnels depuis le 1er janvier 2018 et aux comptes consolidés et combinés depuis le
1er janvier 2019.

## Méthode

1. Identifier la nature de l'opération : achat, vente, charge de personnel, trésorerie, immobilisation,
   opération hors activités ordinaires (HAO), opération avec l'État.
2. Choisir la classe, puis le compte à 2, 3 ou 4 chiffres dans `references/classes-et-comptes.md`.
3. Donner le numéro, l'intitulé exact et une justification d'une ligne.
4. En cas d'ambiguïté (deux comptes plausibles), présenter les deux options, le critère qui les départage et
   la question à poser à l'utilisateur.
5. Ne jamais inventer un numéro de compte. Si le compte cherché ne figure pas dans la référence, le dire et
   proposer le compte parent (2 ou 3 chiffres) le plus proche.
6. Si l'entité utilise ses propres subdivisions (ex. 5521 pour un portefeuille donné), les respecter.

## Repères structurants

- Classes 1 à 5 : comptes de bilan. Classes 6 à 8 : comptes de gestion. Classe 9 : engagements hors bilan et
  comptabilité analytique de gestion.
- Activités ordinaires (classes 6 et 7) et hors activités ordinaires (classe 8) : les cessions
  d'immobilisations, restructurations, liquidations, dons et abandons de créances relèvent en principe de la
  classe 8. Qualifier l'opération avant de choisir la classe.
- Exclusions à connaître : le compte 60 exclut 603 (variations des stocks de biens achetés), le compte 65
  exclut 659, le compte 75 exclut 759. Ces comptes alimentent d'autres rubriques du compte de résultat
  (voir la skill `etats-financiers`).
- Monnaie électronique (mobile money) : compte 55, notamment 552 « Monnaie électronique – téléphone portable » ;
  frais des opérateurs en 6317 « Frais sur instruments monnaie électronique ». Voir la skill `mobile-money`.
- TVA : 443 (TVA facturée), 445 (TVA récupérable), 4441 (TVA due), 4449 (crédit de TVA à reporter).
- Écarts de conversion sur créances et dettes en devises : 478 (actif) et 479 (passif).

## Portée

Le plan comptable est commun aux 17 États membres de l'OHADA. La fiscalité (taux de TVA, impôts, liasse
fiscale) relève de chaque État : ne jamais la déduire du plan comptable.

## Limites

Présenter les réponses comme indicatives. Recommander la validation par un expert-comptable inscrit à l'ordre
du pays concerné pour toute opération inhabituelle, significative ou soumise à un traitement fiscal particulier.
