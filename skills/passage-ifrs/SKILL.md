---
name: passage-ifrs
description: >
  Prépare le passage des comptes SYSCOHADA vers les IFRS pour une filiale de groupe ou une entité cotée de
  l'espace OHADA : checklist des retraitements, note de retraitement et écritures de retraitement hors livres
  légaux. Cette skill s'utilise quand l'utilisateur demande « passage SYSCOHADA IFRS », « retraitements IFRS »,
  « liasse de consolidation d'une filiale africaine », « IFRS 16 / IAS 12 sur des comptes OHADA »,
  « SYSCOHADA to IFRS bridge » ou prépare un reporting groupe.
metadata:
  version: "0.1.1"
---

# Passage SYSCOHADA → IFRS

## Cadre

- AUDCIF 2017, article 8 : les entités dont les titres sont cotés en bourse ou qui font appel public à
  l'épargne établissent des états financiers IFRS en plus de leurs états SYSCOHADA. Dispositions applicables
  aux comptes consolidés et combinés et au référentiel IFRS depuis le 1er janvier 2019.
- Filiale d'un groupe étranger : les états SYSCOHADA restent les états légaux ; les retraitements IFRS
  servent la consolidation du groupe (liasse ou package de reporting).
- Présentation : IAS 1 jusqu'aux exercices ouverts avant le 1er janvier 2027 ; IFRS 18 la remplace pour les
  exercices ouverts à compter de cette date (application anticipée permise). Demander quel référentiel de
  présentation le groupe applique.

## Procédure

1. Cadrer : entité, exercice, date de clôture du groupe, seuil de matérialité, manuel de reporting du groupe,
   plan de comptes groupe.
2. Parcourir `references/retraitements.md` thème par thème. Pour chaque thème, demander les données listées,
   puis conclure : « sans objet », « retraitement à passer » ou « à investiguer ».
3. Rédiger la note de retraitement : Poste SYSCOHADA | Montant SYSCOHADA | Retraitement | Norme IFRS |
   Montant IFRS | Commentaire.
4. Préparer les écritures de retraitement dans un journal distinct, jamais dans les livres légaux SYSCOHADA.
5. Si un taux d'impôt est nécessaire (impôts différés), le demander : il dépend de l'État.
6. Terminer par la liste des jugements à faire valider par la direction financière du groupe et les
   commissaires aux comptes.

## Garde-fous

- Ne jamais présenter un retraitement comme définitif : durées de location, pertes de crédit attendues,
  hypothèses actuarielles et impôts différés relèvent de jugements de la direction et des auditeurs.
- Citer la norme (et le paragraphe quand il est connu). En cas de doute sur le traitement SYSCOHADA d'origine,
  le dire et demander la politique comptable de l'entité.
- Ne pas extrapoler une règle d'un État OHADA à un autre pour la fiscalité.
