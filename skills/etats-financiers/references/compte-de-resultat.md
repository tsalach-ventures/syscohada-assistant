# Compte de résultat SYSCOHADA révisé (modèle en liste)

Structure des rubriques et des soldes : modèle du compte de résultat SYSCOHADA révisé (vérifié le 24/09/2026
sur une reproduction du modèle, voir SOURCES.md à la racine du plugin). Colonne « Comptes » : correspondances
arbitrées lors de la relecture par un expert-comptable (octobre 2026). Les sous-comptes propres à l'entité
restent à rattacher à la rubrique de leur compte parent.

Convention : produits en positif, charges en négatif ; chaque solde X est une somme.

| Réf | Libellé | Comptes |
| --- | --- | --- |
| TA | Ventes de marchandises | 701 |
| RA | Achats de marchandises | 601 |
| RB | Variation de stocks de marchandises | 6031 |
| **XA** | **Marge commerciale (somme TA à RB)** | |
| TB | Ventes de produits fabriqués | 702, 703, 704 |
| TC | Travaux, services vendus | 705, 706 |
| TD | Produits accessoires | 707 |
| **XB** | **Chiffre d'affaires (TA + TB + TC + TD)** | |
| TE | Production stockée (ou déstockage) | 73 |
| TF | Production immobilisée | 72 |
| TG | Subventions d'exploitation | 71 |
| TH | Autres produits | 75 sauf 759 |
| TI | Transferts de charges d'exploitation | 781 |
| RC | Achats de matières premières et fournitures liées | 602 |
| RD | Variation de stocks de matières premières et fournitures liées | 6032 |
| RE | Autres achats | 604, 605, 608 |
| RF | Variation de stocks d'autres approvisionnements | 6033 |
| RG | Transports | 61 |
| RH | Services extérieurs | 62, 63 |
| RI | Impôts et taxes | 64 |
| RJ | Autres charges | 65 sauf 659 |
| **XC** | **Valeur ajoutée ((XB + RA + RB) + somme TE à RJ)** | |
| RK | Charges de personnel | 66 |
| **XD** | **Excédent brut d'exploitation (XC + RK)** | |
| TJ | Reprises d'amortissements, provisions et dépréciations | 791, 798, 799, 759 |
| RL | Dotations aux amortissements, aux provisions et dépréciations | 681, 691, 659 |
| **XE** | **Résultat d'exploitation (XD + TJ + RL)** | |
| TK | Revenus financiers et assimilés | 77 sauf 779 |
| TL | Reprises de provisions et dépréciations financières | 797, 779 |
| TM | Transferts de charges financières | 787 |
| RM | Frais financiers et charges assimilées | 67 sauf 679 |
| RN | Dotations aux provisions et aux dépréciations financières | 697, 679, 687 |
| **XF** | **Résultat financier (somme TK à RN)** | |
| **XG** | **Résultat des activités ordinaires (XE + XF)** | |
| TN | Produits des cessions d'immobilisations | 82 |
| TO | Autres produits HAO | 84, 86, 88 |
| RO | Valeurs comptables des cessions d'immobilisations | 81 |
| RP | Autres charges HAO | 83, 85 |
| **XH** | **Résultat hors activités ordinaires (somme TN à RP)** | |
| RQ | Participation des travailleurs | 87 |
| RS | Impôts sur le résultat | 89 |
| **XI** | **Résultat net (XG + XH + RQ + RS)** | |

## Points de vigilance

- XB additionne les ventes de marchandises (TA), pas la marge commerciale (XA).
- Les variations de stocks (603x) ont le signe de leur solde : un solde débiteur réduit la marge ou la valeur
  ajoutée, un solde créditeur l'augmente.
- Les cessions courantes d'immobilisations (654, 754) restent dans les activités ordinaires ; les cessions HAO
  passent par 81 et 82.

## Règles des rubriques financières (arbitrage d'octobre 2026)

| Réf | Comptes | Règle |
| --- | --- | --- |
| TK | 77 sauf 779 | Produits financiers réalisés : intérêts, escomptes obtenus, gains de change, revenus de placement. Le 779 en est exclu car c'est une reprise sur dépréciation ou provision. |
| TL | 797, 779 | 797 : reprises sur immobilisations et risques financiers à long terme ; 779 : reprises sur titres de placement et risques financiers à court terme. |
| RM | 67 sauf 679 | Charges financières réelles, décaissées ou courues : intérêts, escomptes accordés, pertes de change. Le 679 en est exclu car c'est une dotation aux dépréciations. |
| RN | 697, 679, 687 | 697 : dotations financières durables ; 679 : dépréciations à court terme (titres de placement, trésorerie) ; 687 : dotations aux amortissements à caractère financier (primes de remboursement des obligations). |
