# Politique de confidentialité — Assistant SYSCOHADA

Éditeur : Tsalach Ventures LLC · Dernière mise à jour : 27 octobre 2026 · *English version below.*

## En bref

Le plugin ne collecte, ne stocke et ne transmet aucune donnée. Tsalach Ventures LLC ne reçoit rien de ce
que vous traitez avec lui.

## Ce que contient le plugin

- Des instructions (skills) que Claude lit pour vous aider à appliquer le SYSCOHADA révisé.
- Un script Python, `rapprocher.py` (skill `mobile-money`). Il n'utilise que la bibliothèque standard et
  n'accède pas au réseau. Il lit le relevé CSV que vous lui indiquez (et, en option, la liste des pièces),
  puis écrit un fichier CSV de résultat à l'emplacement choisi.

## Données personnelles

Un relevé mobile money peut contenir des numéros de téléphone et des noms de contreparties. Le script les
traite là où il s'exécute (votre ordinateur ou votre session Claude) et masque les numéros de téléphone
dans son fichier de sortie, sauf si vous demandez le contraire (option `--sans-masquage`).

Vos échanges avec Claude restent régis par les conditions et la politique de confidentialité d'Anthropic :
le plugin n'y ajoute aucun destinataire.

## Conservation

Le plugin ne conserve rien. Les fichiers qu'il produit restent sous votre contrôle.

## Public visé

Professionnels de la comptabilité et de la gestion. Le plugin n'est pas destiné aux personnes de moins
de 18 ans.

## Contact

steph@tsalach.ventures

---

# Privacy policy — SYSCOHADA Assistant

Publisher: Tsalach Ventures LLC · Last updated: October 27, 2026

## Summary

The plugin collects, stores and transmits no data. Tsalach Ventures LLC receives nothing you process
with it.

## What the plugin contains

- Instructions (skills) that Claude reads to help you apply the revised SYSCOHADA framework.
- One Python script, `rapprocher.py` (`mobile-money` skill). It uses the Python standard library only and
  has no network access. It reads the CSV statement you point it to (and, optionally, a CSV list of
  invoices) and writes one CSV result file where you choose.

## Personal data

A mobile money statement can contain phone numbers and counterparty names. The script processes them
where it runs (your computer or your Claude session) and masks phone numbers in its output file unless
you ask otherwise (`--sans-masquage` option).

Your conversations with Claude remain governed by Anthropic's terms and privacy policy; the plugin adds
no recipient.

## Retention

The plugin keeps nothing. Files it produces stay under your control.

## Audience

Accounting and finance professionals. The plugin is not intended for people under 18.

## Contact

steph@tsalach.ventures
