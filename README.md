# Assistant SYSCOHADA (OHADA) — plugin Claude

Plugin pour Claude (Cowork et Claude Code) qui aide les comptables, dirigeants de PME et directions
financières de l'espace OHADA à appliquer le SYSCOHADA révisé, en français.

> Version 0.1.3 — contenu comptable relu par un expert-comptable (octobre 2026) ; ses arbitrages sont
> intégrés (rubriques financières du compte de résultat, frais et TVA des opérateurs mobile money,
> comptes 552 et 585).

## Ce que fait le plugin

| Skill | Rôle | Exemple de demande |
| --- | --- | --- |
| `plan-comptable` | Choisir et vérifier un compte du plan SYSCOHADA révisé | « Quel compte pour les frais de télécommunication ? » |
| `ecritures` | Préparer des écritures équilibrées, TVA comprise, avec export CSV | « Comptabilise cette facture fournisseur de 1 180 000 TTC » |
| `mobile-money` | Rapprocher un relevé Orange Money, MTN MoMo, Moov Money ou Wave avec les factures | « Rapproche mon relevé de septembre avec mes factures » |
| `etats-financiers` | Construire le compte de résultat (XA à XI) depuis une balance | « Calcule la valeur ajoutée et l'EBE à partir de cette balance » |
| `passage-ifrs` | Lister et documenter les retraitements IFRS d'une filiale ou d'une entité cotée | « Prépare les retraitements IFRS de notre filiale d'Abidjan » |

Le plan comptable est commun aux 17 États membres de l'OHADA. Les règles fiscales (taux de TVA, impôts)
restent propres à chaque État : le plugin demande le taux applicable au lieu de le supposer.

## Installation

- **Depuis ce dépôt (Claude Code)** :

  ```shell
  /plugin marketplace add tsalach-ventures/syscohada-assistant
  /plugin install syscohada-assistant@tsalach-ventures
  ```

- **Cowork** : importer le fichier `.plugin` joint à la dernière version publiée (onglet *Releases* du
  dépôt).
- **Annuaire des plugins Claude** : lien ajouté ici après publication.

## Exemple : rapprochement mobile money

```bash
cd skills/mobile-money
python3 scripts/rapprocher.py --releve examples/releve-exemple.csv --pieces examples/pieces-exemple.csv
```

Résultat sur les données fictives fournies : 3 opérations rapprochées, 3 lignes de frais, 2 transferts
internes probables, 1 opération non rapprochée, 1 facture sans paiement, et le contrôle du solde final.
Formats acceptés : `skills/mobile-money/references/format-csv.md`.

## Limites

- Aide à la préparation : ce plugin ne remplace ni l'avis d'un expert-comptable inscrit à l'ordre du pays,
  ni un conseil fiscal. Les écritures et états produits doivent être relus avant usage.
- Le plugin n'initie, ne valide et n'exécute aucun paiement.
- Hors périmètre en 0.1 : paie, liasse fiscale nationale, bilan et tableau des flux de trésorerie.
- Plugin indépendant, non affilié à l'OHADA et non approuvé par elle. « SYSCOHADA » désigne le référentiel
  comptable public de l'OHADA.

## Confidentialité

- Le plugin ne collecte, ne stocke et ne transmet aucune donnée : il contient des instructions pour Claude
  et un script qui s'exécute localement sur les fichiers fournis par l'utilisateur.
- Ce que le script exécute : `rapprocher.py` n'utilise que la bibliothèque standard de Python et n'accède
  pas au réseau. Il lit le relevé CSV (et, en option, la liste des pièces), affiche un résumé et écrit un
  fichier CSV de résultat (par défaut `rapprochement.csv` dans le dossier courant).
- Le script de rapprochement masque les numéros de téléphone dans son fichier de sortie.
- Détails : [PRIVACY.md](PRIVACY.md). Signaler une vulnérabilité : [SECURITY.md](SECURITY.md).
- Contact : steph@tsalach.ventures

## Sources

Voir [SOURCES.md](SOURCES.md).

## Contribuer

Les corrections d'experts-comptables et d'auditeurs de l'espace OHADA sont bienvenues : ouvrir une issue en
citant la source (acte uniforme, guide d'application, texte fiscal) et la date.

## Licence et éditeur

Licence MIT. Édité par Tsalach Ventures LLC.

---

## English summary

French-language Claude plugin for the 17 OHADA member states (SYSCOHADA révisé accounting framework):
chart of accounts lookup, balanced journal entries, mobile money statement reconciliation (read-only
script), income statement from a trial balance, and a SYSCOHADA-to-IFRS restatement checklist. It
collects no data and never executes payments. Its only executable part is a local Python script (standard
library only, no network access) that reads a CSV statement, optionally a CSV list of invoices, and writes
one CSV result file. Version 0.1.3: the accounting content was reviewed by a chartered accountant in
October 2026. Independent project, not affiliated with or endorsed by OHADA. Privacy: [PRIVACY.md](PRIVACY.md).
Security: [SECURITY.md](SECURITY.md).
