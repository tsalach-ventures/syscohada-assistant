# Sécurité

*English version below.*

## Signaler une vulnérabilité

Merci de ne pas ouvrir d'issue publique pour une faille de sécurité. Écrivez à steph@tsalach.ventures en
indiquant la version concernée, le fichier en cause et, si possible, un exemple qui reproduit le problème.
Nous accusons réception, puis nous publions le correctif dans une nouvelle version, mentionnée dans
CHANGELOG.md.

## Versions maintenues

Seule la dernière version publiée reçoit des correctifs.

## Périmètre

Le plugin n'exécute aucun paiement, ne demande aucun identifiant et n'accède pas au réseau. Sa seule partie
exécutable, `skills/mobile-money/scripts/rapprocher.py`, lit des fichiers CSV et écrit un fichier CSV.

---

# Security

## Reporting a vulnerability

Please do not open a public issue for a security problem. Email steph@tsalach.ventures with the affected
version, the file involved and, if possible, an example that reproduces the problem. We acknowledge
receipt, then ship the fix in a new version, recorded in CHANGELOG.md.

## Supported versions

Only the latest published version receives fixes.

## Scope

The plugin executes no payments, asks for no credentials and has no network access. Its only executable
part, `skills/mobile-money/scripts/rapprocher.py`, reads CSV files and writes one CSV file.
