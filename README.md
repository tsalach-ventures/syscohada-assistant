# Assistant SYSCOHADA (OHADA) — plugin Claude

Plugin pour Claude (Cowork et Claude Code) qui aide les comptables, dirigeants de PME et directions
financières de l'espace OHADA à appliquer le SYSCOHADA révisé, en français.

> Version 0.1.6 — contenu comptable relu par un expert-comptable (octobre 2026) ; ses arbitrages sont
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

- **Cowork** : importer l'archive du plugin (fichier `.plugin` ou `.zip`) jointe à la dernière version
  publiée (onglet *Releases* du dépôt).
- **Annuaire des plugins Claude** : lien ajouté ici après publication.

## Exemple : rapprochement mobile money

Demander à Claude : « Rapproche le relevé et les pièces d'exemple du plugin ». Ces deux jeux de données
fictifs, au format CSV, figurent dans `skills/mobile-money/examples/exemples-rapprochement.md`. Claude
applique la méthode de la skill avec ses propres outils et obtient : 3 opérations rapprochées, 3 lignes de
frais, 2 transferts internes probables, 1 opération non rapprochée, 1 facture sans paiement, et le contrôle
du solde final.

Méthode : `skills/mobile-money/references/methode-rapprochement.md`. Formats acceptés :
`skills/mobile-money/references/format-csv.md`.

## Limites

- Aide à la préparation : ce plugin ne remplace ni l'avis d'un expert-comptable inscrit à l'ordre du pays,
  ni un conseil fiscal. Les écritures et états produits doivent être relus avant usage.
- Le plugin n'initie, ne valide et n'exécute aucun paiement.
- Hors périmètre en 0.1 : paie, liasse fiscale nationale, bilan et tableau des flux de trésorerie.
- Plugin indépendant, non affilié à l'OHADA et non approuvé par elle. « SYSCOHADA » désigne le référentiel
  comptable public de l'OHADA.

## Confidentialité

- Le plugin ne collecte, ne stocke et ne transmet aucune donnée. Il ne contient aucun code exécutable :
  seulement des fichiers Markdown, pour les instructions destinées à Claude et les exemples fictifs, son
  manifeste JSON et son icône.
- Pour un rapprochement, Claude lit les fichiers que vous lui fournissez et applique la méthode de la skill
  avec ses propres outils, dans votre session. Les numéros de téléphone sont masqués dans les résultats.
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
chart of accounts lookup, balanced journal entries, mobile money statement reconciliation (a documented,
read-only method), income statement from a trial balance, and a SYSCOHADA-to-IFRS restatement checklist.
It collects no data, never executes payments and contains no executable code: only Markdown files for the
instructions and the fictitious examples, its JSON manifest and its icon. For a reconciliation, Claude reads
the files you provide and applies the documented method with its own tools, in your session. Version 0.1.6: the
accounting content was reviewed by a chartered accountant in
October 2026. Independent project, not affiliated with or endorsed by OHADA. Privacy: [PRIVACY.md](PRIVACY.md).
Security: [SECURITY.md](SECURITY.md).
