# Module 2 : IA Générative & Prompt Engineering
## Durée : 3 heures

---

## 🎯 Objectifs du module

À la fin de ce module, vous serez capable de :
- Comprendre le fonctionnement des modèles de langage génératifs
- Maîtriser les techniques de prompt engineering
- Optimiser vos interactions avec les IA conversationnelles
- Créer des prompts réutilisables pour différents cas d'usage
- Implémenter des stratégies avancées de génération de contenu

---

## 📚 Leçon 1 : Comprendre l'IA Générative

### 1.1 Architecture des modèles de langage

#### 🧠 **Comment fonctionne un LLM (Large Language Model) ?**

Les modèles de langage sont entraînés sur d'immenses corpus de texte pour prédire le mot suivant dans une séquence. Cette simplicité apparente cache une complexité remarquable.

**Processus de fonctionnement :**
1. **Tokenisation** : Découpage du texte en unités (tokens)
2. **Encodage** : Transformation en vecteurs numériques
3. **Attention** : Analyse des relations entre les mots
4. **Prédiction** : Génération probabiliste du texte suivant
5. **Décodage** : Conversion en texte lisible

**Exemple concret :**
```
Entrée : "Le ciel est"
Tokenisation : ["Le", "ciel", "est"]
Prédictions possibles :
- "bleu" (30% de probabilité)
- "nuageux" (25% de probabilité)
- "magnifique" (20% de probabilité)
```

### 1.2 Capacités et limitations

#### ✅ **Ce que l'IA générative fait bien**
- Comprendre le contexte et les nuances
- Générer du texte cohérent et fluide
- Traduire entre langues
- Résumer et synthétiser l'information
- Adapter le ton et le style
- Créer du contenu original

#### ❌ **Limitations importantes**
- **Hallucinations** : Invention d'informations fausses mais plausibles
- **Biais** : Reproduction des biais présents dans les données d'entraînement
- **Actualité** : Connaissances limitées à la date de formation
- **Raisonnement** : Difficultés avec la logique complexe et les mathématiques
- **Cohérence** : Peut se contredire sur de longs textes
- **Confidentialité** : Ne pas partager d'informations sensibles

### 1.3 Paramètres clés des modèles

| Paramètre | Description | Impact | Valeur recommandée |
|-----------|-------------|--------|-------------------|
| **Temperature** | Contrôle la créativité | 0 = Déterministe, 1 = Créatif | 0.7 pour équilibre |
| **Top-p** | Limite les choix de mots | 0.1 = Restrictif, 1 = Ouvert | 0.9 pour variété |
| **Max tokens** | Longueur de la réponse | Court vs Long | Selon besoin |
| **Frequency penalty** | Évite les répétitions | 0 = Répétitions OK | 0.3-0.5 |
| **Presence penalty** | Favorise nouveaux sujets | 0 = Même thème OK | 0.3-0.5 |

---

## 📚 Leçon 2 : Les Fondamentaux du Prompt Engineering

### 2.1 Anatomie d'un prompt efficace

Un prompt bien structuré suit généralement ce schéma :

```
[CONTEXTE] + [RÔLE] + [TÂCHE] + [FORMAT] + [CONTRAINTES] = RÉSULTAT OPTIMAL
```

#### 📝 **Exemple décomposé :**

```markdown
[CONTEXTE] Je dirige une startup de 10 personnes dans la tech.

[RÔLE] Agis comme un expert en recrutement spécialisé dans les startups tech.

[TÂCHE] Rédige une offre d'emploi pour un développeur full-stack junior.

[FORMAT] Structure l'offre avec : titre, description entreprise, missions, profil recherché, avantages, processus de recrutement.

[CONTRAINTES] 
- Ton dynamique et inclusif
- Maximum 500 mots
- Mets l'accent sur l'apprentissage et l'évolution
- Évite le jargon technique excessif
```

### 2.2 Les 7 techniques essentielles

#### 1️⃣ **Technique du Rôle (Role Prompting)**
Assigner une personnalité ou expertise spécifique à l'IA.

```
❌ Mauvais : "Écris un article sur le marketing"
✅ Bon : "Tu es un expert en marketing digital avec 15 ans d'expérience. Écris un article sur les tendances 2024 du marketing d'influence."
```

#### 2️⃣ **Technique des Exemples (Few-Shot Learning)**
Fournir des exemples du résultat attendu.

```
Transforme ces phrases en ton professionnel :

Exemple 1 :
Entrée : "C'est nul, ça marche pas"
Sortie : "Nous rencontrons des difficultés techniques"

Exemple 2 :
Entrée : "J'ai pas le temps"
Sortie : "Mon planning ne me permet pas actuellement"

Maintenant transforme : "C'est trop cher pour ce que c'est"
```

#### 3️⃣ **Technique de la Chaîne de Pensée (Chain-of-Thought)**
Demander à l'IA d'expliquer son raisonnement étape par étape.

```
Résous ce problème étape par étape :
"Une entreprise a 120 employés. 40% travaillent en remote, 25% en hybride. 
Combien travaillent uniquement au bureau ?"

Montre ton raisonnement :
1. Calcule le nombre en remote
2. Calcule le nombre en hybride
3. Déduis ceux au bureau
```

#### 4️⃣ **Technique du Cadrage (Framing)**
Définir précisément le contexte et les limites.

```
Contexte : Email professionnel B2B
Destinataire : Directeur financier d'une PME
Objectif : Proposer une démonstration de notre logiciel comptable
Ton : Formel mais accessible
Longueur : 150 mots maximum
Interdits : Prix, réductions, termes techniques complexes

Rédige l'email.
```

#### 5️⃣ **Technique de l'Itération (Iterative Refinement)**
Affiner progressivement le résultat.

```
Première demande : "Crée un slogan pour une marque de café bio"
Réponse : "Naturellement bon"
Deuxième demande : "Plus original et qui évoque l'énergie du matin"
Réponse : "Réveillez vos sens, naturellement"
Troisième demande : "Ajoute une notion d'éthique et de commerce équitable"
Réponse finale : "L'énergie pure d'un café qui change le monde"
```

#### 6️⃣ **Technique des Contraintes Négatives**
Préciser ce qu'il ne faut PAS faire.

```
Écris une description de produit pour des écouteurs bluetooth.
NE PAS :
- Utiliser de superlatifs (meilleur, parfait, exceptionnel)
- Mentionner la concurrence
- Faire plus de 100 mots
- Utiliser du jargon audiophile
```

#### 7️⃣ **Technique du Format Structuré**
Demander une sortie dans un format spécifique.

```
Analyse ce texte et réponds au format suivant :

## Résumé (2 phrases)
[Ton résumé ici]

## Points clés (bullets)
- Point 1
- Point 2
- Point 3

## Sentiment général
[Positif/Neutre/Négatif]

## Recommandations
1. [Recommandation 1]
2. [Recommandation 2]
```

---

## 📚 Leçon 3 : Prompts Avancés et Cas d'Usage

### 3.1 Templates de prompts par métier

#### 📊 **Marketing & Communication**

**Template : Création de persona marketing**
```
Tu es un expert en marketing avec une spécialisation en psychologie du consommateur.

Crée un persona détaillé pour [PRODUIT/SERVICE] :

DÉMOGRAPHIE
- Âge :
- Genre :
- Localisation :
- Revenus :
- Éducation :

PSYCHOGRAPHIE
- Valeurs :
- Motivations :
- Frustrations :
- Objectifs :

COMPORTEMENT D'ACHAT
- Canaux préférés :
- Facteurs de décision :
- Objections courantes :

JOUR TYPE
Décris une journée type en 5 moments clés.

MESSAGE CLÉ
Quelle phrase résumerait parfaitement la proposition de valeur pour ce persona ?
```

**Template : Génération de contenu social media**
```
Contexte : [MARQUE/PRODUIT]
Plateforme : [LinkedIn/Instagram/Twitter]
Objectif : [Engagement/Conversion/Notoriété]

Crée 5 posts avec :
1. Hook accrocheur (première ligne)
2. Corps du message (valeur ajoutée)
3. CTA clair
4. 3-5 hashtags pertinents
5. Suggestion visuelle

Ton : [Professionnel/Décontracté/Inspirant]
Contraintes : [Caractères max, mentions, etc.]
```

#### 💼 **Vente & Prospection**

**Template : Email de prospection personnalisé**
```
Informations prospect :
- Entreprise : [NOM]
- Secteur : [SECTEUR]
- Taille : [EFFECTIF]
- Actualité récente : [NEWS]

Notre solution : [DESCRIPTION COURTE]

Rédige un email de prospection qui :
1. Montre qu'on connaît leur actualité
2. Identifie un pain point probable
3. Propose notre solution sans survendre
4. Inclut une question ouverte
5. Propose un call de 15 minutes

Maximum 150 mots, ton consultif et non-commercial.
```

#### 📝 **Rédaction & Content**

**Template : Article de blog optimisé SEO**
```
Mot-clé principal : [MOT-CLÉ]
Mots-clés secondaires : [LISTE]
Intention de recherche : [Informationnelle/Transactionnelle/Navigation]
Cible : [AUDIENCE]

Structure l'article ainsi :
1. Titre H1 accrocheur avec mot-clé
2. Introduction (problème + promesse)
3. 4-5 sections H2 avec mots-clés
4. Sous-sections H3 si nécessaire
5. Conclusion avec CTA
6. Meta description (155 caractères)

Longueur : [NOMBRE] mots
Ton : [TON]
Include : Exemples concrets, statistiques, citations
```

### 3.2 Techniques de prompt avancées

#### 🎯 **Prompt Chaining (Enchaînement)**
Utiliser plusieurs prompts successifs pour des tâches complexes.

```
PROMPT 1 : "Liste les 5 principaux défis du e-commerce en 2024"
[Récupérer réponse]

PROMPT 2 : "Pour le défi n°1 [INSÉRER], propose 3 solutions innovantes"
[Récupérer réponse]

PROMPT 3 : "Développe la solution n°2 en plan d'action sur 90 jours"
```

#### 🔄 **Self-Consistency (Auto-cohérence)**
Demander plusieurs versions et synthétiser.

```
Génère 3 approches différentes pour [PROBLÈME].

Version 1 : Approche conservatrice
Version 2 : Approche innovante
Version 3 : Approche disruptive

Puis synthétise les meilleures idées de chaque approche.
```

#### 🎭 **Perspective Prompting**
Explorer différents points de vue.

```
Analyse cette décision stratégique depuis 4 perspectives :

1. PDG : Vision long terme et rentabilité
2. Employé : Impact sur le quotidien et la culture
3. Client : Valeur ajoutée et expérience
4. Investisseur : ROI et risques

Synthèse : Points de convergence et divergence
```

---

## 📚 Leçon 4 : Optimisation et Debugging des Prompts

### 4.1 Diagnostic des problèmes courants

| Problème | Symptômes | Solutions |
|----------|-----------|-----------|
| **Réponses trop génériques** | Manque de spécificité, banalités | Ajouter contexte, exemples, contraintes |
| **Hallucinations** | Informations inventées | Demander les sources, vérifier les faits |
| **Incohérence** | Contradictions dans la réponse | Diviser en prompts plus courts |
| **Format incorrect** | Structure non respectée | Fournir un template clair |
| **Ton inapproprié** | Style ne correspond pas | Préciser le ton avec exemples |
| **Longueur inadéquate** | Trop court ou trop long | Spécifier nombre de mots/sections |

### 4.2 Méthodologie de test A/B

**Protocole de test :**
1. Définir la métrique de succès
2. Créer 2-3 variantes du prompt
3. Tester sur 5-10 itérations
4. Mesurer et comparer
5. Affiner le gagnant

**Exemple de test :**
```
Version A : "Écris un email professionnel"
Score : 6/10

Version B : "Tu es assistant de direction. Écris un email professionnel"
Score : 7/10

Version C : "Tu es assistant de direction senior dans une multinationale. 
Écris un email professionnel formel mais chaleureux"
Score : 9/10

→ Version C retenue et optimisée
```

### 4.3 Check-list d'optimisation

Avant de valider un prompt, vérifiez :

- [ ] Le contexte est-il suffisant ?
- [ ] Le rôle est-il défini ?
- [ ] La tâche est-elle claire ?
- [ ] Le format de sortie est-il spécifié ?
- [ ] Les contraintes sont-elles explicites ?
- [ ] Y a-t-il des exemples si nécessaire ?
- [ ] Le ton est-il précisé ?
- [ ] La longueur est-elle indiquée ?
- [ ] Les éléments à éviter sont-ils listés ?
- [ ] Le prompt est-il testé sur 3+ itérations ?

---

## 🏃 Exercices pratiques

### Exercice 1 : Construction de prompt étape par étape
**Durée : 20 minutes**

Transformez cette demande basique en prompt optimisé :
"Aide-moi à vendre mon produit"

**Étapes :**
1. Ajoutez le contexte (quel produit, quel marché)
2. Définissez le rôle (expert en quoi ?)
3. Précisez la tâche (quel livrable exact ?)
4. Structurez le format attendu
5. Ajoutez les contraintes pertinentes

**Résultat attendu :** Un prompt de 100-150 mots parfaitement structuré.

### Exercice 2 : Débogage de prompts défaillants
**Durée : 25 minutes**

Voici 3 prompts problématiques. Identifiez les problèmes et corrigez-les :

**Prompt 1 :**
"Fais-moi un truc sur le marketing"

**Prompt 2 :**
"Tu es le meilleur expert au monde en tout. Révolutionne complètement ma stratégie business en créant quelque chose que personne n'a jamais vu. Sois ultra créatif et innovant. Change tout !"

**Prompt 3 :**
"Écris article blog titre introduction développement 3 parties conclusion CTA mots clés SEO méta description images alt text 2000 mots marketing digital tendances 2024 B2B SaaS startup"

### Exercice 3 : Création de votre bibliothèque de prompts
**Durée : 30 minutes**

Créez 5 prompts réutilisables pour votre activité professionnelle :

1. **Prompt de synthèse** (pour résumer des documents)
2. **Prompt de création** (pour générer du contenu)
3. **Prompt d'analyse** (pour évaluer des données/situations)
4. **Prompt de résolution** (pour solutionner des problèmes)
5. **Prompt de planification** (pour organiser des projets)

Format de documentation :
```
NOM DU PROMPT : [Titre descriptif]
CAS D'USAGE : [Quand l'utiliser]
PROMPT : [Le prompt complet avec variables]
EXEMPLE D'OUTPUT : [Résultat type attendu]
NOTES : [Ajustements possibles]
```

---

## 💡 Points clés à retenir

✅ **Structure = Succès** : Un prompt bien structuré donne de meilleurs résultats

✅ **Itération = Amélioration** : Raffinez vos prompts progressivement

✅ **Contexte = Pertinence** : Plus de contexte = réponses plus pertinentes

✅ **Exemples = Clarté** : Les exemples valent mieux que les longues explications

✅ **Test = Validation** : Testez toujours vos prompts avant utilisation production

---

## 📊 Métriques de qualité des prompts

Évaluez vos prompts selon ces critères :

| Critère | Score (1-5) | Indicateurs |
|---------|-------------|------------|
| **Clarté** | ⭐⭐⭐⭐⭐ | Compréhension immédiate de la demande |
| **Complétude** | ⭐⭐⭐⭐⭐ | Tous les éléments nécessaires présents |
| **Spécificité** | ⭐⭐⭐⭐⭐ | Niveau de détail et précision |
| **Réutilisabilité** | ⭐⭐⭐⭐⭐ | Facilité d'adaptation à d'autres cas |
| **Efficacité** | ⭐⭐⭐⭐⭐ | Qualité du résultat vs effort |

**Score total : __/25**

Un bon prompt doit scorer minimum 20/25.

---

## 🔗 Ressources complémentaires

### Outils de test de prompts
- **PromptPerfect** : Optimisation automatique
- **Promptbase** : Marketplace de prompts
- **ChatGPT Prompt Engineering Guide** : Documentation OpenAI

### Communautés spécialisées
- r/PromptEngineering
- Discord : Prompt Engineering Community
- LinkedIn : AI Prompt Masters

### Lectures recommandées
- "The Art of Prompt Engineering" - Dair.ai
- "Prompt Engineering Guide" - CUNY
- "Advanced Prompt Engineering" - Anthropic

---

## ❓ Quiz d'auto-évaluation

1. **Quel élément N'EST PAS essentiel dans un prompt bien structuré ?**
   - a) Le contexte
   - b) Le prix du service
   - c) Le format de sortie
   - d) Les contraintes

2. **La "température" d'un modèle contrôle :**
   - a) La vitesse de réponse
   - b) La créativité/variabilité
   - c) La longueur du texte
   - d) La précision factuelle

3. **Quelle technique consiste à fournir des exemples dans le prompt ?**
   - a) Chain-of-thought
   - b) Role prompting
   - c) Few-shot learning
   - d) Framing

4. **Pour éviter les hallucinations, il est préférable de :**
   - a) Augmenter la température
   - b) Demander des sources
   - c) Allonger le prompt
   - d) Utiliser plus d'emojis

5. **Le "prompt chaining" consiste à :**
   - a) Écrire des prompts très longs
   - b) Enchaîner plusieurs prompts successifs
   - c) Copier des prompts existants
   - d) Générer des prompts automatiquement

**Réponses : 1-b, 2-b, 3-c, 4-b, 5-b**

---

## 🚀 Prochaine étape

Dans le Module 3, nous explorerons l'univers créatif de l'IA avec Midjourney, Adobe Firefly et autres outils de génération visuelle pour transformer vos idées en images spectaculaires.