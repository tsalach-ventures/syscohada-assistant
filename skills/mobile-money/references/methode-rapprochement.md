# Méthode de rapprochement mobile money

Méthode à appliquer telle quelle sur le relevé et, s'il existe, le fichier de pièces fournis par
l'utilisateur. Avec un outil d'exécution de code (Cowork, Claude Code, chat avec exécution de code), écrire
un court programme qui suit exactement ces règles ; sinon, les appliquer ligne par ligne. Travail en lecture
seule : ne jamais modifier les fichiers fournis, écrire tout résultat dans un nouveau fichier.

Formats lus (encodages, séparateurs, dates, montants, intitulés de colonnes) : `format-csv.md`.

## Paramètres par défaut

| Paramètre | Valeur | Quand la changer |
| --- | --- | --- |
| Fenêtre après la pièce | 60 jours | L'utilisateur indique d'autres délais de paiement |
| Tolérance avant la pièce | 3 jours | Des paiements précèdent souvent la facture |
| Compte des frais d'opérateur | 6317 | 6318 si le plan interne de l'entité n'a pas éclaté le 631 |
| Masquage des numéros de téléphone | Activé | Seulement sur demande explicite de l'utilisateur |

Note : Compte 6317 (Frais sur instruments de monnaie électronique) selon la nomenclature officielle SYSCOHADA révisé, paramétrable en 6318 si le plan de comptes interne de l'entité n'a pas éclaté le compte 631.

## 1. Préparer les mouvements du relevé

- Ignorer les lignes vides. Signaler chaque ligne dont la date ou le montant est illisible, avec son numéro
  de ligne, sans rien inventer.
- Montant : positif = entrée, négatif = sortie. Si une colonne sens existe, elle l'emporte : entrée, crédit,
  in, reçu, réception, encaissement ou « + » donnent un montant positif ; sortie, débit, out, envoi,
  paiement, retrait, décaissement ou « - » donnent un montant négatif.
- Frais : valeur absolue de la colonne frais, ou 0 sans cette colonne.
- Libellé masqué : remplacer chaque suite d'au moins 8 chiffres (un « + » initial, des espaces ou des points
  possibles entre les chiffres) par des X, en gardant les 2 derniers chiffres. Exemple : « 07 01 02 03 56 »
  devient « XXXXXXXX56 ». Tout ce qui est présenté ou exporté utilise le libellé masqué ; la recherche de
  références et de mots-clés utilise le libellé d'origine.
- Traiter les mouvements dans l'ordre chronologique : par date, puis dans l'ordre du fichier.

## 2. Préparer les pièces (si un fichier de pièces est fourni)

- Pour chaque pièce : référence, montant en valeur absolue, tiers, date si elle existe, et type « client » ou
  « fournisseur » si la colonne type commence par l'un de ces mots (sinon type inconnu).
- Une pièce ne sert qu'une seule fois.

## 3. Chercher la pièce de chaque mouvement

Pour un mouvement de montant non nul, une pièce est candidate si :

1. elle n'a pas encore servi ;
2. son montant est égal à la valeur absolue du montant du mouvement ;
3. son type, s'il est connu, est cohérent : entrée avec client, sortie avec fournisseur ;
4. si elle est datée, l'écart (date du mouvement moins date de la pièce, en jours) va de moins la tolérance
   (−3) à la fenêtre (+60).

Classer les candidates : d'abord celles dont la référence, comparée sans accents ni majuscules, figure dans
la référence ou le libellé d'origine du mouvement ; puis par écart absolu croissant, une pièce sans date
passant après les pièces datées. Retenir la première.

## 4. Classer chaque mouvement

Comparer les mots-clés sans accents ni majuscules. Appliquer la première ligne du tableau qui convient, de
haut en bas : une sortie sans pièce libellée « Frais de retrait » est donc classée en frais, pas en transfert.

| Cas | Statut | Compte de contrepartie | Commentaire |
| --- | --- | --- | --- |
| Pièce retenue, entrée | rapproche | 411 | « référence retrouvée » ou « montant et date » |
| Pièce retenue, sortie | rapproche | 401 | « référence retrouvée » ou « montant et date » |
| Sans pièce, sortie dont le libellé contient « frais », « commission » ou « fees » | frais | 6317 | TTC en charge ; TVA en 4454 seulement sur facture mensuelle conforme (NCC) |
| Sans pièce, libellé contenant « transfert vers banque », « transfert banque », « virement », « depot », « retrait », « cash in », « cash out », « alimentation » ou « rechargement compte » | transfert_interne_probable | 585 | à confirmer : mouvement entre trésoreries de l'entité |
| Tous les autres cas | non_rapproche | (vide) | aucune pièce de même montant dans la fenêtre |

Si le mouvement porte des frais (colonne frais non nulle), ajouter juste après lui une ligne de statut
« frais » : même date, même référence, même libellé masqué, montant égal à moins les frais, compte 6317,
commentaire « frais prélevés sur l'opération ; TTC en charge ; TVA en 4454 seulement sur facture mensuelle
conforme (NCC) ».

Un rapprochement « montant et date », sans référence retrouvée, reste une proposition à faire confirmer.

## 5. Présenter le résultat

- Un tableau par statut : nombre de lignes, total des entrées, total des sorties.
- Le détail ligne par ligne et, sur demande, un fichier CSV (séparateur point-virgule, UTF-8) avec les
  colonnes date (JJ/MM/AAAA), reference, libelle (masqué), montant, statut, piece_reference, piece_tiers,
  ecart_jours, compte_contrepartie, commentaire.
- Les pièces restées sans paiement : ce sont des relances possibles.
- La variation nette du portefeuille : somme des montants des mouvements moins somme des frais.
- Si la colonne solde existe : solde final = solde du dernier mouvement dans l'ordre chronologique ; solde
  d'ouverture implicite = solde final moins la variation nette. Comparer le solde final au solde du compte
  552 (ou de son sous-compte) après écritures.

## 6. Contrôle sur les exemples

Avec le relevé et les pièces de `examples/exemples-rapprochement.md` (données fictives), la méthode donne :
7 mouvements et 4 pièces lus ; 3 lignes rapprochées, 3 lignes de frais, 2 transferts internes probables et
1 ligne non rapprochée ; 1 pièce sans paiement (FAC-2026-040) ; une variation nette de 234 050 ; un solde
final de 484 050 et un solde d'ouverture implicite de 250 000. Un autre résultat signale une erreur
d'application de la méthode.
