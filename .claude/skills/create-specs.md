# Skill : Générer les Spécifications Fonctionnelles

## Déclencheur
Utiliser ce skill quand l'utilisateur demande de "générer les specs", "créer les spécifications fonctionnelles", "create specs" ou "generate specs" pour un projet.

## Objectif
Générer un fichier `Specs.md` de spécifications fonctionnelles complet et interactif à partir d'un `Brief.md`, en suivant la structure standard de l'équipe.

---

## Sources requises

**Fichiers d'entrée (par ordre de priorité) :**
1. `Brief.md` dans le dossier du projet (source principale)
2. `brief-{nom-projet}.md` dans `docs/{nom-projet}/`
3. Contenu du brief copié-collé directement dans la conversation

**Chemin de sortie :** dans le même dossier que le brief source (`Specs.md`)

---

## Étape 0 : Vérification préalable (avant de poser les questions)

### Vérifier si Specs.md existe déjà
Avant toute action, vérifier si un fichier `Specs.md` existe dans le dossier cible.
- **Si oui** : demander à l'utilisateur : *"Un fichier `Specs.md` existe déjà dans ce dossier. Voulez-vous l'écraser ou créer `Specs-v2.md` ?"* Attendre la réponse avant de continuer.
- **Si non** : continuer directement vers le processus interactif.

---

## Étape 1 : Processus interactif

Poser les questions suivantes à l'utilisateur dans un seul message :

```
Pour générer les Spécifications Fonctionnelles, j'ai besoin de quelques informations :

1. **Personas** : Qui sont les utilisateurs de ce projet ? (ex: utilisateur final, développeur, admin)
   → Laisser vide pour déduire automatiquement depuis le Brief.md
2. **Contraintes techniques** : Y a-t-il des contraintes de performance ou d'environnement ?
   (ex: temps d'exécution < 100ms, mémoire < 10MB, Python 3.7+)
   → Laisser vide pour déduire depuis le Brief.md
3. **Périmètre** : Y a-t-il des fonctionnalités explicitement hors scope ?
   → Laisser vide si non précisé dans le Brief.md
```

Attendre la réponse de l'utilisateur avant de continuer.

---

## Étape 2 : Traitement des réponses

### Fallback pour questions sans réponse
Si l'utilisateur n'a pas répondu à une question :
- **Personas** : déduire depuis le Brief.md les acteurs mentionnés (ex: "l'utilisateur tape son prénom" → persona = utilisateur final)
- **Contraintes techniques** : extraire les contraintes explicites du Brief.md (ex: "doit s'exécuter en moins de 100ms"). Si aucune, ne pas inventer — laisser la section vide dans les Détails Techniques.
- **Périmètre hors scope** : extraire la section "Hors scope" ou "Exclusions" du Brief.md si elle existe. Si absente, ne pas générer de hors scope fictif.
- Informer l'utilisateur de chaque déduction : *"Personas déduits depuis Brief.md : utilisateur final, développeur"*

### Vérification de cohérence du Brief
Avant de générer, vérifier que le Brief.md contient les éléments minimaux :
- Un titre ou nom de projet identifiable
- Au moins un objectif ou fonctionnalité décrite

Si le Brief.md est trop vague ou incomplet, signaler à l'utilisateur les informations manquantes avant de générer.

### Inférence du nom de fichier livrable
Chercher dans le Brief.md les mentions de fichiers concrets ou de commandes (ex: `python script.py`, `node index.js`) pour identifier le livrable principal — utile pour renseigner les Détails Techniques des US.

---

## Étape 3 : Règles de génération du contenu

1. **Extraction des User Stories** : chaque objectif du brief devient au moins une US. Chaque critère de succès du brief devient un critère d'acceptation.
2. **Personas** : utiliser les réponses de l'utilisateur ou les valeurs déduites. Varier les personas selon le contexte de chaque US (ex: US-007 "Code documenté" → persona = développeur).
3. **Critères d'acceptation** : formuler en termes mesurables et testables, préfixés `- [ ]`. Inclure les commandes concrètes quand c'est possible (ex: `python script.py Jean` plutôt que "le script accepte un prénom").
4. **Détails Techniques** : inclure les contraintes de performance issues du Brief ou des réponses utilisateur. Mentionner la version d'environnement minimale si connue.
5. **Complexité** : évaluer selon le scope et les dépendances — Faible = une seule responsabilité, Moyen = logique conditionnelle, Élevé = multiples dépendances ou cas limites.
6. **Priorités** : CRITIQUE = bloquant pour le lancement, HAUTE = important pour la qualité, MOYENNE = nice-to-have ou documentation.
7. **Numérotation** : toujours numéroter les US en séquence US-001, US-002, etc. Ne pas sauter de numéro.
8. **Dépendances** : remplir la colonne Dépendances de la Matrice de Traçabilité en analysant les liens logiques entre US (ex: afficher un prénom dépend de l'avoir capturé).

---

## Structure du fichier Specs.md à générer

````markdown
# Spécifications Fonctionnelles - {Titre du Projet}

## User Stories et Critères d'Acceptation

---

### US-001 : {Titre de la fonctionnalité principale}

**En tant que** {persona déduit ou fourni}
**Je souhaite** {action souhaitée — formulée du point de vue utilisateur}
**Afin de** {bénéfice attendu — valeur métier ou technique}

#### Critères d'Acceptation
- [ ] {critère mesurable et testable 1 — avec commande concrète si applicable}
- [ ] {critère mesurable et testable 2}
- [ ] {critère mesurable et testable 3}

#### Détails Techniques
- {contrainte technique ou de performance issue du Brief}
- {version d'environnement minimale si connue}
- {outil ou module recommandé si mentionné dans le Brief}

---

### US-002 : {Titre}

**En tant que** {persona}
**Je souhaite** {action}
**Afin de** {bénéfice}

#### Critères d'Acceptation
- [ ] {critère 1}
- [ ] {critère 2}

#### Détails Techniques
- {détail technique}

---

[Continuer pour chaque fonctionnalité majeure identifiée dans le Brief — au moins une US par objectif]

---

## Matrice de Traçabilité

| User Story | Critère résumé | Complexité | Dépendances |
|---|---|---|---|
| US-001 | {résumé en 3-5 mots} | Faible/Moyen/Élevé | Aucune |
| US-002 | {résumé en 3-5 mots} | Faible/Moyen/Élevé | US-001 |

---

## Priorités

| Priorité | User Stories |
|---|---|
| CRITIQUE | {US bloquantes pour le lancement} |
| HAUTE | {US importantes pour la qualité} |
| MOYENNE | {US souhaitables — documentation, accessibilité} |

---

## Version
**Version** : 1.0
**Date** : {date du jour}
**Statut** : En cours de rédaction
````

---

## Exemple concret (projet Hello World - Script Python Echo Prénom)

Basé sur `Training lab/Hello World/Brief.md` → produit `Training lab/Hello World/Specs.md`

**Brief source :** Script Python CLI qui accepte un prénom en argument et affiche `Bonjour <prénom>!`. Contraintes : < 100ms, < 10MB, Python 3.7+, modules standard uniquement.

**Déductions appliquées :**
- Personas : utilisateur final (US-001 à US-006), développeur (US-004, US-007)
- Contraintes extraites : `< 100ms` → ajouté dans US-002, `< 10MB` → ajouté dans US-004
- Livrable inféré : `script.py` (depuis mention `python script.py` dans le Brief)

**Structure produite :**

| US | Titre | Priorité | Dépendances |
|---|---|---|---|
| US-001 | Accepter un prénom en argument CLI | CRITIQUE | Aucune |
| US-002 | Afficher le prénom fourni | CRITIQUE | US-001 |
| US-003 | Gérer l'absence d'argument | HAUTE | US-001 |
| US-004 | Gérer les arguments vides ou invalides | HAUTE | US-001 |
| US-005 | Gérer les caractères spéciaux et prénoms internationaux | MOYENNE | US-001 |
| US-006 | Afficher un message d'aide | MOYENNE | Aucune |
| US-007 | Code commenté et documenté | MOYENNE | Aucune |
