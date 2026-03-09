# Skill : Générer le TODO

## Déclencheur
Utiliser ce skill quand l'utilisateur demande de "générer le todo", "créer le todo", "create todo" ou "generate todo" pour un projet.

## Objectif
Générer un fichier `TODO.md` de suivi des actions à partir du `Plan.md` d'un projet, de manière interactive, en identifiant les owners, les parties prenantes (consulté / informé), les ETA et les statuts, avec classification Mandatory / Optionnel.

---

## Sources requises

**Fichiers d'entrée (par ordre de priorité) :**
1. `Plan.md` dans le dossier du projet (source principale)
2. `Brief.md` dans le dossier du projet (contexte équipe, parties prenantes)
3. `Specs.md` dans le dossier du projet (priorités des US)

**Chemin de sortie :** dans le même dossier que les sources (`TODO.md`)

---

## Étape 0 : Vérification préalable (avant de poser les questions)

### R1 — Vérifier si Plan.md existe
Avant toute action, vérifier si un fichier `Plan.md` existe dans le dossier cible.
- **Si non** : stopper et afficher le message suivant :
  *"Aucun fichier `Plan.md` trouvé dans ce dossier. Ce skill nécessite un Plan.md existant. Utilisez d'abord le skill `create-plan` pour générer le plan d'implémentation."*
- **Si oui** : continuer.

### R4 — Vérifier si TODO.md existe déjà
- **Si oui** : demander à l'utilisateur : *"Un fichier `TODO.md` existe déjà dans ce dossier. Voulez-vous l'écraser ou créer `TODO-v2.md` ?"* Attendre la réponse avant de continuer.
- **Si non** : continuer directement vers le processus interactif.

---

## Étape 1 : Processus interactif

Poser les questions suivantes à l'utilisateur dans un seul message :

```
Pour générer le TODO, j'ai besoin de quelques informations :

1. **Owners** : Qui sont les owners potentiels des actions ? (noms, rôles ou équipes)
   → Laisser vide pour déduire automatiquement depuis le Plan.md (rôles de l'équipe)

2. **Parties prenantes** : Quelles sont les parties prenantes du projet ?
   → Préciser pour chacune si elle doit être Consultée ou Informée
   → Laisser vide pour déduire depuis le Brief.md ou laisser "À définir"

3. **Format ETA** : Quel format de dates préférez-vous ?
   → Dates absolues (ex: 20 mars 2026), semaines relatives (ex: S+2), sprints (ex: Sprint 3)
   → Laisser vide pour calculer depuis la date de début du Plan.md

4. **Granularité** : Quel niveau de détail souhaitez-vous ?
   → Par phase (une entrée par phase)
   → Par tâche (une entrée par tâche `- [ ]`)
   → Par défaut : par phase
```

Attendre la réponse de l'utilisateur avant de continuer.

---

## Étape 2 : Traitement des réponses

### R2 — Fallback pour owners sans réponse
Si l'utilisateur n'a pas fourni d'owners :
- Lire la section "Aperçu du Plan" du `Plan.md` pour extraire les rôles (champ **Rôles**)
- Informer l'utilisateur : *"Owners déduits depuis Plan.md : {liste des rôles}"*
- Si aucun rôle n'est trouvé : utiliser `À définir`

### R3 — Fallback pour ETA sans réponse
Si l'utilisateur n'a pas fourni de format ETA :
- Lire la date de début dans la section "Aperçu du Plan" du `Plan.md` (champ **Date de début**)
- Calculer des ETA relatifs en semaines depuis cette date
- Informer l'utilisateur : *"ETA calculés depuis la date de début du Plan.md : {date}"*
- Si aucune date n'est trouvée : utiliser `À définir`

### R5 — Vérification cohérence owners / parties prenantes
- Si un owner est également listé comme partie prenante (Consulté/Informé) : signaler à l'utilisateur avant de générer :
  *"Attention : {nom} est listé à la fois comme owner et comme partie prenante. Je génère le TODO avec ces informations telles quelles."*

### Règle de classification Mandatory / Optionnel
- **🔴 Mandatory** : tâches issues de phases ou US de priorité CRITIQUE ou HAUTE dans le Plan.md
- **🟡 Optionnel** : tâches issues de phases ou US de priorité MOYENNE dans le Plan.md
- Si la priorité n'est pas explicite dans le Plan.md : utiliser `🔴 Mandatory` par défaut

---

## Étape 3 : Règles de génération du contenu

1. **Extraction** : lire la section "3. Phases d'Implémentation" du Plan.md pour les phases et tâches
2. **Dépendances** : lire la "Matrice de Dépendances et Ordre d'Implémentation" (section 4 du Plan.md)
3. **Granularité** : respecter le choix de l'utilisateur (par phase ou par tâche)
4. **Owner unique** : si plusieurs owners sont fournis, assigner le plus pertinent selon la phase (ex: QA pour la phase de tests)
5. **Matrice RACI simplifiée** : générer uniquement Owner, Consulté, Informé (pas de Responsable séparé)
6. **Statuts initiaux** : toutes les actions démarrent à `⬜ À faire`
7. **Vue d'ensemble** : toujours inclure le tableau récapitulatif en début de document

---

## Structure du fichier TODO.md à générer

````markdown
# TODO - {Titre du Projet}

---

## Légende

| Symbole | Signification |
|---|---|
| 🔴 Mandatory | Action obligatoire (priorité CRITIQUE ou HAUTE) |
| 🟡 Optionnel | Action souhaitable (priorité MOYENNE) |
| ✅ Fait | Action complétée |
| 🔄 En cours | Action en cours de réalisation |
| ⬜ À faire | Action non démarrée |

---

## Vue d'ensemble

| Phase / Thématique | Nb actions | Owner(s) | ETA | Statut |
|---|---|---|---|---|
| {Phase 1 : Configuration et Structure de Base} | {N} | {owner} | {ETA} | ⬜ À faire |
| {Phase 2 : Traitement et Affichage de Base} | {N} | {owner} | {ETA} | ⬜ À faire |
| {Phase 3 : Validation et Gestion des Erreurs} | {N} | {owner} | {ETA} | ⬜ À faire |
| {Phase 4 : Support des Caractères Spéciaux} | {N} | {owner} | {ETA} | ⬜ À faire |
| {Phase 5 : Accessibilité et Documentation} | {N} | {owner} | {ETA} | ⬜ À faire |
| {Phase 6 : Tests et Validation} | {N} | {owner} | {ETA} | ⬜ À faire |

---

## Phase 1 : Configuration et Structure de Base

### Action 1.1 : {titre de la tâche ou de la phase selon granularité}

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | {owner principal — nom ou rôle} |
| **Consulté** | {parties prenantes à consulter — ou "Aucun"} |
| **Informé** | {parties prenantes à informer — ou "Aucun"} |
| **ETA** | {date absolue, semaine relative ou sprint} |
| **Statut** | ⬜ À faire |
| **Dépendances** | {dépendances issues du Plan.md — ou "Aucune"} |

**Description :** {description courte issue du Plan.md}

---

### Action 1.2 : {titre}

| Champ | Valeur |
|---|---|
| **Priorité** | 🔴 Mandatory |
| **Owner(s)** | {owner} |
| **Consulté** | {consulté} |
| **Informé** | {informé} |
| **ETA** | {ETA} |
| **Statut** | ⬜ À faire |
| **Dépendances** | {dépendances} |

**Description :** {description}

---

[Répéter pour chaque action selon la granularité choisie]

---

## Phase 2 : Traitement et Affichage de Base

[Idem — une section par phase avec ses actions]

---

[Continuer pour toutes les phases du Plan.md]

---

## Matrice RACI simplifiée

| Action | Owner | Consulté | Informé |
|---|---|---|---|
| {Phase 1 — Action 1.1} | {owner} | {consulté} | {informé} |
| {Phase 1 — Action 1.2} | {owner} | {consulté} | {informé} |
| {Phase 2 — Action 2.1} | {owner} | {consulté} | {informé} |
| {Phase 3 — Action 3.1} | {owner} | {consulté} | {informé} |
| {Phase 4 — Action 4.1} | {owner} | {consulté} | {informé} |
| {Phase 5 — Action 5.1} | {owner} | {consulté} | {informé} |
| {Phase 6 — Action 6.1} | {owner} | {consulté} | {informé} |

---

## Version
**Version** : 1.0
**Date** : {date du jour}
**Statut** : En cours de rédaction
````

---

## Exemple concret (projet Hello World - Script Python Echo Prénom)

Voir `Training lab/Hello World/Plan.md` pour un exemple de source.

Résultat attendu à partir de ce Plan.md :
- **Phase 1** (Mandatory) : Configuration de base — Owner: Lead Dev — ETA: J+1 — Consulté: Tech Lead
- **Phase 2** (Mandatory) : Traitement et affichage — Owner: Lead Dev — ETA: J+2
- **Phase 3** (Mandatory) : Validation et erreurs — Owner: Lead Dev — ETA: J+3
- **Phase 4** (Mandatory) : Caractères spéciaux — Owner: Lead Dev — ETA: J+4
- **Phase 5** (Optionnel) : Documentation — Owner: Lead Dev — ETA: J+5 — Informé: QA
- **Phase 6** (Mandatory) : Tests et validation — Owner: QA / Lead Dev — ETA: J+6
