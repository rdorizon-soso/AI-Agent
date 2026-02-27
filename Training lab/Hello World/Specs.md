# Spécifications Fonctionnelles - Script Python Echo Prénom

## User Stories et Critères d'Acceptation

---

### US-001 : Accepter un prénom en argument de ligne de commande

**En tant que** utilisateur
**Je souhaite** pouvoir passer mon prénom en argument à la ligne de commande
**Afin de** que le script le traite et l'affiche en réponse

#### Critères d'Acceptation
- [ ] La commande `python script.py Jean` exécute sans erreur
- [ ] Le script accepte un argument positional nommé "prénom"
- [ ] L'argument est stocké correctement dans une variable accessible
- [ ] Le script supporte les prénoms alphanumériques (lettres, tirets, apostrophes)
- [ ] Le script n'échoue pas si le prénom contient des accents (é, è, ê, etc.)

#### Détails Techniques
- Utiliser `sys.argv` ou `argparse` pour capturer l'argument
- Le script doit être exécutable via : `python script.py <prenom>`

---

### US-002 : Afficher le prénom fourni

**En tant que** utilisateur
**Je souhaite** recevoir une réponse affichant le prénom que j'ai saisi
**Afin de** confirmer que le script a bien traité mon entrée

#### Critères d'Acceptation
- [ ] Le script affiche le prénom saisi dans la console
- [ ] Le message de réponse est clair et lisible
- [ ] Le format est : `Bonjour <prénom>!` ou équivalent
- [ ] L'affichage ne contient pas d'erreurs ou de caractères corrompus
- [ ] Le prénom est affiché exactement comme saisi (respect de la casse)

#### Détails Techniques
- Utiliser `print()` pour l'affichage en console
- Format suggéré : `Bonjour {prénom}!`

---

### US-003 : Gérer l'absence d'argument

**En tant que** utilisateur
**Je souhaite** recevoir un message d'aide clair si je n'ai pas fourni d'argument
**Afin de** comprendre comment utiliser correctement le script

#### Critères d'Acceptation
- [ ] Si aucun argument n'est fourni, le script ne s'arrête pas abruptement
- [ ] Un message d'usage/aide s'affiche : "Usage: python script.py <prénom>"
- [ ] Le code d'erreur retourné est non-zéro (exit code 1)
- [ ] Le message est affiché sur la sortie erreur (stderr)
- [ ] L'utilisateur comprend comment corriger son utilisation

#### Détails Techniques
- Utiliser `sys.exit(1)` pour indiquer une erreur
- Utiliser `print(..., file=sys.stderr)` pour stderr
- Vérifier `len(sys.argv) < 2` ou utiliser argparse avec argument obligatoire

---

### US-004 : Gérer les arguments vides

**En tant que** développeur
**Je souhaite** que le script rejette les arguments vides ou ne contenant que des espaces
**Afin de** éviter des affichages incorrects ou des entrées invalides

#### Critères d'Acceptation
- [ ] La commande `python script.py ""` est rejetée avec un message d'erreur
- [ ] La commande `python script.py "   "` (espaces) est rejetée
- [ ] Un message explicite s'affiche : "Erreur : Le prénom ne peut pas être vide"
- [ ] Le code d'erreur retourné est 1
- [ ] La validation est effectuée avant l'affichage

#### Détails Techniques
- Utiliser `str.strip()` pour nettoyer les espaces
- Vérifier `if not prenom or not prenom.strip():`

---

### US-005 : Gérer les caractères spéciaux

**En tant que** utilisateur
**Je souhaite** que le script accepte les prénoms avec accents, tirets et apostrophes
**Afin de** que les prénoms composés et internationaux fonctionnent correctement

#### Critères d'Acceptation
- [ ] `python script.py "José"` affiche "Bonjour José!"
- [ ] `python script.py "Jean-Pierre"` affiche "Bonjour Jean-Pierre!"
- [ ] `python script.py "O'Connor"` affiche "Bonjour O'Connor!"
- [ ] `python script.py "François"` affiche "Bonjour François!"
- [ ] Aucun encodage UTF-8 n'est corrompu à l'affichage

#### Détails Techniques
- Assurer la compatibilité UTF-8 en Python 3
- Tester avec différents locales système

---

### US-007 : Code commenté et documenté

**En tant que** développeur
**Je souhaite** que le code soit bien commenté et documenté
**Afin de** pouvoir le maintenir ou le modifier facilement

#### Critères d'Acceptation
- [ ] Le fichier contient une docstring d'en-tête avec description et usage
- [ ] Chaque fonction contient une docstring expliquant son rôle
- [ ] Les sections logiques ont des commentaires
- [ ] Les variables ont des noms explicites
- [ ] Le code suit PEP 8 (style Python standard)

#### Détails Techniques
```python
"""
Script Echo Prénom
Description: Affiche le prénom fourni en argument
Usage: python script.py <prénom>
"""
```

---

## Matrice de Traçabilité

| User Story | Critère | Complexité | Dépendances |
|---|---|---|---|
| US-001 | Accepter argument CLI | Faible | Aucune |
| US-002 | Afficher le prénom | Faible | US-001 |
| US-003 | Gérer absence argument | Moyen | US-001 |
| US-004 | Gérer arguments vides | Moyen | US-001 |
| US-005 | Caractères spéciaux | Faible | Aucune |
| US-006 | Afficher l'aide | Faible | Aucune |
| US-007 | Code commenté | Faible | Aucune |

---

## Priorités

| Priorité | User Stories |
|---|---|
| CRITIQUE | US-001, US-002 |
| HAUTE | US-003, US-004 |
| MOYENNE | US-005, US-006, US-007 |

---

## Version
**Version** : 1.0
**Date** : 16 février 2026
**Statut** : En cours de rédaction
