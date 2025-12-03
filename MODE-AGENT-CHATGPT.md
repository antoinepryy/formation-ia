# Le Mode Agent de ChatGPT

**Guide complet pour maîtriser les agents autonomes**
**Durée de lecture** : 30 minutes
**Niveau** : Intermédiaire à avancé

---

## Sommaire

1. [Qu'est-ce que le mode agent ?](#quest-ce-que-le-mode-agent)
2. [Comment activer et utiliser le mode agent](#comment-activer-et-utiliser-le-mode-agent)
3. [Les capacités du mode agent](#les-capacités-du-mode-agent)
4. [Cas d'usage concrets](#cas-dusage-concrets)
5. [Bonnes pratiques](#bonnes-pratiques)
6. [Limites et précautions](#limites-et-précautions)
7. [Exercices pratiques](#exercices-pratiques)

---

# Qu'est-ce que le mode agent ?

## Définition

Le **mode agent** (ou "Agentic AI") représente une évolution majeure de ChatGPT. Contrairement au mode conversationnel classique où l'IA répond à une question unique, le mode agent permet à ChatGPT de :

- **Planifier** une séquence d'actions pour atteindre un objectif
- **Exécuter** ces actions de manière autonome
- **Itérer** et s'adapter en fonction des résultats obtenus
- **Utiliser des outils** (navigation web, exécution de code, analyse de fichiers)

> 💡 **En résumé** : Le mode agent transforme ChatGPT d'un assistant réactif en un assistant proactif capable d'accomplir des tâches complexes de bout en bout.

---

## Mode conversationnel vs Mode agent

| Aspect | Mode conversationnel | Mode agent |
|--------|---------------------|------------|
| **Interaction** | Question → Réponse | Objectif → Séquence d'actions |
| **Autonomie** | Faible (attend vos instructions) | Élevée (planifie et exécute) |
| **Outils** | Limités | Navigation, code, fichiers, recherche |
| **Durée** | Réponse instantanée | Peut prendre plusieurs minutes |
| **Complexité** | Tâches simples | Tâches multi-étapes |

---

## Comment ça fonctionne ?

Le mode agent utilise une boucle **Perception → Planification → Action → Évaluation** :

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   1. PERCEPTION                                             │
│      └─ Comprendre l'objectif et le contexte                │
│                        ↓                                    │
│   2. PLANIFICATION                                          │
│      └─ Décomposer en sous-tâches                          │
│                        ↓                                    │
│   3. ACTION                                                 │
│      └─ Exécuter chaque sous-tâche avec les outils         │
│                        ↓                                    │
│   4. ÉVALUATION                                             │
│      └─ Vérifier le résultat, ajuster si nécessaire        │
│                        ↓                                    │
│   5. ITÉRATION (si besoin)                                  │
│      └─ Retour à l'étape 2 ou 3                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

# Comment activer et utiliser le mode agent

## Prérequis

- **Compte ChatGPT Plus, Pro ou Team** (le mode agent n'est pas disponible sur la version gratuite pour toutes les fonctionnalités)
- **Navigateur web moderne** ou application ChatGPT
- **Connexion internet stable** (pour les tâches de recherche)

---

## Activer le mode agent

### Méthode 1 : Activation automatique

ChatGPT active automatiquement le mode agent quand vous formulez une demande complexe nécessitant plusieurs étapes. Il suffit de poser une question qui implique :
- Une recherche d'information
- Une analyse de données
- Une création de contenu élaborée
- Une tâche multi-étapes

### Méthode 2 : Demande explicite

Vous pouvez explicitement demander à ChatGPT d'agir en mode agent :

```
"Agis comme un agent autonome pour accomplir cette tâche :
[Description de votre objectif]

Planifie les étapes nécessaires, exécute-les une par une,
et présente-moi le résultat final."
```

### Méthode 3 : Via les GPTs spécialisés

Certains GPTs personnalisés sont conçus pour fonctionner en mode agent avec des capacités spécifiques (recherche, analyse, création).

---

## Les indicateurs du mode agent

Quand ChatGPT est en mode agent, vous verrez :

- 🔍 **"Recherche en cours..."** - Navigation web active
- 💻 **"Analyse du code..."** - Exécution de Python
- 📊 **"Traitement des données..."** - Analyse de fichiers
- ⏳ **Indicateur de progression** - Pour les tâches longues
- 📋 **Liste des étapes** - Plan d'action affiché

---

# Les capacités du mode agent

## 1. Navigation web et recherche

Le mode agent peut :
- Rechercher des informations actualisées sur le web
- Visiter des pages spécifiques
- Extraire et synthétiser des données de plusieurs sources
- Comparer des informations de différents sites

**Exemple de prompt** :
```
"Recherche les 5 dernières actualités sur l'intelligence artificielle
en France cette semaine. Pour chaque actualité, donne-moi :
- Le titre
- La source
- Un résumé en 2 phrases
- L'impact potentiel pour les entreprises"
```

---

## 2. Exécution de code (Code Interpreter)

Le mode agent peut écrire et exécuter du code Python pour :
- Analyser des données (CSV, Excel, JSON)
- Créer des visualisations (graphiques, diagrammes)
- Effectuer des calculs complexes
- Manipuler des fichiers

**Exemple de prompt** :
```
"Voici un fichier CSV de mes ventes 2024.
Analyse les données et :
1. Calcule le chiffre d'affaires mensuel
2. Identifie les 3 produits les plus vendus
3. Crée un graphique d'évolution des ventes
4. Prédis les ventes du mois prochain"
```

---

## 3. Analyse de documents

Le mode agent peut traiter :
- **PDF** : Extraction de texte, résumé, analyse
- **Images** : Description, OCR, analyse visuelle
- **Fichiers Office** : Word, Excel, PowerPoint
- **Code source** : Revue, debugging, documentation

**Exemple de prompt** :
```
"Analyse ce contrat PDF et :
1. Identifie les parties prenantes
2. Liste les obligations de chaque partie
3. Repère les clauses potentiellement problématiques
4. Suggère des points de négociation"
```

---

## 4. Génération de contenu multimédia

Avec DALL-E intégré, le mode agent peut :
- Créer des images à partir de descriptions
- Itérer sur des visuels pour les améliorer
- Adapter des images à différents formats

**Exemple de prompt** :
```
"Crée une série de 3 visuels pour ma campagne LinkedIn sur
le développement durable. Chaque visuel doit :
- Avoir un style corporate moderne
- Inclure un message inspirant
- Utiliser des tons verts et bleus
- Être optimisé pour le format LinkedIn (1200x627px)"
```

---

## 5. Tâches de recherche approfondie

Le mode agent excelle dans les recherches complexes :

**Exemple de prompt** :
```
"Effectue une analyse concurrentielle complète pour une
startup de livraison de repas bio à Paris :

1. Identifie les 5 principaux concurrents
2. Analyse leurs forces et faiblesses
3. Compare leurs modèles de prix
4. Évalue leur présence sur les réseaux sociaux
5. Identifie les opportunités de différenciation

Présente le tout dans un rapport structuré avec tableaux comparatifs."
```

---

# Cas d'usage concrets

## Cas 1 : Veille concurrentielle automatisée

**Objectif** : Surveiller l'actualité de vos concurrents

**Prompt agent** :
```
"Tu es mon agent de veille concurrentielle.

MISSION : Analyser l'actualité récente de [CONCURRENT 1], [CONCURRENT 2]
et [CONCURRENT 3] dans le secteur [SECTEUR].

POUR CHAQUE CONCURRENT :
1. Recherche les dernières actualités (1 mois)
2. Identifie les nouveaux produits/services lancés
3. Analyse leur communication sur LinkedIn
4. Repère les signaux faibles (recrutements, partenariats)

LIVRABLE :
- Tableau comparatif
- 3 insights stratégiques
- Recommandations d'actions pour mon entreprise"
```

---

## Cas 2 : Création de contenu complet

**Objectif** : Produire une campagne marketing complète

**Prompt agent** :
```
"Tu es mon agent de création de contenu.

MISSION : Créer une campagne de communication pour le lancement
de [PRODUIT] ciblant [AUDIENCE].

ÉTAPES À SUIVRE :
1. Recherche les tendances actuelles du marché
2. Analyse 3 campagnes réussies de concurrents
3. Propose 5 angles créatifs différents
4. Développe l'angle choisi en :
   - 1 communiqué de presse (300 mots)
   - 3 posts LinkedIn avec visuels
   - 1 script vidéo de 60 secondes
   - 5 idées de stories Instagram

CONTRAINTES :
- Ton : [professionnel/décalé/inspirant]
- Budget : [limité/moyen/élevé]
- Délai de lancement : [date]"
```

---

## Cas 3 : Analyse de données business

**Objectif** : Transformer des données brutes en insights actionnables

**Prompt agent** :
```
"Tu es mon agent d'analyse de données.

MISSION : Analyser le fichier de ventes joint et produire
un rapport exécutif.

ANALYSES REQUISES :
1. Tendances de ventes (mensuel, trimestriel)
2. Segmentation clients (RFM si possible)
3. Produits stars vs produits à problème
4. Saisonnalité détectée
5. Prévisions pour le prochain trimestre

FORMAT DU RAPPORT :
- Executive summary (5 lignes)
- Graphiques clés
- Tableau de KPIs
- 5 recommandations prioritaires

Génère également le code Python utilisé pour que je puisse
le réutiliser."
```

---

## Cas 4 : Préparation de réunion

**Objectif** : Préparer une réunion client importante

**Prompt agent** :
```
"Tu es mon agent de préparation de réunion.

CONTEXTE : J'ai une réunion avec [CLIENT] demain pour
présenter [SUJET].

MISSION :
1. Recherche des informations sur l'entreprise cliente
   - Actualités récentes
   - Résultats financiers
   - Dirigeants clés
2. Identifie leurs enjeux probables
3. Prépare :
   - 5 questions pertinentes à poser
   - 3 objections possibles et réponses
   - 2 success stories à mentionner
4. Crée un one-pager de présentation

LIVRABLE : Document de briefing complet"
```

---

## Cas 5 : Automatisation de tâches récurrentes

**Objectif** : Créer un workflow reproductible

**Prompt agent** :
```
"Tu es mon agent d'automatisation.

TÂCHE RÉCURRENTE : Chaque lundi, je dois créer un rapport
de performance de mes réseaux sociaux.

CRÉE UN TEMPLATE RÉUTILISABLE :
1. Liste des métriques à collecter
2. Format du rapport standardisé
3. Prompt optimisé pour les prochaines semaines
4. Checklist de vérification

Le template doit être autonome : je veux pouvoir copier-coller
le prompt chaque semaine avec mes nouvelles données."
```

---

# Bonnes pratiques

## 1. Formuler un objectif clair

❌ **Mauvais** : "Aide-moi avec mon marketing"

✅ **Bon** :
```
"Objectif : Augmenter ma visibilité LinkedIn de 50% en 3 mois.
Contexte : Je suis consultant en transformation digitale,
           500 abonnés actuellement, je publie 1x/semaine.
Demande : Crée une stratégie complète avec calendrier éditorial."
```

---

## 2. Définir les étapes attendues

Guidez l'agent avec une structure :

```
"Pour accomplir cette mission, procède ainsi :

ÉTAPE 1 : [Recherche/Analyse initiale]
ÉTAPE 2 : [Traitement/Transformation]
ÉTAPE 3 : [Création/Synthèse]
ÉTAPE 4 : [Vérification/Validation]

À chaque étape, montre-moi ta progression."
```

---

## 3. Spécifier le format de sortie

```
"LIVRABLE ATTENDU :
- Format : [Rapport PDF / Tableau / Liste / Code]
- Longueur : [X pages / X mots / X items]
- Structure : [Sections obligatoires]
- Ton : [Professionnel / Décontracté / Technique]"
```

---

## 4. Demander de la transparence

```
"Pendant l'exécution :
- Explique chaque étape avant de l'effectuer
- Indique les sources utilisées
- Signale les incertitudes ou limites
- Propose des alternatives si blocage"
```

---

## 5. Prévoir l'itération

```
"Après la première version :
- Présente un résumé des choix effectués
- Liste les points à valider avec moi
- Propose 2-3 améliorations possibles
- Attends mon feedback avant de finaliser"
```

---

# Limites et précautions

## Ce que le mode agent NE PEUT PAS faire

| Limitation | Explication |
|------------|-------------|
| **Actions dans le monde réel** | Ne peut pas envoyer d'emails, publier sur les réseaux, effectuer des achats |
| **Accès à vos comptes** | Ne peut pas se connecter à vos outils (CRM, réseaux sociaux, etc.) |
| **Données en temps réel** | Les informations web peuvent avoir quelques heures/jours de retard |
| **Calculs financiers critiques** | Toujours vérifier les chiffres importants |
| **Décisions définitives** | L'humain doit valider les choix importants |

---

## Précautions d'usage

### Sécurité des données

⚠️ **Ne partagez JAMAIS** :
- Mots de passe ou identifiants
- Données personnelles de clients
- Informations financières sensibles
- Documents confidentiels stratégiques

### Vérification des résultats

✅ **Toujours vérifier** :
- Les chiffres et statistiques cités
- Les sources mentionnées
- Les dates et informations factuelles
- Les recommandations stratégiques

### Supervision humaine

> 🎯 **Règle d'or** : Le mode agent est un assistant puissant, pas un décideur.
> Vous restez responsable de la validation et de l'exécution finale.

---

## Gestion des erreurs

Quand l'agent se trompe ou bloque :

```
"Je remarque que [PROBLÈME].
Peux-tu :
1. Expliquer ce qui s'est passé
2. Proposer une approche alternative
3. Reprendre à partir de l'étape [X]"
```

---

# Exercices pratiques

## Exercice 1 : Recherche et synthèse (15 min)

**Objectif** : Maîtriser la recherche web en mode agent

**Instructions** :
```
"Agis comme un agent de recherche.

MISSION : Trouve les 3 tendances majeures de l'IA générative
pour les entreprises en 2024.

PROCESSUS :
1. Recherche sur au moins 5 sources différentes
2. Croise les informations
3. Identifie les points de convergence

LIVRABLE :
- 3 tendances avec description (50 mots chacune)
- Pour chaque tendance : 1 exemple concret d'entreprise
- Sources utilisées"
```

**Critères de réussite** :
- [ ] L'agent a effectué des recherches visibles
- [ ] Les sources sont citées
- [ ] Les tendances sont pertinentes et actuelles

---

## Exercice 2 : Analyse de données (20 min)

**Objectif** : Utiliser le Code Interpreter en mode agent

**Instructions** :
1. Préparez un fichier CSV simple (ou utilisez un exemple fourni)
2. Uploadez-le dans ChatGPT
3. Utilisez ce prompt :

```
"Agis comme un agent data analyst.

MISSION : Analyse complète de ce fichier de données.

PROCESSUS :
1. Explore et décris la structure des données
2. Nettoie les données si nécessaire
3. Calcule les statistiques clés
4. Crée 2 visualisations pertinentes
5. Identifie 3 insights business

LIVRABLE :
- Rapport d'analyse structuré
- Graphiques exportables
- Code Python commenté"
```

**Critères de réussite** :
- [ ] Les données sont correctement interprétées
- [ ] Les visualisations sont claires
- [ ] Le code est réutilisable

---

## Exercice 3 : Création de contenu multi-format (25 min)

**Objectif** : Produire du contenu cohérent sur plusieurs formats

**Instructions** :
```
"Agis comme un agent de content marketing.

MISSION : Créer une mini-campagne sur le thème [VOTRE THÈME].

PROCESSUS :
1. Recherche les angles les plus engageants sur ce thème
2. Définis un message central
3. Décline en 4 formats :
   - Post LinkedIn (texte + suggestion visuelle)
   - Tweet/Thread X (max 280 caractères ou thread)
   - Paragraphe newsletter (100 mots)
   - Idée de vidéo courte (script 30 sec)

CONTRAINTES :
- Cohérence du message sur tous les formats
- Adaptation au ton de chaque plateforme
- CTA adapté à chaque format"
```

**Critères de réussite** :
- [ ] Message cohérent sur tous les formats
- [ ] Adaptation réelle à chaque plateforme
- [ ] Contenu actionnable

---

## Exercice 4 : Agent personnel (30 min)

**Objectif** : Créer votre propre agent spécialisé

**Instructions** :
1. Identifiez une tâche récurrente dans votre travail
2. Créez un prompt "agent" complet :

```
"Tu es mon agent [SPÉCIALITÉ].

CONTEXTE :
[Décrivez votre situation, votre entreprise, vos contraintes]

MISSION RÉCURRENTE :
[Décrivez la tâche que vous voulez automatiser]

PROCESSUS STANDARD :
1. [Étape 1]
2. [Étape 2]
3. [Étape 3]
...

FORMAT DE SORTIE :
[Décrivez précisément le livrable attendu]

RÈGLES :
- [Ce que l'agent doit toujours faire]
- [Ce que l'agent ne doit jamais faire]

PREMIÈRE MISSION : [Lancez une première tâche concrète]"
```

**Critères de réussite** :
- [ ] Le prompt est réutilisable
- [ ] L'agent comprend sa mission
- [ ] Le résultat est exploitable professionnellement

---

# Récapitulatif

## Les 5 clés du mode agent

1. **Objectif clair** : Définissez précisément ce que vous voulez obtenir
2. **Étapes structurées** : Guidez l'agent avec un processus logique
3. **Format de sortie** : Spécifiez exactement le livrable attendu
4. **Transparence** : Demandez à l'agent d'expliquer ses actions
5. **Supervision** : Validez toujours les résultats critiques

---

## Template universel de prompt agent

```
Tu es mon agent [RÔLE/SPÉCIALITÉ].

CONTEXTE :
[Qui vous êtes, votre situation, vos contraintes]

OBJECTIF :
[Ce que vous voulez accomplir - soyez spécifique]

PROCESSUS :
1. [Première étape avec instruction claire]
2. [Deuxième étape]
3. [Troisième étape]
4. [Vérification/Validation]

LIVRABLE :
- Format : [type de document]
- Longueur : [contrainte de taille]
- Contenu obligatoire : [éléments requis]

RÈGLES :
✅ TOUJOURS : [ce que l'agent doit faire]
❌ JAMAIS : [ce que l'agent doit éviter]

COMMENCER PAR :
[Première action à effectuer maintenant]
```

---

## Checklist avant de lancer un agent

- [ ] Mon objectif est-il clairement défini ?
- [ ] Les étapes sont-elles logiques et séquentielles ?
- [ ] Le format de sortie est-il spécifié ?
- [ ] Ai-je prévu des points de validation ?
- [ ] Les données sensibles sont-elles exclues ?
- [ ] Suis-je prêt à vérifier les résultats ?

---

*Guide créé pour la formation IA - Mode Agent*
*Version 1.0 | 2024*
