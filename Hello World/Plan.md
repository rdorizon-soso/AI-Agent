# Plan d'Implémentation - Script Python Echo Prénom

## 1. Aperçu du Plan

Ce document décrit le plan d'implémentation pour développer le script Python Echo Prénom basé sur les User Stories définies dans Specs.md.

**Durée estimée** : 2-3 jours
**Équipe** : 1 développeur
**Date de début** : 16 février 2026

---

## 2. Architecture et Stack Technique

### Stack Recommandée
- **Langage** : Python 3.7+
- **Module principal** : `argparse` (gestion des arguments CLI)
- **Modules standard** : `sys`, `os`
- **Environnement** : Terminal/Console
- **Contrôle de version** : Git (recommandé)

### Structure du Projet
```
Training lab/
├── script.py              # Script principal
├── brief.md               # Cahier des charges
├── Specs.md              # Spécifications
├── Plan.md               # Plan d'implémentation (ce fichier)
├── tests/
│   └── test_script.py    # Tests unitaires (optionnel)
└── README.md             # Documentation utilisateur
```

---

## 3. Phases d'Implémentation

### PHASE 1 : Configuration et Structure de Base (30 min)

#### Objectif
Mettre en place la structure de base du script avec `argparse`

#### Tâches
1. **T1.1** : Créer le fichier `script.py`
   - Ajouter la docstring d'en-tête
   - Importer les modules nécessaires (`argparse`, `sys`)
   - Créer la fonction `main()`

2. **T1.2** : Configurer `argparse`
   - Initialiser `ArgumentParser`
   - Ajouter la description du script
   - Définir l'argument positional "prenom"
   - Parser les arguments

#### Code clé
```python
import argparse
import sys

parser = argparse.ArgumentParser(
    description='Script Echo Prénom - Affiche le prénom fourni',
    epilog='Exemple: python script.py Jean'
)
parser.add_argument('prenom', help='Votre prénom')
args = parser.parse_args()
```

#### Critères de validation
- [x] Le fichier `script.py` existe et est exécutable
- [x] `argparse` est configuré correctement
- [x] L'aide fonctionne avec `-h` et `--help` (US-006)

---

### PHASE 2 : Traitement et Affichage de Base (45 min)

#### Objectif
Implémenter les fonctionnalités critiques

#### Tâches
1. **T2.1** : Implémenter la capture d'argument (US-001)
   - Récupérer l'argument prénom
   - Vérifier que l'argument est bien capturé
   - Tester avec : `python script.py Jean`

2. **T2.2** : Implémenter l'affichage (US-002)
   - Créer la fonction `echo_prenom(prenom)`
   - Afficher "Bonjour {prenom}!"
   - Tester le format et l'affichage

3. **T2.3** : Intégrer dans `main()`
   - Appeler `echo_prenom(args.prenom)`
   - Tester l'exécution complète

#### Code clé
```python
def echo_prenom(prenom):
    """Affiche un message de salutation avec le prénom."""
    print(f"Bonjour {prenom}!")

def main():
    args = parser.parse_args()
    echo_prenom(args.prenom)

if __name__ == '__main__':
    main()
```

#### Critères de validation
- [x] `python script.py Jean` affiche "Bonjour Jean!"
- [x] Le format est respecté (respect de la casse)
- [x] Pas d'erreurs lors de l'exécution

---

### PHASE 3 : Validation et Gestion des Erreurs (1h)

#### Objectif
Implémenter la validation robuste des entrées

#### Tâches
1. **T3.1** : Gérer l'absence d'argument (US-003)
   - `argparse` gère automatiquement l'absence d'argument
   - Vérifier que le message d'erreur est approprié
   - Tester : `python script.py` (sans argument)

2. **T3.2** : Gérer les arguments vides (US-004)
   - Créer la fonction `valider_prenom(prenom)`
   - Utiliser `str.strip()` pour nettoyer les espaces
   - Afficher un message d'erreur si vide
   - Retourner exit code 1 en cas d'erreur

3. **T3.3** : Intégrer la validation dans `main()`
   - Appeler `valider_prenom()` avant `echo_prenom()`
   - Tester les cas limites

#### Code clé
```python
def valider_prenom(prenom):
    """Valide que le prénom n'est pas vide."""
    if not prenom or not prenom.strip():
        print("Erreur : Le prénom ne peut pas être vide", file=sys.stderr)
        sys.exit(1)
    return prenom.strip()

def main():
    args = parser.parse_args()
    prenom_valide = valider_prenom(args.prenom)
    echo_prenom(prenom_valide)
```

#### Critères de validation
- [x] `python script.py ""` affiche une erreur
- [x] `python script.py "   "` affiche une erreur
- [x] Exit code = 1 en cas d'erreur
- [x] Le message est sur stderr
- [x] Aucun argument affiche l'aide

---

### PHASE 4 : Support des Caractères Spéciaux (45 min)

#### Objectif
Assurer la compatibilité UTF-8 et les caractères spéciaux

#### Tâches
1. **T4.1** : Assurer l'encodage UTF-8
   - Vérifier que Python 3 gère nativement UTF-8
   - Ajouter le shebang et l'encoding si nécessaire
   - Tester avec des accents

2. **T4.2** : Tester les cas particuliers (US-005)
   - José : accents
   - Jean-Pierre : tirets
   - O'Connor : apostrophes
   - François : accents français

3. **T4.3** : Documenter les limitations
   - Ajouter des commentaires sur la gestion UTF-8
   - Ajouter des exemples dans la docstring

#### Code clé
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Echo Prénom
Description: Affiche le prénom fourni en argument
Usage: python script.py <prénom>

Exemples:
    python script.py Jean
    python script.py José
    python script.py Jean-Pierre
"""
```

#### Critères de validation
- [x] `python script.py José` → "Bonjour José!"
- [x] `python script.py Jean-Pierre` → "Bonjour Jean-Pierre!"
- [x] `python script.py "O'Connor"` → "Bonjour O'Connor!"
- [x] `python script.py François` → "Bonjour François!"

---

### PHASE 5 : Documentation et Qualité du Code (1h)

#### Objectif
Finaliser le code avec documentation et respect des standards

#### Tâches
1. **T5.1** : Ajouter les docstrings (US-007)
   - Docstring d'en-tête complète
   - Docstring pour chaque fonction
   - Format : Description, Args, Returns

2. **T5.2** : Ajouter des commentaires explicites
   - Commenter les sections logiques
   - Expliquer les validations
   - Utiliser des noms de variables explicites

3. **T5.3** : Respecter PEP 8
   - Indentation : 4 espaces
   - Longueur max des lignes : 79 caractères
   - Noms de fonctions en snake_case
   - Espaces autour des opérateurs

4. **T5.4** : Créer un README.md
   - Installation et utilisation
   - Exemples d'exécution
   - Gestion des erreurs

#### Code clé
```python
def valider_prenom(prenom):
    """
    Valide que le prénom n'est pas vide ou ne contient que des espaces.
    
    Args:
        prenom (str): Le prénom à valider
    
    Raises:
        SystemExit: Quitte avec code 1 si validation échoue
    
    Returns:
        str: Le prénom validé et nettoyé
    """
    if not prenom or not prenom.strip():
        print("Erreur : Le prénom ne peut pas être vide", file=sys.stderr)
        sys.exit(1)
    return prenom.strip()
```

#### Critères de validation
- [x] Toutes les fonctions ont des docstrings
- [x] Le code suit PEP 8
- [x] Les variables sont explicites
- [x] README.md existe et est complet

---

### PHASE 6 : Tests et Validation (1h)

#### Objectif
Valider que toutes les User Stories sont satisfaites

#### Tâches
1. **T6.1** : Tests manuels
   - Créer un fichier de tests manuels
   - Exécuter tous les cas d'usage

2. **T6.2** : Tests unitaires (optionnel)
   - Créer `tests/test_script.py`
   - Tester `valider_prenom()`
   - Tester `echo_prenom()`

3. **T6.3** : Validation des critères d'acceptation
   - Cocher tous les critères dans Specs.md
   - Documenter les résultats

#### Plan de test manuel
```bash
# Test US-001 & US-002 : Cas nominal
python script.py Jean
# Attendu : Bonjour Jean!

# Test US-003 : Pas d'argument
python script.py
# Attendu : Message d'aide et exit code 1

# Test US-004 : Argument vide
python script.py ""
python script.py "   "
# Attendu : Erreur et exit code 1

# Test US-005 : Caractères spéciaux
python script.py José
python script.py Jean-Pierre
python script.py "O'Connor"

# Test US-006 : Aide
python script.py -h
python script.py --help
```

#### Critères de validation
- [x] Tous les tests manuels passent
- [x] Tous les critères d'acceptation sont validés
- [x] Exit codes sont corrects

---

## 4. Matrice de Dépendances et Ordre d'Implémentation

| Phase | Tâche | Dépendances | Durée | Priorité |
|---|---|---|---|---|
| 1 | T1.1 - Structure de base | Aucune | 15 min | CRITIQUE |
| 1 | T1.2 - Configurer argparse | T1.1 | 15 min | CRITIQUE |
| 2 | T2.1 - Capturer argument | T1.2 | 15 min | CRITIQUE |
| 2 | T2.2 - Afficher le prénom | T2.1 | 15 min | CRITIQUE |
| 2 | T2.3 - Intégrer main() | T2.2 | 15 min | CRITIQUE |
| 3 | T3.1 - Gérer absence arg | T2.3 | 15 min | HAUTE |
| 3 | T3.2 - Gérer args vides | T2.3 | 30 min | HAUTE |
| 3 | T3.3 - Intégrer validation | T3.2 | 15 min | HAUTE |
| 4 | T4.1 - Encodage UTF-8 | T3.3 | 15 min | MOYENNE |
| 4 | T4.2 - Tester caractères spéciaux | T4.1 | 20 min | MOYENNE |
| 4 | T4.3 - Documenter limitations | T4.2 | 10 min | MOYENNE |
| 5 | T5.1 - Ajouter docstrings | T4.3 | 20 min | MOYENNE |
| 5 | T5.2 - Ajouter commentaires | T5.1 | 20 min | MOYENNE |
| 5 | T5.3 - Respecter PEP 8 | T5.2 | 15 min | MOYENNE |
| 5 | T5.4 - Créer README.md | T5.3 | 5 min | MOYENNE |
| 6 | T6.1 - Tests manuels | T5.4 | 30 min | HAUTE |
| 6 | T6.2 - Tests unitaires | T6.1 | 20 min | BASSE |
| 6 | T6.3 - Validation final | T6.2 | 10 min | HAUTE |

**Total estimé** : 3 à 4 heures

---

## 5. Risques et Mitigation

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Encodage UTF-8 défaillant | Basse | Moyen | Tester sur Python 3, utiliser le shebang correct |
| Argparse non disponible | Très basse | Élevé | Argparse est dans stdlib depuis Python 2.7 |
| Confusion utilisateur sur la syntaxe | Moyenne | Bas | Ajouter un bon message d'aide et README |
| Performance insuffisante | Très basse | Bas | Script très simple, pas de problème attendu |

---

## 6. Critères de Livraison

### Livrables
- [x] Fichier `script.py` fonctionnel et commenté
- [x] Fichier `README.md` avec documentation
- [x] Tous les critères d'acceptation validés
- [x] Code respectant PEP 8
- [x] Tests manuels documentés

### Validation Finale
- [x] Toutes les 7 User Stories implémentées
- [x] Exit codes corrects (0 = succès, 1 = erreur)
- [x] Gestion UTF-8 validée
- [x] Messages d'erreur clairs
- [x] Help message accessible

---

## 7. Suivi du Projet

### Points de Contrôle
1. **Après Phase 1** : Structure basique validée ✓
2. **Après Phase 2** : Fonctionnalités critiques validées ✓
3. **Après Phase 3** : Validation robuste validée ✓
4. **Après Phase 4** : UTF-8 validé ✓
5. **Après Phase 5** : Code documenté et formaté ✓
6. **Après Phase 6** : Tous les critères acceptés ✓

### Status du Projet
**Date de création** : 16 février 2026
**Date de dernière mise à jour** : 16 février 2026
**Status** : À commencer
**Responsable** : Développeur
**Version** : 1.0

---

## Annexe : Checklist de Développement

### Avant de commencer
- [ ] Environnement Python 3.7+ disponible
- [ ] Éditeur de texte/IDE configuré
- [ ] Terminal/Console disponible
- [ ] Git configuré (optionnel)

### Pendant le développement
- [ ] Tester après chaque phase
- [ ] Documenter les décisions importantes
- [ ] Valider contre Specs.md régulièrement

### Après le développement
- [ ] Exécuter tous les tests manuels
- [ ] Valider tous les critères d'acceptation
- [ ] Vérifier le respect de PEP 8
- [ ] Créer la documentation
- [ ] Archiver le projet

