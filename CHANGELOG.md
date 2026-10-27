# Journal des versions

## 0.1.3 — 27/10/2026

L'icône de la fiche est désormais déclarée dans le manifeste (champ icon de plugin.json), en plus de son
emplacement par défaut. Aucun autre changement.

## 0.1.2 — 27/10/2026

Préparation de la fiche dans l'annuaire des plugins Claude. Le contenu comptable des skills ne change pas :
c'est celui de la version 0.1.1, relue par un expert-comptable.

- Icône du plugin (compte en T, aux couleurs de Tsalach Ventures) pour la fiche de l'annuaire.
- Liens de la fiche dans `plugin.json` : documentation, support (issues GitHub), politique de confidentialité
  et conditions d'utilisation (licence MIT).
- Nouveaux fichiers `PRIVACY.md` (confidentialité) et `SECURITY.md` (signalement d'une vulnérabilité), en
  français et en anglais.
- README : ce que le script de rapprochement exécute (bibliothèque standard Python, aucun accès réseau) ;
  résumé anglais mis à jour.

## 0.1.1 — 07/10/2026

Arbitrages issus de la relecture par un expert-comptable.

- Compte de résultat : TK = 77 sauf 779 ; TL = 797 et 779 ; RM = 67 sauf 679 ; RN = 697, 679 et 687.
  Mentions « à confirmer » supprimées et règles de chaque rubrique documentées.
- Frais des opérateurs de monnaie électronique : 6317 « Frais sur instruments monnaie électronique » (classe 631,
  pas 628). TVA déductible en 4454 uniquement sur facture mensuelle conforme mentionnant le NCC ; sinon montant
  TTC en charge. Nouvel exemple d'écriture (4 bis) et script de rapprochement mis à jour.
  Paramétrable en 6318 si le plan interne de l'entité n'a pas éclaté le 631 (option `--compte-frais`).
- Compte 552 jamais créditeur à la clôture ; compte 585 soldé à chaque arrêté.
- Plan comptable : ajout des sous-comptes 6317 et 6318.

## 0.1.0 — 24/09/2026

Structure initiale du plugin.

- Skills : `plan-comptable`, `ecritures`, `mobile-money`, `etats-financiers`, `passage-ifrs`.
- Script `rapprocher.py` (rapprochement relevé mobile money / pièces), testé sur données fictives.
- Relecture par un expert-comptable : à faire avant la soumission à l'annuaire des plugins.

## Prévu

- 0.2 : bilan et tableau des flux de trésorerie ; correspondance des postes SYSCOHADA vers les lignes IFRS.
- 0.3 : références fiscales par État (TVA, impôt minimum), maintenues avec leurs sources et dates.
