# TODO - Script Python Echo Prénom

---

## Légende

| Symbole | Signification |
|---|---|
| 🔴 Mandatory | Action obligatoire (priorité CRITIQUE ou HAUTE) |
| 🟡 Optionnel | Action souhaitable (priorité MOYENNE ou BASSE) |
| ✅ Fait | Action complétée |
| 🔄 En cours | Action en cours de réalisation |
| ⬜ À faire | Action non démarrée |

---

## Vue d'ensemble

| Phase / Thématique | Nb actions | Owner(s) | ETA | Statut |
|---|---|---|---|---|
| Phase 1 : Configuration et Structure de Base | 2 | Mathias (Dev) | 16 fév. 2026 | ⬜ À faire |
| Phase 2 : Traitement et Affichage de Base | 3 | Mathias (Dev) | 17 fév. 2026 | ⬜ À faire |
| Phase 3 : Validation et Gestion des Erreurs | 3 | Mathias (Dev) | 17 fév. 2026 | ⬜ À faire |
| Phase 4 : Support des Caractères Spéciaux | 3 | Mathias (Dev) | 18 fév. 2026 | ⬜ À faire |
| Phase 5 : Documentation et Qualité du Code | 4 | Mathias (Dev) | 18 fév. 2026 | ⬜ À faire |
| Phase 6 : Tests et Validation | 3 | Thibault P. (QA) | 19 fév. 2026 | ⬜ À faire |

---

## Phase 1 : Configuration et Structure de Base

### T1.1 — Créer le fichier `script.py`

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 16 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | Aucune |

**Description :** Créer le fichier `script.py` avec la docstring d'en-tête, les imports (`argparse`, `sys`) et la fonction `main()`.

---

### T1.2 — Configurer `argparse`

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 16 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T1.1 |

**Description :** Initialiser `ArgumentParser`, ajouter la description du script, définir l'argument positional "prenom" et parser les arguments.

---

## Phase 2 : Traitement et Affichage de Base

### T2.1 — Implémenter la capture d'argument (US-001)

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 17 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T1.2 |

**Description :** Récupérer l'argument prénom, vérifier qu'il est bien capturé et tester avec `python script.py Jean`.

---

### T2.2 — Implémenter l'affichage (US-002)

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product), Aurélien D. (Group PM) |
| **ETA** | 17 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T2.1 |

**Description :** Créer la fonction `echo_prenom(prenom)` et afficher "Bonjour {prenom}!". Tester le format et l'affichage.

---

### T2.3 — Intégrer dans `main()`

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 17 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T2.2 |

**Description :** Appeler `echo_prenom(args.prenom)` depuis `main()` et tester l'exécution complète.

---

## Phase 3 : Validation et Gestion des Erreurs

### T3.1 — Gérer l'absence d'argument (US-003)

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead), Thibault P. (QA) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 17 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T2.3 |

**Description :** Vérifier que `argparse` gère automatiquement l'absence d'argument et que le message d'erreur est approprié. Tester `python script.py` sans argument.

---

### T3.2 — Gérer les arguments vides (US-004)

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead), Thibault P. (QA) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 17 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T2.3 |

**Description :** Créer la fonction `valider_prenom(prenom)` avec `str.strip()`, afficher un message d'erreur sur stderr si vide, et retourner exit code 1.

---

### T3.3 — Intégrer la validation dans `main()`

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead), Thibault P. (QA) |
| **Informé** | Séraphin D. (Product), Aurélien D. (Group PM) |
| **ETA** | 17 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T3.2 |

**Description :** Appeler `valider_prenom()` avant `echo_prenom()` dans `main()` et tester les cas limites.

---

## Phase 4 : Support des Caractères Spéciaux

### T4.1 — Assurer l'encodage UTF-8 (US-005)

| Champ | Valeur |
|---|---|
| **Priorité** | 🟡 Optionnel |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 18 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T3.3 |

**Description :** Vérifier que Python 3 gère nativement UTF-8, ajouter le shebang et l'encoding si nécessaire, tester avec des accents.

---

### T4.2 — Tester les cas particuliers (US-005)

| Champ | Valeur |
|---|---|
| **Priorité** | 🟡 Optionnel |
| **Owner(s)** | Thibault P. (QA) |
| **Consulté** | Mathias (Dev) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 18 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T4.1 |

**Description :** Tester José (accents), Jean-Pierre (tirets), O'Connor (apostrophes), François (accents français).

---

### T4.3 — Documenter les limitations UTF-8

| Champ | Valeur |
|---|---|
| **Priorité** | 🟡 Optionnel |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 18 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T4.2 |

**Description :** Ajouter des commentaires sur la gestion UTF-8 et des exemples dans la docstring.

---

## Phase 5 : Documentation et Qualité du Code

### T5.1 — Ajouter les docstrings (US-007)

| Champ | Valeur |
|---|---|
| **Priorité** | 🟡 Optionnel |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead), Kenza B. (Design) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 18 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T4.3 |

**Description :** Ajouter la docstring d'en-tête complète et une docstring pour chaque fonction au format Description / Args / Returns.

---

### T5.2 — Ajouter des commentaires explicites

| Champ | Valeur |
|---|---|
| **Priorité** | 🟡 Optionnel |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 18 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T5.1 |

**Description :** Commenter les sections logiques, expliquer les validations, utiliser des noms de variables explicites.

---

### T5.3 — Respecter PEP 8

| Champ | Valeur |
|---|---|
| **Priorité** | 🟡 Optionnel |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 18 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T5.2 |

**Description :** Appliquer indentation 4 espaces, longueur max 79 caractères, noms en snake_case, espaces autour des opérateurs.

---

### T5.4 — Créer un `README.md`

| Champ | Valeur |
|---|---|
| **Priorité** | 🟡 Optionnel |
| **Owner(s)** | Mathias (Dev) |
| **Consulté** | Kenza B. (Design), Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product), Aurélien D. (Group PM) |
| **ETA** | 18 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T5.3 |

**Description :** Rédiger le README.md avec installation, utilisation, exemples d'exécution et gestion des erreurs.

---

## Phase 6 : Tests et Validation

### T6.1 — Tests manuels

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | Thibault P. (QA) |
| **Consulté** | Mathias (Dev), Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product), Aurélien D. (Group PM) |
| **ETA** | 19 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T5.4 |

**Description :** Créer un fichier de tests manuels et exécuter tous les cas d'usage (nominaux, erreurs, caractères spéciaux, aide).

---

### T6.2 — Tests unitaires

| Champ | Valeur |
|---|---|
| **Priorité** | 🟡 Optionnel |
| **Owner(s)** | Thibault P. (QA) |
| **Consulté** | Mathias (Dev), Thibault R. (IT Lead) |
| **Informé** | Séraphin D. (Product) |
| **ETA** | 19 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T6.1 |

**Description :** Créer `tests/test_script.py` pour tester `valider_prenom()` et `echo_prenom()`.

---

### T6.3 — Validation des critères d'acceptation

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | Thibault P. (QA) |
| **Consulté** | Mathias (Dev), Séraphin D. (Product) |
| **Informé** | Aurélien D. (Group PM), Thibault R. (IT Lead) |
| **ETA** | 19 février 2026 |
| **Statut** | ⬜ À faire |
| **Dépendances** | T6.2 |

**Description :** Cocher tous les critères d'acceptation dans Specs.md et documenter les résultats de validation.

---

## Matrice RACI simplifiée

| Action | Owner | Consulté | Informé |
|---|---|---|---|
| T1.1 — Créer script.py | Mathias (Dev) | Thibault R. (IT Lead) | Séraphin D. (Product) |
| T1.2 — Configurer argparse | Mathias (Dev) | Thibault R. (IT Lead) | Séraphin D. (Product) |
| T2.1 — Capturer argument | Mathias (Dev) | Thibault R. (IT Lead) | Séraphin D. (Product) |
| T2.2 — Implémenter affichage | Mathias (Dev) | Thibault R. (IT Lead) | Séraphin D. (Product), Aurélien D. (Group PM) |
| T2.3 — Intégrer main() | Mathias (Dev) | Thibault R. (IT Lead) | Séraphin D. (Product) |
| T3.1 — Gérer absence argument | Mathias (Dev) | Thibault R. (IT Lead), Thibault P. (QA) | Séraphin D. (Product) |
| T3.2 — Gérer arguments vides | Mathias (Dev) | Thibault R. (IT Lead), Thibault P. (QA) | Séraphin D. (Product) |
| T3.3 — Intégrer validation | Mathias (Dev) | Thibault R. (IT Lead), Thibault P. (QA) | Séraphin D. (Product), Aurélien D. (Group PM) |
| T4.1 — Encodage UTF-8 | Mathias (Dev) | Thibault R. (IT Lead) | Séraphin D. (Product) |
| T4.2 — Tester caractères spéciaux | Thibault P. (QA) | Mathias (Dev) | Séraphin D. (Product) |
| T4.3 — Documenter limitations | Mathias (Dev) | Thibault R. (IT Lead) | Séraphin D. (Product) |
| T5.1 — Docstrings | Mathias (Dev) | Thibault R. (IT Lead), Kenza B. (Design) | Séraphin D. (Product) |
| T5.2 — Commentaires | Mathias (Dev) | Thibault R. (IT Lead) | Séraphin D. (Product) |
| T5.3 — PEP 8 | Mathias (Dev) | Thibault R. (IT Lead) | Séraphin D. (Product) |
| T5.4 — README.md | Mathias (Dev) | Kenza B. (Design), Thibault R. (IT Lead) | Séraphin D. (Product), Aurélien D. (Group PM) |
| T6.1 — Tests manuels | Thibault P. (QA) | Mathias (Dev), Thibault R. (IT Lead) | Séraphin D. (Product), Aurélien D. (Group PM) |
| T6.2 — Tests unitaires | Thibault P. (QA) | Mathias (Dev), Thibault R. (IT Lead) | Séraphin D. (Product) |
| T6.3 — Validation finale | Thibault P. (QA) | Mathias (Dev), Séraphin D. (Product) | Aurélien D. (Group PM), Thibault R. (IT Lead) |

---

## Version
**Version** : 1.0
**Date** : 9 mars 2026
**Statut** : En cours de rédaction
