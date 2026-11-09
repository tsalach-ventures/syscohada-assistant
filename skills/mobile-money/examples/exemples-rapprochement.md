# Exemples fictifs pour le rapprochement mobile money

Ces deux jeux de données sont fictifs. Ils servent à vérifier que la méthode de
`references/methode-rapprochement.md` est bien appliquée ; le résultat attendu figure à la section 6 de
cette méthode.

Pour un essai, il suffit de demander à Claude : « Rapproche le relevé et les pièces d'exemple du plugin ».
Claude enregistre alors chaque bloc dans un fichier CSV (UTF-8, séparateur point-virgule), puis applique
la méthode. Les intitulés de colonnes suivent `references/format-csv.md`.

## Relevé du portefeuille (releve-exemple.csv)

Sept opérations de septembre 2026, avec une colonne de frais et le solde après chaque opération.

```csv
Date;Référence;Libellé;Montant;Frais;Solde
01/09/2026 08:15;MP260901.0815.A10001;Dépôt depuis banque;500000;0;750000
03/09/2026 10:02;MP260903.1002.B20002;Paiement reçu de 0707123456 - FAC-2026-031;236000;0;986000
05/09/2026 14:30;MP260905.1430.C30003;Paiement marchand Fournisseur Alpha F-0142;-590000;2950;393050
08/09/2026 09:47;MP260908.0947.D40004;Paiement reçu de 0101987654;118000;0;511050
10/09/2026 00:05;MP260910.0005.E50005;Frais de tenue de compte;-1000;0;510050
12/09/2026 16:20;MP260912.1620.F60006;Transfert reçu de 0505123456;75000;0;585050
15/09/2026 11:11;MP260915.1111.G70007;Retrait agent;-100000;1000;484050
```

## Pièces (pieces-exemple.csv)

Quatre factures : trois factures clients et une facture fournisseur.

```csv
Date;Référence;Tiers;Montant TTC;Type
28/08/2026;FAC-2026-031;Client Beta SARL;236000;client
20/08/2026;F-0142;Fournisseur Alpha SA;590000;fournisseur
02/09/2026;FAC-2026-035;Client Gamma;118000;client
10/09/2026;FAC-2026-040;Client Delta;354000;client
```
