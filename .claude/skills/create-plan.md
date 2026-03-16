# Skill : Générer le Plan d'Implémentation

## Déclencheur
Utiliser ce skill quand l'utilisateur demande de "générer le plan", "créer le plan d'implémentation", "create plan" ou "generate plan" pour un projet.

## Objectif
Générer un fichier `Plan.md` de plan d'implémentation complet et interactif à partir du `Specs.md` d'un projet, en suivant la structure standard de l'équipe.

---

## Sources requises

**Fichiers d'entrée (par ordre de priorité) :**
1. `Specs.md` dans le dossier du projet (source principale)
2. `Brief.md` dans le dossier du projet (contexte, contraintes, risques)
3. `brief-{nom-projet}.md` dans `docs/{nom-projet}/`

**Chemin de sortie :** dans le même dossier que les sources (`Plan.md`)

---

## Étape 0 : Vérification préalable (avant de poser les questions)

### Vérifier si Plan.md existe déjà
Avant toute action, vérifier si un fichier `Plan.md` existe dans le dossier cible.
- **Si oui** : demander à l'utilisateur : *"Un fichier `Plan.md` existe déjà dans ce dossier. Voulez-vous l'écraser ou créer `Plan-v2.md` ?"* Attendre la réponse avant de continuer.
- **Si non** : continuer directement vers le processus interactif.

---

## Étape 1 : Processus interactif

Poser les questions suivantes à l'utilisateur dans un seul message :

```
Pour générer le Plan d'Implémentation, j'ai besoin de quelques informations :

1. **Durée estimée** : Combien de temps prévoyez-vous pour ce projet ? (ex: 2-3 jours, 1 semaine)
2. **Équipe** : Combien de personnes travaillent sur ce projet ? (ex: 1 développeur, 2 développeurs)
3. **Rôles** : Quels sont les rôles dans l'équipe ? (ex: Lead Dev, Tech Lead, QA)
4. **Date de début** : Quelle est la date de début prévue ? (ex: 16 février 2026)
5. **Langage principal** : Quel langage de programmation est utilisé ? (ex: Python, JavaScript, TypeScript)
   → Laisser vide pour déduire automatiquement depuis le Specs.md
6. **Environnement** : Quel environnement d'exécution ? (ex: Python 3.9+, Node.js 18+)
   → Laisser vide pour déduire automatiquement depuis le Specs.md
```

Attendre la réponse de l'utilisateur avant de continuer.

---

## Étape 2 : Traitement des réponses

### Fallback pour questions 5 et 6 sans réponse
Si l'utilisateur n'a pas répondu aux questions 5 (langage) ou 6 (environnement) :
- Lire le `Specs.md` et le `Brief.md` pour déduire le langage (ex: mentions de `python`, `argparse`, `node`, `npm`, etc.)
- Lire les "Détails Techniques" de chaque US pour identifier la version d'environnement (ex: "Python 3.7 ou supérieur requis")
- Informer l'utilisateur de la déduction : *"Langage déduit depuis Specs.md : Python | Environnement : Python 3.7+"*
- Si aucune déduction n'est possible, utiliser "À préciser" et laisser un commentaire dans le Plan.md généré

### Vérification cohérence équipe / rôles
Après réception des réponses, vérifier la cohérence entre le nombre de personnes (question 2) et les rôles listés (question 3) :
- **Incohérence détectée** (ex: "1 développeur" + "Dev Front-end, Dev Back-end, QA") : signaler à l'utilisateur avant de générer :
  *"Attention : vous avez indiqué 1 développeur mais 3 rôles distincts. Je génère le plan avec ces informations telles quelles — un seul développeur assumera tous les rôles."*
- **Cohérence confirmée** : continuer sans commentaire.

### Inférence des livrables depuis les Specs
Identifier le ou les fichiers livrables à partir des Specs et du Brief :
- Chercher les mentions de fichiers concrets dans les "Détails Techniques" (ex: `python script.py`, `index.js`, `app.ts`)
- Si aucun fichier n'est mentionné, utiliser le nom du projet en snake_case + extension du langage détecté (ex: `hello_world.py`)
- Lister également `Brief.md`, `Specs.md` et `Plan.md` comme livrables de documentation

---

## Étape 3 : Règles de génération du contenu

1. **Phases** : regrouper les US par priorité et logique fonctionnelle (CRITIQUE → HAUTE → MOYENNE). Les noms de phases sont **fixes** (voir liste ci-dessous) — ne pas les renommer.
2. **Tâches** : découper chaque phase en tâches atomiques et ordonnées, préfixées `- [ ]`
3. **Code clé** : inclure des extraits de code concrets et fonctionnels pour chaque phase technique
4. **Critères d'acceptance** : reprendre exactement les critères d'acceptation des Specs sous forme de checklist `- [ ]`
5. **Critères de validation** : ajouter des critères techniques vérifiables (commandes exécutables, sorties attendues, exit codes)
6. **Risques** : voir section "Risques sans Brief.md" ci-dessous
7. **Ordre** : toujours respecter les dépendances entre US définies dans la Matrice de Traçabilité des Specs
8. **Stack** : utiliser les réponses de l'utilisateur ou les valeurs déduites
9. **Suivi** : inclure des points de contrôle réalistes alignés sur les phases, avec un critère de succès mesurable par commande

### Noms de phases standardisés (ne pas modifier)
Les noms de phases dans le fichier généré doivent toujours correspondre exactement à :
- PHASE 1 : Configuration et Structure de Base
- PHASE 2 : Traitement et Affichage de Base
- PHASE 3 : Validation et Gestion des Erreurs
- PHASE 4 : Support des Caractères Spéciaux et Internationalisation
- PHASE 5 : Accessibilité et Documentation
- PHASE 6 : Tests et Validation

### Risques sans Brief.md
Si `Brief.md` est absent ou ne contient pas de section risques :
- Générer des risques génériques cohérents avec la stack identifiée et les contraintes des Specs
- Toujours inclure au minimum 3 risques issus de cette liste selon le contexte :

| Contexte | Risques génériques à inclure |
|---|---|
| Script CLI (Python) | Encodage UTF-8 sur Windows, version Python incompatible, dépassement contrainte mémoire/temps |
| API REST (Node/Python) | Timeout réseau, gestion des erreurs HTTP, sécurité des inputs |
| Application web | Compatibilité navigateurs, performance chargement, accessibilité |
| Base de données | Migration de schéma, intégrité des données, performances des requêtes |

---

## Structure du fichier Plan.md à générer

````markdown
# Plan d'Implémentation - {Titre du Projet}

---

## 1. Aperçu du Plan

| Champ | Valeur |
|---|---|
| **Durée estimée** | {réponse utilisateur} |
| **Équipe** | {réponse utilisateur} |
| **Rôles** | {réponse utilisateur} |
| **Date de début** | {réponse utilisateur} |

> {note de cohérence si incohérence équipe/rôles détectée — supprimer ce bloc sinon}

---

## 2. Architecture et Stack Technique

### Stack Recommandée

| Composant | Valeur |
|---|---|
| **Langage** | {réponse utilisateur ou valeur déduite} |
| **Module principal** | {module clé identifié dans les Specs} |
| **Modules standard** | {liste des modules/libs de la stdlib} |
| **Modules custom** | {libs tierces si nécessaire, sinon "Aucun"} |
| **Environnement** | {réponse utilisateur ou valeur déduite} |
| **Contrôle de version** | Git |

### Structure du Projet

```
{nom-projet}/
├── {fichier principal déduit}.{ext}
├── Brief.md
├── Specs.md
└── Plan.md
```

---

## 3. Phases d'Implémentation

---

### PHASE 1 : Configuration et Structure de Base

#### Objectif
{Mettre en place la structure de base du script/application et les fondations techniques — sans logique métier}

#### Tâches
- [ ] {tâche concrète 1}
- [ ] {tâche concrète 2}
- [ ] {tâche concrète 3}

#### Code clé
```{langage}
{extrait de code pertinent et fonctionnel}
```

#### Critères d'acceptance
- [ ] {critère repris directement des Specs — ce que l'utilisateur doit pouvoir faire}
- [ ] {critère repris directement des Specs}

#### Critères de validation
- [ ] {critère technique vérifiable avec commande concrète et sortie attendue}
- [ ] {critère technique vérifiable}

---

### PHASE 2 : Traitement et Affichage de Base

#### Objectif
{Implémenter la logique principale de traitement et d'affichage — US priorité CRITIQUE}

#### Tâches
- [ ] {tâche concrète 1}
- [ ] {tâche concrète 2}

#### Code clé
```{langage}
{extrait de code pertinent et fonctionnel}
```

#### Critères d'acceptance
- [ ] {critère repris des Specs}
- [ ] {critère repris des Specs}

#### Critères de validation
- [ ] {critère technique vérifiable avec commande et sortie attendue}
- [ ] {critère technique vérifiable}

---

### PHASE 3 : Validation et Gestion des Erreurs

#### Objectif
{Ajouter la gestion des cas limites, arguments invalides et messages d'erreur — US priorité HAUTE}

#### Tâches
- [ ] {tâche concrète 1}
- [ ] {tâche concrète 2}

#### Code clé
```{langage}
{extrait de code pertinent et fonctionnel}
```

#### Critères d'acceptance
- [ ] {critère repris des Specs}
- [ ] {critère repris des Specs}

#### Critères de validation
- [ ] {critère technique vérifiable avec exit code attendu}
- [ ] {critère technique vérifiable}

---

### PHASE 4 : Support des Caractères Spéciaux et Internationalisation

#### Objectif
{Assurer la compatibilité encodage (UTF-8) et le traitement des entrées internationales}

#### Tâches
- [ ] {tâche concrète 1}
- [ ] {tâche concrète 2}

#### Code clé
```{langage}
{extrait de code pertinent et fonctionnel}
```

#### Critères d'acceptance
- [ ] {critère repris des Specs}
- [ ] {critère repris des Specs}

#### Critères de validation
- [ ] {critère technique vérifiable — sortie attendue sans corruption}
- [ ] {critère technique vérifiable}

---

### PHASE 5 : Accessibilité et Documentation

#### Objectif
{Vérifier que le code est utilisable, documenté et conforme aux standards — US priorité MOYENNE}

#### Tâches
- [ ] {tâche concrète 1}
- [ ] {tâche concrète 2}

#### Code clé
```{langage}
{extrait de code pertinent et fonctionnel}
```

#### Critères d'acceptance
- [ ] {critère repris des Specs}
- [ ] {critère repris des Specs}

#### Critères de validation
- [ ] {critère technique vérifiable — ex: outil de lint, revue manuelle}
- [ ] {critère technique vérifiable}

---

### PHASE 6 : Tests et Validation

#### Objectif
{Exécuter et valider tous les scénarios définis dans les Specs sur l'ensemble des User Stories}

#### Tâches
- [ ] {tâche de test 1 — scénarios nominaux}
- [ ] {tâche de test 2 — cas d'erreur}
- [ ] {tâche de test 3 — performances et contraintes}

#### Code clé
```bash
{liste de commandes de test avec sortie attendue en commentaire}
```

#### Critères d'acceptance
- [ ] Tous les critères d'acceptance des {N} User Stories sont satisfaits
- [ ] Tous les cas limites définis dans les Specs sont testés
- [ ] Aucune régression entre les phases

#### Critères de validation
- [ ] 100% des commandes de test produisent la sortie attendue
- [ ] {contrainte de performance issue des Specs — ex: temps d'exécution < 100 ms}
- [ ] {contrainte de ressource issue des Specs — ex: mémoire < 10 MB}
- [ ] Aucun `Traceback` ou exception non gérée

---

## 4. Matrice de Dépendances et Ordre d'Implémentation

| Étape | Description | User Stories | Priorité | Dépendances |
|---|---|---|---|---|
| 1.1 | {description} | — | CRITIQUE | Aucune |
| 1.2 | {description} | US-001 | CRITIQUE | Étape 1.1 |
| 2.1 | {description} | US-002 | CRITIQUE | Phase 1 |
| 3.1 | {description} | US-003 | HAUTE | Phase 2 |
| 3.2 | {description} | US-004 | HAUTE | Étape 3.1 |
| 4.1 | {description} | US-005 | MOYENNE | Phase 2 |
| 5.1 | {description} | US-006, US-007 | MOYENNE | Phase 4 |
| 6.1 | {description} | Toutes | CRITIQUE | Phases 1-5 |

---

## 5. Risques et Mitigation

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| {risque 1} | Faible/Moyen/Élevé | Faible/Moyen/Élevé | {mitigation concrète} |
| {risque 2} | Faible/Moyen/Élevé | Faible/Moyen/Élevé | {mitigation concrète} |
| {risque 3} | Faible/Moyen/Élevé | Faible/Moyen/Élevé | {mitigation concrète} |

---

## 6. Critères de Livraison

### Livrables

| Livrable | Description | Phase |
|---|---|---|
| `{fichier principal déduit}.{ext}` | {description fonctionnelle du livrable} | Phases 1-5 |
| `Plan.md` | Plan d'implémentation (ce document) | — |
| `Specs.md` | Spécifications fonctionnelles | — |
| `Brief.md` | Brief projet (si présent) | — |

### Validation Finale

- [ ] Tous les critères d'acceptance des {N} User Stories sont satisfaits
- [ ] Le code s'exécute sans erreur sur tous les scénarios nominaux
- [ ] Les cas limites sont gérés et retournent les codes d'erreur corrects
- [ ] Le code est documenté (docstrings, commentaires, conformité style)
- [ ] {contrainte de performance spécifique au projet — ex: < 100 ms, < 10 MB}

---

## 7. Suivi du Projet

### Points de Contrôle

| Point de contrôle | Phase | Critère de succès |
|---|---|---|
| Structure de base opérationnelle | Fin Phase 1 | {commande concrète — ex: `python script.py --help` sans erreur} |
| Fonctionnalité principale livrée | Fin Phase 2 | {commande concrète — ex: `python script.py Jean` → `Bonjour Jean!`} |
| Gestion des erreurs complète | Fin Phase 3 | {commande concrète — ex: exit code 1 sur entrée vide} |
| Support internationalisation validé | Fin Phase 4 | {commande concrète — ex: prénom accentué affiché sans corruption} |
| Accessibilité et docs vérifiées | Fin Phase 5 | {commande ou revue — ex: `--help` exit 0, lint sans erreur} |
| Tous les tests passent | Fin Phase 6 | 100% des commandes de test produisent la sortie attendue |

### Statut du Projet

| Phase | Statut | Notes |
|---|---|---|
| Phase 1 | A faire | — |
| Phase 2 | A faire | — |
| Phase 3 | A faire | — |
| Phase 4 | A faire | — |
| Phase 5 | A faire | — |
| Phase 6 | A faire | — |

---

## Annexe : Checklist de Développement

### Avant de commencer
- [ ] Lire le `Brief.md` en entier (si présent)
- [ ] Lire le `Specs.md` en entier
- [ ] Identifier les dépendances et l'ordre d'implémentation (section 4)
- [ ] Configurer l'environnement de développement ({environnement déduit ou fourni})
- [ ] Initialiser le dépôt Git

### Pendant le développement
- [ ] Suivre l'ordre des phases défini dans ce plan
- [ ] Valider chaque critère d'acceptance avant de passer à la phase suivante
- [ ] Committer après chaque phase complétée
- [ ] Documenter le code au fur et à mesure
- [ ] Tester chaque fonctionnalité dès son implémentation

### Après le développement
- [ ] Exécuter la suite de tests complète (Phase 6)
- [ ] Vérifier tous les critères de livraison (section 6)
- [ ] Relire le code pour la lisibilité
- [ ] Mettre à jour le statut du projet dans la section 7
- [ ] Créer le tag de version Git

---

## 8. Rapport

*À compléter à la fin du projet*

| Champ | Valeur |
|---|---|
| **Date de livraison** | — |
| **Durée réelle** | — |
| **Phases complétées** | — |
| **Écarts par rapport au plan** | — |
| **Points d'amélioration** | — |

---

## Version
**Version** : 1.0
**Date** : {date du jour}
**Statut** : En cours de rédaction
````

---

## Exemple concret (projet Hello World - Script Python Echo Prénom)

Basé sur `Brief.md` + `Specs.md` → produit `Plan.md`

**Sources utilisées :**
- `Brief.md` : contexte, contraintes de performance (< 100ms, < 10MB), risques, scope
- `Specs.md` : 7 User Stories avec critères d'acceptation et matrice de traçabilité

**Déductions appliquées :**
- Langage déduit depuis Specs.md : Python | Environnement : Python 3.7+
- Livrable inféré : `script.py` (depuis mention `python script.py` dans les Détails Techniques)
- Risques extraits du Brief.md (section risques présente)

**Structure produite :**

| Phase | Contenu | US couvertes | Priorité |
|---|---|---|---|
| Phase 1 | Configuration et Structure de Base | — | CRITIQUE |
| Phase 2 | Traitement et Affichage de Base | US-001, US-002 | CRITIQUE |
| Phase 3 | Validation et Gestion des Erreurs | US-003, US-004 | HAUTE |
| Phase 4 | Support des Caractères Spéciaux et Internationalisation | US-005 | MOYENNE |
| Phase 5 | Accessibilité et Documentation | US-006, US-007 | MOYENNE |
| Phase 6 | Tests et Validation | Toutes | CRITIQUE |
