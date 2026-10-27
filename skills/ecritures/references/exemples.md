# Exemples d'écritures SYSCOHADA

Montants en francs CFA (XOF). Taux de TVA de 18 % utilisé à titre d'exemple (taux normal en Côte d'Ivoire) :
toujours confirmer le taux applicable. Les frais et commissions des opérateurs de monnaie électronique
(Wave, Orange Money, MTN MoMo…) s'imputent en 6317 « Frais sur instruments monnaie électronique », sous le
631 « Frais bancaires » : ces opérateurs sont des prestataires de services de paiement agréés par la BCEAO,
pas des opérateurs de télécommunications (628).

> Note : Compte 6317 (Frais sur instruments de monnaie électronique) selon la nomenclature officielle SYSCOHADA révisé, paramétrable en 6318 si le plan de comptes interne de l'entité n'a pas éclaté le compte 631.

## 1. Achat de marchandises à crédit

Facture fournisseur : 1 000 000 HT, TVA 180 000, TTC 1 180 000.

| Journal | Compte | Intitulé | Débit | Crédit |
| --- | --- | --- | --- | --- |
| AC | 601 | Achats de marchandises | 1 000 000 | |
| AC | 4452 | TVA récupérable sur achats | 180 000 | |
| AC | 401 | Fournisseurs, dettes en compte | | 1 180 000 |

## 2. Vente de marchandises à crédit

Facture client : 2 000 000 HT, TVA 360 000, TTC 2 360 000.

| Journal | Compte | Intitulé | Débit | Crédit |
| --- | --- | --- | --- | --- |
| VT | 411 | Clients | 2 360 000 | |
| VT | 701 | Ventes de marchandises | | 2 000 000 |
| VT | 4431 | TVA facturée sur ventes | | 360 000 |

## 3. Encaissement d'un client par mobile money

Le client règle 236 000 sur le portefeuille mobile money de l'entité.

| Journal | Compte | Intitulé | Débit | Crédit |
| --- | --- | --- | --- | --- |
| MM | 552 | Monnaie électronique – téléphone portable | 236 000 | |
| MM | 411 | Clients | | 236 000 |

## 4. Paiement d'un fournisseur par mobile money, avec frais

Règlement de 1 180 000 ; l'opérateur prélève 5 900 de frais.

| Journal | Compte | Intitulé | Débit | Crédit |
| --- | --- | --- | --- | --- |
| MM | 401 | Fournisseurs, dettes en compte | 1 180 000 | |
| MM | 6317 | Frais sur instruments monnaie électronique | 5 900 | |
| MM | 552 | Monnaie électronique – téléphone portable | | 1 185 900 |

Frais prélevés sur simple relevé, sans facture conforme : le montant TTC reste en charge en 6317.

## 4 bis. Facture mensuelle de l'opérateur avec TVA

Les frais du mois ont été passés TTC en 6317 au fil des prélèvements (29 500). L'opérateur émet ensuite une
facture mensuelle conforme mentionnant son NCC : 25 000 HT et 4 500 de TVA. La TVA devient déductible et sort
de la charge.

| Journal | Compte | Intitulé | Débit | Crédit |
| --- | --- | --- | --- | --- |
| OD | 4454 | TVA récupérable sur services extérieurs et autres charges | 4 500 | |
| OD | 6317 | Frais sur instruments monnaie électronique | | 4 500 |

## 5. Alimentation du portefeuille mobile money depuis la banque

Virement interne de 500 000, enregistré via le compte de passage 585 (deux journaux).

| Journal | Compte | Intitulé | Débit | Crédit |
| --- | --- | --- | --- | --- |
| BQ | 585 | Virements de fonds | 500 000 | |
| BQ | 521 | Banques locales | | 500 000 |
| MM | 552 | Monnaie électronique – téléphone portable | 500 000 | |
| MM | 585 | Virements de fonds | | 500 000 |

Le compte 585 doit être soldé (solde nul) à chaque arrêté.

## Format CSV d'import (exemple 1)

```csv
date;journal;compte;libelle;debit;credit
15/09/2026;AC;601;Facture F-0142 fournisseur;1000000;
15/09/2026;AC;4452;Facture F-0142 fournisseur TVA;180000;
15/09/2026;AC;401;Facture F-0142 fournisseur;;1180000
```
