# Script Python Echo Prénom

Un script Python simple et efficace qui affiche un message de salutation avec le prénom fourni en argument de ligne de commande.

## 📋 Description

Ce script démontre les concepts fondamentaux de la programmation Python :
- Gestion des arguments en ligne de commande avec `argparse`
- Validation robuste des entrées utilisateur
- Gestion des erreurs avec exit codes appropriés
- Support complet UTF-8 pour les caractères spéciaux
- Documentation et commentaires de qualité

## 📋 Installation

### Prérequis
- Python 3.7 ou supérieur
- Un terminal ou invite de commande

### Vérification de l'installation de Python
```bash
python --version
# ou
python3 --version
```

## 🚀 Utilisation

### Commande de base
```bash
python script.py <prénom>
```

### Exemples

**Cas simple**
```bash
python script.py Jean
# Sortie : Bonjour Jean!
```

**Prénom avec accents**
```bash
python script.py José
# Sortie : Bonjour José!
```

**Prénom composé**
```bash
python script.py Jean-Pierre
# Sortie : Bonjour Jean-Pierre!
```

**Prénom avec apostrophe**
```bash
python script.py "O'Connor"
# Sortie : Bonjour O'Connor!
```

**Prénom avec accents français**
```bash
python script.py François
# Sortie : Bonjour François!
```

### Afficher l'aide
```bash
python script.py -h
# ou
python script.py --help
```

## ⚠️ Gestion des Erreurs

### Erreur : Pas d'argument
```bash
python script.py
```
**Résultat** : Affiche l'aide et retourne exit code 1
```
usage: script.py [-h] <prénom>
script.py: error: the following arguments are required: <prénom>
```

### Erreur : Prénom vide
```bash
python script.py ""
```
**Résultat** : Affiche un message d'erreur et retourne exit code 1
```
Erreur : Le prénom ne peut pas être vide
```

### Erreur : Prénom avec seulement des espaces
```bash
python script.py "   "
```
**Résultat** : Affiche un message d'erreur et retourne exit code 1
```
Erreur : Le prénom ne peut pas être vide
```

## 📊 Exit Codes

| Code | Signification |
|---|---|
| 0 | Succès - Le script s'est exécuté correctement |
| 1 | Erreur - Argument manquant, vide ou invalide |

## 🔧 Architecture du Code

### Fonctions principales

#### `main()`
- Orchestration du programme
- Parse les arguments avec `argparse`
- Valide et affiche le prénom

#### `valider_prenom(prenom: str) -> str`
- Valide que le prénom n'est pas vide
- Nettoie les espaces superflus
- Quitte avec exit code 1 si invalide
- Retourne le prénom validé

#### `echo_prenom(prenom: str)`
- Affiche le message de salutation
- Format : "Bonjour {prénom}!"
- Respecte la casse et caractères spéciaux

## 🌐 Support des Caractères Spéciaux

Ce script supporte complètement l'UTF-8 :
- ✅ Accents : é, è, ê, ë, à, â, ô, ù, etc.
- ✅ Tirets : Jean-Pierre, Mary-Jane
- ✅ Apostrophes : O'Connor, D'Antonio
- ✅ Caractères internationaux : José, François, Müller
- ✅ Caractères accentués multiples

## 📝 Conventions de Code

Le code respecte les standards Python :
- **PEP 8** : Style et formatage
- **Docstrings** : Format Google avec descriptions détaillées
- **Commentaires** : Explications sur les sections clés
- **Noms explicites** : Variables et fonctions auto-documentées

## 🧪 Tests Manuels

### Plan de test complète

```bash
# Test 1 : Cas nominal - US-001 & US-002
python script.py Jean
# Attendu : Bonjour Jean!
# Exit code : 0

# Test 2 : Pas d'argument - US-003
python script.py
# Attendu : Message d'aide
# Exit code : 1

# Test 3 : Argument vide - US-004
python script.py ""
# Attendu : Erreur : Le prénom ne peut pas être vide
# Exit code : 1

# Test 4 : Argument avec espaces - US-004
python script.py "   "
# Attendu : Erreur : Le prénom ne peut pas être vide
# Exit code : 1

# Test 5 : José (accents) - US-005
python script.py José
# Attendu : Bonjour José!

# Test 6 : Jean-Pierre (tiret) - US-005
python script.py Jean-Pierre
# Attendu : Bonjour Jean-Pierre!

# Test 7 : O'Connor (apostrophe) - US-005
python script.py "O'Connor"
# Attendu : Bonjour O'Connor!

# Test 8 : François (accents français) - US-005
python script.py François
# Attendu : Bonjour François!

# Test 9 : Aide avec -h - US-006
python script.py -h
# Attendu : Affiche l'aide
# Exit code : 0

# Test 10 : Aide avec --help - US-006
python script.py --help
# Attendu : Affiche l'aide
# Exit code : 0
```

## 📂 Structure du Projet

```
Training lab/
├── script.py              # Script principal exécutable
├── README.md              # Documentation utilisateur (ce fichier)
├── brief.md               # Cahier des charges
├── Specs.md               # Spécifications techniques
├── Plan.md                # Plan d'implémentation
└── tests/
    └── test_script.py     # Tests unitaires (optionnel)
```

## 🔍 Vérification de la Qualité

Le code a été validé pour :
- [x] Respect de PEP 8
- [x] Docstrings complètes pour toutes les fonctions
- [x] Commentaires explicites
- [x] Noms de variables explicites
- [x] Gestion appropriée des erreurs
- [x] Support UTF-8 complète
- [x] Exit codes corrects

## 📖 Modules Utilisés

- **argparse** : Gestion des arguments CLI (standard library)
- **sys** : Accès aux arguments et gestion des exit codes (standard library)

**Aucune dépendance externe** - Utilise uniquement les modules standards Python

## 🐛 Limitations Connues

Aucune limitation majeure. Le script :
- Fonctionne sur Windows, macOS et Linux
- Gère les locales système différentes
- Supporte les prénoms de toute longueur
- Accepte les caractères Unicode

## 📞 Support

Pour toute question ou problème :
1. Vérifiez que Python 3.7+ est installé
2. Vérifiez la syntaxe de votre commande
3. Consultez l'aide : `python script.py -h`

## 📄 Licence

Ce script est fourni à titre éducatif.

---

**Version** : 1.0  
**Date** : 16 février 2026  
**Auteur** : Développeur
