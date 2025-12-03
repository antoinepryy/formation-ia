# Module d'Exercices Pratiques ChatGPT

**Public cible** : 3 participants (débutant à utilisateur régulier)
**Durée estimée** : 4 heures
**Prérequis** : Compte ChatGPT créé (gratuit ou Plus)

---

## Structure de la formation

| Bloc | Durée | Contenu |
|------|-------|---------|
| Méthodes de prompting | 1h30 | Théorie et techniques essentielles |
| Ateliers pratiques | 1h30 | Exercices guidés par niveau |
| Bonnes pratiques & limites | 45 min | Éthique, vérification, cas d'usage |
| Projet final & évaluation | 15 min | Mise en pratique complète |

---

## Objectifs pédagogiques

À la fin de ce module, les participants seront capables de :

1. Naviguer dans l'interface ChatGPT avec aisance
2. Rédiger des prompts clairs et structurés
3. Utiliser les techniques d'itération pour améliorer les réponses
4. Exploiter les fonctionnalités avancées (GPTs, analyse de fichiers, génération d'images)
5. Créer des conversations multi-tours efficaces
6. Adapter le ton et le format des réponses selon leurs besoins
7. Identifier les limites de l'outil et vérifier les informations

---

# PARTIE 1 : Méthodes de prompting (1h30)

## Leçon 1 : Qu'est-ce qu'un prompt ?

Un **prompt** est l'instruction que vous donnez à l'IA. C'est votre moyen de communication avec le modèle.

> 💡 **Principe clé** : La qualité de la réponse dépend directement de la qualité de votre prompt. "Garbage in, garbage out."

### Les 4 niveaux de prompts

| Niveau | Caractéristique | Exemple |
|--------|-----------------|---------|
| **Basique** | Question simple | "C'est quoi le SEO ?" |
| **Précis** | Contexte ajouté | "Explique le SEO pour un débutant" |
| **Structuré** | Format demandé | "Explique le SEO en 5 points clés" |
| **Expert** | CRAC complet | Contexte + Rôle + Action + Contraintes |

---

## Leçon 2 : La méthode CRAC

La méthode **CRAC** est votre framework pour des prompts efficaces :

```
┌─────────────────────────────────────────────────────────────┐
│  C - CONTEXTE   →  Qui êtes-vous ? Quelle situation ?       │
│  R - RÔLE       →  Quel expert doit incarner ChatGPT ?      │
│  A - ACTION     →  Que voulez-vous qu'il fasse précisément ?│
│  C - CONTRAINTES→  Format, ton, longueur, public cible...   │
└─────────────────────────────────────────────────────────────┘
```

### Exemple comparatif

❌ **Prompt faible** :
> "Écris un email marketing"

✅ **Prompt CRAC** :
> **Contexte** : Je suis responsable marketing d'une boutique de thé bio en ligne.
> **Rôle** : Tu es un expert en copywriting e-commerce.
> **Action** : Rédige un email pour annoncer notre nouvelle collection de thés d'hiver.
> **Contraintes** : Ton chaleureux, 150 mots max, inclure un code promo HIVER2024, CTA vers le site.

---

## Leçon 3 : Les techniques de prompting avancées

### 3.1 Le Few-Shot Prompting (Apprentissage par l'exemple)

Donnez des exemples pour guider le format de réponse :

```
Transforme ces phrases en style professionnel :

Entrée : "Salut, ça te dit qu'on se voit demain ?"
Sortie : "Bonjour, seriez-vous disponible pour une rencontre demain ?"

Entrée : "C'est nul ton idée"
Sortie : "Cette proposition mériterait d'être retravaillée"

Entrée : "J'ai trop de boulot, je peux pas"
Sortie : [ChatGPT complète selon le pattern]
```

> 💡 **Tip** : 2-3 exemples suffisent généralement pour établir un pattern.

---

### 3.2 Le Chain of Thought (Raisonnement étape par étape)

Demandez à l'IA de raisonner avant de conclure :

```
Analyse ce problème étape par étape avant de proposer une solution :

1. D'abord, identifie les causes possibles
2. Ensuite, évalue chaque cause
3. Puis, propose des solutions pour chaque cause
4. Enfin, recommande la meilleure approche

Problème : Nos emails marketing ont un taux d'ouverture de 5%
```

> 💡 **Tip** : Cette technique améliore significativement la qualité des réponses pour les problèmes complexes.

---

### 3.3 Le Role Prompting (Jeu de rôle)

Assignez une expertise spécifique :

| Rôle | Effet sur la réponse |
|------|---------------------|
| "Tu es un avocat fiscaliste" | Vocabulaire juridique, prudence |
| "Tu es un community manager Gen Z" | Ton décontracté, références actuelles |
| "Tu es un data analyst senior" | Rigueur, chiffres, méthodologie |
| "Tu es un prof qui explique à un enfant de 10 ans" | Simplification, analogies |

---

### 3.4 L'itération conversationnelle

ChatGPT garde le contexte de la conversation. Exploitez-le :

```
Tour 1 : "Génère 10 idées de noms pour une app de fitness"
Tour 2 : "Développe les idées 3, 5 et 8"
Tour 3 : "Ajoute un slogan pour chacune"
Tour 4 : "Laquelle recommandes-tu pour une cible 18-25 ans ?"
```

> 💡 **Tip** : N'hésitez pas à dire "Non, recommence" ou "Plus court" ou "Moins formel".

---

## Leçon 4 : Les modificateurs de format

Contrôlez précisément le format de sortie :

### Formats courants

| Demande | Résultat |
|---------|----------|
| "Sous forme de tableau" | Données structurées en colonnes |
| "En bullet points" | Liste à puces concise |
| "En 3 paragraphes" | Structure narrative |
| "Format JSON" | Données exploitables par code |
| "Comme un tweet" | Ultra-concis, percutant |

### Modificateurs de longueur

```
"En 50 mots maximum"
"En une phrase"
"Développe en 500 mots"
"Résume en 3 bullet points"
```

### Modificateurs de ton

```
"Ton professionnel mais accessible"
"Style conversationnel"
"Registre soutenu"
"Comme si tu parlais à un ami"
```

---

## Leçon 5 : Les commandes magiques

Phrases clés qui améliorent les réponses :

| Commande | Usage |
|----------|-------|
| "Sois précis et factuel" | Évite le blabla |
| "Donne des exemples concrets" | Ancre dans le réel |
| "Explique ton raisonnement" | Transparence |
| "Si tu n'es pas sûr, dis-le" | Évite les hallucinations |
| "Pose-moi des questions si besoin" | Clarifie les ambiguïtés |
| "Critique ta propre réponse" | Auto-amélioration |

---

## Leçon 6 : Techniques avancées complémentaires

### 6.1 Le Zero-Shot vs Few-Shot

**Zero-Shot** : Demande directe sans exemple
```
"Classe ce commentaire comme positif, négatif ou neutre :
'Le produit est arrivé en retard mais la qualité est excellente'"
```

**Few-Shot** : Avec exemples pour guider
```
Exemples :
- "Super produit, je recommande !" → Positif
- "Nul, ne fonctionne pas" → Négatif
- "Livraison correcte" → Neutre

Maintenant classe : "Le produit est arrivé en retard mais la qualité est excellente"
```

> 💡 **Quand utiliser quoi ?**
> - Zero-shot : tâches simples, classifications évidentes
> - Few-shot : tâches ambiguës, format spécifique requis

---

### 6.2 Le Self-Consistency (Auto-cohérence)

Demandez plusieurs réponses et faites synthétiser :

```
"Génère 3 analyses différentes de ce problème marketing,
puis identifie les points communs et les divergences.
Conclus par la recommandation la plus fiable."
```

> 🎯 **Avantage** : Réduit les erreurs en croisant les raisonnements.

---

### 6.3 Le Prompt avec contraintes négatives

Précisez ce que vous ne voulez PAS :

```
"Rédige un email de relance client.

À ÉVITER :
- Pas de ton agressif ou culpabilisant
- Pas de phrases de plus de 20 mots
- Pas de jargon technique
- Pas de formules clichés type 'N'hésitez pas'"
```

> 💡 **Tip** : Les contraintes négatives sont souvent plus efficaces que les positives pour éviter les réponses génériques.

---

### 6.4 Le Meta-Prompting

Demandez à ChatGPT de créer le prompt pour vous :

```
"Je veux obtenir [OBJECTIF].
Quel serait le prompt idéal à te poser pour obtenir
le meilleur résultat possible ?
Propose-moi 3 versions de prompt, du plus simple au plus élaboré."
```

> 🎯 **Usage** : Excellent pour découvrir des angles auxquels vous n'auriez pas pensé.

---

### 6.5 Le Persona Stacking (Multi-personnalités)

Combinez plusieurs expertises :

```
"Réponds à cette question en adoptant successivement 3 points de vue :
1. Un expert marketing digital
2. Un directeur financier
3. Un client final

Puis synthétise les 3 perspectives en une recommandation équilibrée."
```

---

### 6.6 Le Reverse Prompting

Partez du résultat souhaité pour construire le prompt :

```
"Voici le type de réponse que je voudrais obtenir :
[COLLER UN EXEMPLE DE BONNE RÉPONSE]

Quel prompt aurais-je dû te donner pour obtenir ce résultat ?
Ensuite, utilise ce prompt pour traiter mon vrai sujet : [SUJET]"
```

---

## Leçon 7 : Optimisation et debugging de prompts

### 7.1 Quand un prompt ne fonctionne pas

**Symptômes courants et solutions** :

| Problème | Cause probable | Solution |
|----------|---------------|----------|
| Réponse trop vague | Manque de contexte | Ajouter CRAC complet |
| Réponse hors-sujet | Ambiguïté dans la demande | Reformuler plus précisément |
| Réponse trop longue | Pas de contrainte de longueur | Ajouter "en X mots/lignes" |
| Ton inadapté | Rôle non spécifié | Définir le persona |
| Format incorrect | Format non demandé | Spécifier tableau/liste/etc. |

### 7.2 La technique du debugging progressif

```
1. Prompt initial → Résultat insatisfaisant
2. "Qu'est-ce qui n'était pas clair dans ma demande ?"
3. "Comment aurais-je pu mieux formuler ma demande ?"
4. Prompt amélioré → Meilleur résultat
5. Itérer si nécessaire
```

---

# PARTIE 2 : Ateliers pratiques (1h30)

## Niveau 1 : Prise en main (Débutant)

### Exercice 1.1 - Premier contact
**Objectif** : Découvrir l'interface et poser sa première question

**Instructions** :
1. Connectez-vous à ChatGPT (chat.openai.com)
2. Créez une nouvelle conversation
3. Posez une question simple : *"Qu'est-ce que l'intelligence artificielle en 3 phrases ?"*
4. Observez la réponse générée

**Questions de réflexion** :
- La réponse est-elle compréhensible ?
- Auriez-vous posé la question différemment ?

> 💡 **Tip formateur** : Montrez comment la même question posée 2 fois peut donner des réponses légèrement différentes. C'est normal, l'IA est probabiliste.

---

### Exercice 1.2 - Reformulation et précision
**Objectif** : Comprendre l'importance de la précision dans les prompts

**Instructions** :
Testez ces 3 versions d'une même demande et comparez les résultats :

```
Version 1 : "Parle-moi du marketing"

Version 2 : "Explique-moi les bases du marketing digital"

Version 3 : "Explique-moi les 5 piliers du marketing digital
pour une petite entreprise, avec un exemple concret pour chaque pilier"
```

**Livrable** : Notez les différences de qualité entre les 3 réponses.

> 🎯 **Point clé** : Plus le prompt est précis, plus la réponse est utile. La version 3 obtient systématiquement de meilleurs résultats.

> 💡 **Tip** : Ajoutez toujours "pour qui" et "dans quel but" à vos prompts.

---

### Exercice 1.3 - Demander un format spécifique
**Objectif** : Apprendre à structurer les réponses

**Instructions** :
Demandez à ChatGPT de vous donner des idées de posts Instagram pour une boulangerie, en testant différents formats :

```
Prompt A : "Donne-moi des idées de posts Instagram pour une boulangerie"

Prompt B : "Donne-moi 5 idées de posts Instagram pour une boulangerie
artisanale. Présente-les sous forme de tableau avec :
| Thème | Légende | Hashtags suggérés |"

Prompt C : "Donne-moi 5 idées de posts Instagram pour une boulangerie
artisanale bio à Lyon. Pour chaque idée, indique :
- Le visuel suggéré
- La légende (max 150 caractères)
- 5 hashtags pertinents
- Le meilleur moment pour publier"
```

**Livrable** : Capture d'écran du meilleur résultat obtenu.

> 💡 **Tip** : Les tableaux Markdown sont directement exploitables. Vous pouvez les copier-coller dans Excel ou Google Sheets.

> 🎯 **Retenez** : Demander un format précis = réponse directement utilisable sans reformatage.

---

### Exercice 1.4 - Correction et amélioration de texte
**Objectif** : Utiliser ChatGPT comme assistant rédactionnel

**Instructions** :
Copiez ce texte mal rédigé et demandez à ChatGPT de l'améliorer :

```
"bonjour je vous ecrit pour vous dire que notre entreprise elle fait
des super produit bio et on voudrai bien que vous les acheter car
c'est vraiment bien pour la santé et pas cher en plus"
```

**Prompts à tester** :
1. "Corrige les fautes de ce texte"
2. "Réécris ce texte de manière professionnelle"
3. "Transforme ce texte en email commercial professionnel avec objet, introduction, 3 arguments et appel à l'action"

> 💡 **Tip** : ChatGPT excelle en réécriture. Utilisez-le pour améliorer vos brouillons, jamais pour créer du contenu ex nihilo sans votre input.

> ⚠️ **Attention** : Relisez toujours les textes générés. L'IA peut modifier le sens ou ajouter des informations non souhaitées.

---

## Niveau 2 : Maîtrise des prompts (Intermédiaire)

### Exercice 2.1 - La méthode CRAC
**Objectif** : Structurer ses prompts avec Contexte-Rôle-Action-Contraintes

**Instructions** :
Rédigez un prompt complet en utilisant la structure CRAC :

```
CONTEXTE : [Décrivez la situation]
RÔLE : [Quel expert voulez-vous que ChatGPT incarne]
ACTION : [Ce que vous voulez qu'il fasse]
CONTRAINTES : [Limites, format, ton, longueur...]
```

**Cas pratique** :
Vous devez rédiger une newsletter pour annoncer le lancement d'un nouveau service de livraison express pour votre e-commerce de vêtements.

**Exemple de prompt structuré** :
```
CONTEXTE : Je gère un e-commerce de vêtements éco-responsables.
Nous lançons un service de livraison express en 24h.

RÔLE : Tu es un expert en email marketing spécialisé dans la mode durable.

ACTION : Rédige une newsletter d'annonce pour ce nouveau service.

CONTRAINTES :
- Ton : enthousiaste mais professionnel
- Longueur : 200 mots maximum
- Inclure : un objet accrocheur, 3 bénéfices clients, un CTA
- Public cible : femmes 25-45 ans sensibles à l'écologie
```

**Livrable** : Votre prompt CRAC personnalisé + la réponse de ChatGPT

> 🎯 **Mini-leçon** : La structure CRAC fonctionne car elle mime la façon dont vous brieferiez un collègue humain. Plus vous êtes précis dans le brief, meilleur est le résultat.

> 💡 **Astuce pro** : Sauvegardez vos meilleurs prompts CRAC dans un document. Ils deviennent des templates réutilisables.

---

### Exercice 2.2 - L'itération conversationnelle
**Objectif** : Améliorer progressivement une réponse par le dialogue

**Instructions** :
1. Demandez à ChatGPT : *"Rédige un slogan pour une application de méditation"*
2. Puis enchaînez avec ces demandes d'amélioration :
   - "Propose 5 alternatives plus courtes (max 5 mots)"
   - "Rends-les plus percutants et mémorables"
   - "Ajoute une touche d'humour à 2 d'entre eux"
   - "Lequel recommandes-tu et pourquoi ?"

**Point clé** : ChatGPT garde le contexte de la conversation. Utilisez cette mémoire !

> 💡 **Tip** : Phrases utiles pour itérer :
> - "Raccourcis" / "Développe"
> - "Plus formel" / "Plus décontracté"
> - "Donne-moi 5 alternatives"
> - "Combine les idées 2 et 4"
> - "Non, recommence en..."

---

### Exercice 2.3 - Changer de ton et de persona
**Objectif** : Adapter le style de rédaction selon la cible

**Instructions** :
Faites rédiger le même message (annonce d'une promotion -20%) dans 4 styles différents :

```
Prompt 1 : "Rédige cette annonce pour LinkedIn, ton professionnel"
Prompt 2 : "Réécris pour Instagram, ton décontracté avec emojis"
Prompt 3 : "Version pour un email B2B formel"
Prompt 4 : "Version SMS ultra-court (max 160 caractères)"
```

**Livrable** : Tableau comparatif des 4 versions

> 🎯 **Ce qu'on apprend** : Le même message peut être décliné instantanément pour différents canaux. Gain de temps considérable pour une stratégie multicanale.

---

### Exercice 2.4 - Analyse et synthèse de texte
**Objectif** : Utiliser ChatGPT pour traiter de l'information

**Instructions** :
1. Trouvez un article d'actualité de votre secteur (300+ mots)
2. Copiez-le dans ChatGPT avec ces demandes successives :

```
"Voici un article : [COLLER L'ARTICLE]

1. Résume-le en 3 bullet points
2. Identifie les 3 informations clés pour un professionnel du marketing
3. Génère 3 questions que cet article soulève
4. Propose un post LinkedIn basé sur cet article"
```

> 💡 **Usage pro** : Cette technique est idéale pour la veille. Synthétisez rapidement 5-10 articles et créez du contenu à partir des insights.

> ⚠️ **Rappel** : Vérifiez toujours les faits clés avant de republier. ChatGPT peut mal interpréter ou résumer de façon inexacte.

---

### Exercice 2.5 - Les listes et la créativité
**Objectif** : Générer des idées en quantité

**Instructions** :
Utilisez la technique du brainstorming assisté :

```
"Je cherche des idées de contenu pour [VOTRE SECTEUR].
Génère 20 idées de posts réseaux sociaux, classées par catégorie :
- 5 idées éducatives
- 5 idées inspirantes
- 5 idées engageantes (questions, sondages)
- 5 idées promotionnelles subtiles

Format : titre accrocheur + description en 1 ligne"
```

**Bonus** : Demandez ensuite *"Développe l'idée n°X en post complet"*

> 💡 **Technique avancée** : Demandez "Génère 30 idées, même les plus folles" puis "Classe-les par faisabilité" et "Développe les 3 meilleures". La quantité amène la qualité par filtrage.

---

### Exercice 2.6 - Le Meta-Prompting en action
**Objectif** : Utiliser ChatGPT pour améliorer ses propres prompts

**Instructions** :
1. Choisissez une tâche que vous faites régulièrement
2. Demandez à ChatGPT de créer le prompt idéal :

```
"Je veux [DÉCRIRE VOTRE TÂCHE].
Génère pour moi le prompt parfait que je devrais te donner
pour obtenir le meilleur résultat.

Propose 3 versions :
1. Version courte (1-2 phrases)
2. Version standard (avec contexte)
3. Version CRAC complète (experte)"
```

3. Testez les 3 versions et comparez les résultats

**Livrable** : Votre meilleur prompt découvert + exemple de résultat

> 🎯 **Ce qu'on apprend** : ChatGPT connaît ses propres limites et peut vous aider à mieux l'utiliser.

---

### Exercice 2.7 - Contraintes négatives
**Objectif** : Maîtriser l'art de dire ce qu'on ne veut pas

**Instructions** :
Rédigez un email de relance commerciale en utilisant des contraintes négatives :

```
"Rédige un email de relance pour un prospect qui n'a pas répondu
depuis 2 semaines.

INTERDICTIONS :
- Aucune culpabilisation ("Vous n'avez pas répondu...")
- Aucun cliché ("Je me permets de revenir vers vous")
- Maximum 100 mots
- Pas plus de 3 phrases par paragraphe
- Aucune question rhétorique

Le mail doit proposer une valeur ajoutée concrète."
```

**Bonus** : Comparez avec un prompt sans contraintes négatives.

> 💡 **Pourquoi ça marche** : Les contraintes négatives éliminent les patterns génériques que ChatGPT utilise par défaut.

---

### Exercice 2.8 - Le Persona Stacking
**Objectif** : Obtenir des analyses multi-perspectives

**Instructions** :
Analysez une décision business sous plusieurs angles :

```
"Je dois décider si je lance un nouveau produit à 99€.

Analyse cette décision en incarnant successivement :
1. Le DIRECTEUR COMMERCIAL (focus revenus)
2. Le DIRECTEUR FINANCIER (focus rentabilité)
3. Le RESPONSABLE MARKETING (focus image de marque)
4. Un CLIENT TYPE (focus valeur perçue)

Pour chaque persona :
- 3 points positifs
- 3 points de vigilance
- 1 recommandation

Conclus par une synthèse équilibrée."
```

**Application** : Utilisez cette technique sur une vraie décision professionnelle.

---

## Niveau 3 : Fonctionnalités avancées (Expert)

### Exercice 3.1 - Analyse de fichiers (ChatGPT Plus)
**Objectif** : Exploiter la capacité d'analyse de documents

**Instructions** :
1. Uploadez un document (PDF, Excel, image) dans ChatGPT
2. Testez ces types de demandes :

```
Pour un PDF : "Résume ce document en 5 points clés et identifie
les actions à mener"

Pour un Excel : "Analyse ces données de vente. Quelles tendances
observes-tu ? Génère un rapport avec recommandations"

Pour une image : "Décris cette image et suggère 3 améliorations
pour un usage marketing"
```

**Cas pratique** : Uploadez un rapport ou une présentation de votre travail.

> 💡 **Tip** : Pour les fichiers Excel, demandez explicitement "Quelles sont les colonnes ?" puis "Analyse la colonne X". Procédez par étapes.

> ⚠️ **Confidentialité** : Ne uploadez jamais de documents contenant des données personnelles ou confidentielles sensibles.

---

### Exercice 3.2 - Génération d'images avec DALL-E
**Objectif** : Créer des visuels par le texte (ChatGPT Plus)

**Instructions** :
Testez la génération d'images avec des prompts de plus en plus précis :

```
Niveau basique : "Un chat"

Niveau intermédiaire : "Un chat roux assis sur un bureau
avec un ordinateur, style illustration moderne"

Niveau avancé : "Photo réaliste d'un chat roux Maine Coon
assis majestueusement sur un bureau en bois moderne,
lumière naturelle douce venant d'une fenêtre à gauche,
arrière-plan flou avec des plantes vertes,
ambiance cosy bureau à domicile, 4K, haute qualité"
```

**Exercice créatif** : Générez une image pour illustrer un post LinkedIn sur votre activité.

> 🎯 **Anatomie d'un bon prompt image** :
> 1. **Sujet** : Quoi/qui (un chat, une femme, un bureau...)
> 2. **Action/pose** : Que fait le sujet
> 3. **Style** : Photo réaliste, illustration, aquarelle, 3D...
> 4. **Éclairage** : Lumière naturelle, studio, coucher de soleil...
> 5. **Composition** : Gros plan, vue d'ensemble, arrière-plan...
> 6. **Ambiance** : Couleurs, mood, émotion recherchée

> ⚠️ **Limites** : DALL-E ne peut pas générer de logos avec du texte précis, ni des visages de célébrités.

---

### Exercice 3.3 - Création d'un GPT personnalisé
**Objectif** : Configurer un assistant spécialisé (ChatGPT Plus)

**Instructions** :
1. Allez dans "Explorer les GPTs" > "Créer"
2. Configurez un GPT pour votre usage professionnel :

```
Nom : [Assistant + votre métier]
Description : "Assistant spécialisé en [domaine] pour [tâche principale]"

Instructions (exemple pour un Community Manager) :
"Tu es un expert en community management pour des marques B2C.
- Tu proposes toujours 3 alternatives créatives
- Tu inclus systématiquement des hashtags pertinents
- Tu adaptes le ton selon le réseau social demandé
- Tu respectes les bonnes pratiques de chaque plateforme
- Tu suggères des heures de publication optimales"

Amorces de conversation :
- "Crée un post Instagram pour..."
- "Propose un calendrier éditorial pour..."
- "Analyse cette campagne et suggère des améliorations"
```

**Livrable** : Lien vers votre GPT personnalisé ou capture d'écran de la configuration.

> 💡 **Tip** : Un bon GPT personnalisé a des instructions très spécifiques. Définissez ce qu'il doit TOUJOURS faire et ce qu'il ne doit JAMAIS faire.

> 🎯 **Idées de GPT utiles** :
> - Assistant de rédaction d'emails (votre ton, vos signatures)
> - Générateur de posts pour vos réseaux spécifiques
> - Aide à la rédaction de comptes-rendus de réunion
> - Préparateur d'entretiens pour votre secteur

---

### Exercice 3.4 - Le prompt en chaîne (Chain of Thought)
**Objectif** : Obtenir des raisonnements plus fiables

**Instructions** :
Comparez ces deux approches pour une tâche complexe :

```
Approche simple :
"Quelle stratégie marketing adopter pour lancer une nouvelle
marque de cosmétiques bio ?"

Approche Chain of Thought :
"Je lance une marque de cosmétiques bio ciblant les 25-40 ans.
Aide-moi à construire une stratégie marketing.

Procède étape par étape :
1. D'abord, analyse le marché et identifie 3 opportunités
2. Ensuite, définis le positionnement idéal
3. Puis, propose les canaux de communication prioritaires
4. Enfin, suggère un plan d'action sur 3 mois

Pour chaque étape, explique ton raisonnement avant de conclure."
```

> 🎯 **Pourquoi ça marche** : En forçant l'IA à décomposer son raisonnement, on réduit les erreurs et on obtient des réponses plus réfléchies.

> 💡 **Phrases magiques pour le Chain of Thought** :
> - "Réfléchis étape par étape"
> - "Avant de conclure, analyse..."
> - "Examine tous les angles"
> - "Explique ton raisonnement à chaque étape"

---

### Exercice 3.5 - Simulation et jeu de rôle
**Objectif** : Utiliser ChatGPT pour s'entraîner

**Instructions** :
Créez une simulation de situation professionnelle :

```
"Simule un entretien de négociation commerciale.

Tu joues le rôle d'un client potentiel difficile qui :
- A un budget limité
- Compare avec la concurrence
- Pose des questions pièges sur les délais

Je suis le commercial. Commence par me poser ta première objection.
Après chaque échange, donne-moi un feedback sur ma réponse
et suggère une amélioration."
```

**Variantes** :
- Simulation d'entretien d'embauche
- Simulation de présentation client
- Simulation de gestion de crise sur les réseaux sociaux

> 💡 **Tip** : Demandez un feedback après chaque échange. ChatGPT peut jouer le rôle de coach en même temps que celui d'interlocuteur.

> 🎯 **Usage RH** : Excellent pour préparer des entretiens difficiles, des négociations salariales, ou des annonces délicates.

---

### Exercice 3.6 - Automatisation de tâches répétitives
**Objectif** : Créer des templates réutilisables

**Instructions** :
Créez un "méga-prompt" pour automatiser une tâche récurrente :

```
"Tu es mon assistant pour la création de fiches produit e-commerce.

Quand je te donne le nom d'un produit et ses caractéristiques,
génère automatiquement :

1. TITRE SEO (max 60 caractères, mot-clé principal au début)
2. META DESCRIPTION (max 155 caractères, incitative)
3. DESCRIPTION COURTE (50 mots, bénéfices clients)
4. DESCRIPTION LONGUE (150 mots, storytelling + caractéristiques)
5. 5 BULLET POINTS de vente
6. SUGGESTIONS DE MOTS-CLÉS (10 mots-clés secondaires)
7. FAQ (3 questions/réponses anticipées)

Ton : [professionnel/décontracté/luxe - à préciser]
Cible : [à préciser]

Premier produit : [NOM ET CARACTÉRISTIQUES]"
```

**Livrable** : Votre template personnalisé pour une tâche de votre quotidien.

> 💡 **Pro tip** : Sauvegardez vos méga-prompts dans un document. Copiez-collez au début de chaque nouvelle conversation pour "charger" votre assistant personnalisé.

> 🎯 **Templates utiles à créer** :
> - Générateur de fiches produit
> - Créateur de posts réseaux sociaux
> - Rédacteur de comptes-rendus
> - Analyseur de données CSV/Excel
> - Traducteur avec glossaire métier

---

### Exercice 3.7 - Le Self-Consistency en pratique
**Objectif** : Obtenir des réponses plus fiables par croisement

**Instructions** :
Utilisez la technique de l'auto-cohérence pour une analyse complexe :

```
"Analyse ce problème business 3 fois de manière indépendante,
comme si tu découvrais le problème à chaque fois.

PROBLÈME : [Décrire un défi professionnel réel]

Pour chaque analyse :
- Identifie 3 causes principales
- Propose 2 solutions
- Donne un niveau de confiance (1-10)

Ensuite :
1. Compare tes 3 analyses
2. Identifie les points communs (haute fiabilité)
3. Identifie les divergences (à approfondir)
4. Conclus par la recommandation la plus solide"
```

**Cas pratique** : Appliquez à un vrai problème de votre entreprise.

> 🎯 **Pourquoi ça marche** : Si 3 raisonnements indépendants convergent, la conclusion est plus fiable.

---

### Exercice 3.8 - Création de workflows automatisés
**Objectif** : Créer des chaînes de prompts pour des tâches complexes

**Instructions** :
Créez un workflow complet pour le traitement de feedback client :

```
"Je vais te donner des avis clients. Pour chaque avis, exécute ce workflow :

ÉTAPE 1 - CLASSIFICATION
- Sentiment : Positif / Neutre / Négatif
- Sujet : Produit / Livraison / SAV / Prix / Autre
- Urgence : Basse / Moyenne / Haute

ÉTAPE 2 - EXTRACTION
- Points positifs mentionnés
- Points négatifs mentionnés
- Suggestions du client

ÉTAPE 3 - ACTION
- Réponse type suggérée
- Action interne recommandée
- Priorité de traitement

ÉTAPE 4 - TAGS
- 3 mots-clés pour catégorisation

Présente le tout dans un format structuré.

Premier avis à traiter : [AVIS]"
```

**Livrable** : Votre workflow personnalisé pour une tâche récurrente.

---

### Exercice 3.9 - Debug de prompts
**Objectif** : Apprendre à corriger un prompt qui ne fonctionne pas

**Instructions** :
1. Testez ce prompt volontairement vague :
```
"Fais-moi un truc pour mon business"
```

2. Demandez à ChatGPT de l'analyser :
```
"Pourquoi ce prompt est-il inefficace ?
Identifie tout ce qui manque et propose
une version corrigée en utilisant la méthode CRAC"
```

3. Testez la version corrigée et comparez.

**Exercice avancé** : Prenez un de vos prompts réels qui a donné un mauvais résultat et faites-le debugger par ChatGPT.

---

## Exercice Final : Projet intégré

### Le défi créatif (30 minutes)

**Objectif** : Mobiliser toutes les compétences acquises

**Scénario** :
Vous devez créer une mini-campagne de communication pour le lancement d'un produit/service fictif de votre choix.

**Livrables à produire avec ChatGPT** :

1. **Naming** : 5 propositions de nom avec justification
2. **Slogan** : 3 versions (courte, longue, décalée)
3. **Pitch** : Présentation en 100 mots
4. **Post LinkedIn** : Annonce du lancement
5. **Post Instagram** : Version visuelle avec légende et hashtags
6. **Email** : Newsletter d'annonce aux clients
7. **FAQ** : 5 questions/réponses pour le service client

**Contraintes** :
- Utilisez au minimum 3 techniques vues dans ce module
- Faites au moins 2 itérations par élément
- Documentez vos meilleurs prompts

---

### Bonus : Défi Speed-Prompting (10 minutes)

**Règles du jeu** :
- Vous avez 10 minutes chrono
- Objectif : obtenir le meilleur résultat possible en un minimum d'échanges
- Thème : Créer un pitch elevator de 30 secondes pour votre activité

**Scoring** :
- Résultat satisfaisant en 1 échange : 10 points
- En 2 échanges : 8 points
- En 3 échanges : 6 points
- En 4+ échanges : 4 points

> 🎯 **Ce qu'on apprend** : Un bon prompt initial fait gagner énormément de temps.

---

# PARTIE 3 : Bonnes pratiques & limites (45 min)

## Les limites fondamentales de ChatGPT

### Ce que ChatGPT NE PEUT PAS faire

| Limitation | Explication | Solution |
|------------|-------------|----------|
| **Connaissances datées** | Données d'entraînement avec date de coupure | Vérifier les infos récentes sur sources officielles |
| **Hallucinations** | Peut inventer des faits avec assurance | Toujours fact-checker les infos critiques |
| **Pas d'accès internet** | (sauf navigation activée sur Plus) | Coller le contenu dans le prompt |
| **Calculs complexes** | Peut se tromper sur les maths | Utiliser Code Interpreter ou Excel |
| **Informations personnelles** | Ne connaît pas votre entreprise | Fournir le contexte à chaque fois |
| **Données temps réel** | Pas de cours de bourse, météo, etc. | Utiliser des outils dédiés |

---

## Les hallucinations : comprendre et éviter

### Qu'est-ce qu'une hallucination ?

Une **hallucination** est une information présentée comme vraie par l'IA mais qui est fausse, inventée ou inexacte.

**Exemples courants** :
- Citations de livres qui n'existent pas
- Statistiques inventées
- Références à des études fictives
- Dates ou faits historiques incorrects

### Comment les détecter ?

> ⚠️ **Signaux d'alerte** :
> - Chiffres trop précis (ex: "exactement 73.2% des utilisateurs...")
> - Citations avec auteur et date très spécifiques
> - Informations invérifiables
> - Réponses trop parfaites à des questions complexes

### Comment les éviter ?

```
Ajoutez à vos prompts :
- "Si tu n'es pas sûr, dis-le clairement"
- "Indique le niveau de confiance de tes affirmations"
- "Ne cite que des sources que tu peux vérifier"
- "Distingue les faits des suppositions"
```

---

## La vérification des informations

### La règle des 3V

1. **Vérifier** : Recoupez avec des sources officielles
2. **Valider** : Faites relire par un expert du domaine
3. **Vigilance** : Restez critique, même si la réponse semble parfaite

### Quand vérifier absolument ?

| Type d'information | Risque | Action |
|-------------------|--------|--------|
| Données chiffrées | Élevé | Vérifier source originale |
| Faits historiques | Moyen | Recouper avec 2 sources |
| Informations juridiques | Très élevé | Consulter un expert |
| Conseils médicaux | Critique | JAMAIS suivre sans médecin |
| Informations scientifiques | Élevé | Vérifier publications |

---

## Éthique et confidentialité

### Ce que vous ne devez JAMAIS partager

❌ **Données interdites** :
- Données personnelles (noms, adresses, téléphones)
- Informations médicales
- Données financières sensibles
- Mots de passe et identifiants
- Documents confidentiels d'entreprise
- Données clients non anonymisées

### Les bonnes pratiques de confidentialité

✅ **À faire** :
- Anonymiser les données avant de les soumettre
- Utiliser des exemples fictifs
- Désactiver l'historique si nécessaire (Settings > Data Controls)
- Préférer ChatGPT Enterprise pour les usages professionnels sensibles

> ⚠️ **Rappel légal** : Les données envoyées à ChatGPT peuvent être utilisées pour entraîner les modèles (sauf désactivation ou version Enterprise).

---

## Biais et équité

### Les biais de l'IA

ChatGPT peut reproduire des biais présents dans ses données d'entraînement :
- Biais de genre (associer certains métiers à un genre)
- Biais culturels (perspective occidentale dominante)
- Biais temporels (informations datées)

### Comment les atténuer ?

```
Techniques de débiaisation :
- "Propose des alternatives diversifiées"
- "Inclus différentes perspectives culturelles"
- "Évite les stéréotypes de genre"
- "Présente des points de vue contradictoires"
```

---

## Le bon usage professionnel

### Quand utiliser ChatGPT ?

| Tâche | Recommandation | Niveau de vérification |
|-------|---------------|----------------------|
| Brainstorming | ✅ Excellent | Faible |
| Premier jet de texte | ✅ Très bon | Moyen |
| Reformulation | ✅ Excellent | Faible |
| Synthèse de documents | ✅ Bon | Moyen |
| Traduction | ⚠️ Correct | Élevé pour le pro |
| Données factuelles | ⚠️ Prudence | Très élevé |
| Conseils juridiques/médicaux | ❌ Déconseillé | Expert obligatoire |

### Les 5 règles d'or

1. **ChatGPT est un assistant, pas un expert** - Vous restez responsable
2. **Garbage in, garbage out** - La qualité du prompt détermine la qualité de la réponse
3. **Itérer pour améliorer** - Rarement bon du premier coup
4. **Toujours relire et adapter** - Le contenu généré doit être personnalisé
5. **Vérifier les faits critiques** - Ne jamais faire confiance aveuglément

---

## Exercice pratique : Identifier les problèmes

**Objectif** : Développer son sens critique

**Instructions** :
Posez cette question à ChatGPT et analysez la réponse :

```
"Donne-moi 5 statistiques sur l'usage des réseaux sociaux en France en 2024"
```

**Questions d'analyse** :
1. Les chiffres sont-ils sourcés ?
2. Pouvez-vous vérifier ces statistiques ?
3. Quels signaux d'alerte repérez-vous ?
4. Comment reformuleriez-vous la question pour éviter les hallucinations ?

**Reformulation suggérée** :
```
"Quelles sont les tendances générales d'usage des réseaux sociaux en France ?
Si tu cites des chiffres, indique clairement leur source et leur date.
Si tu n'es pas sûr d'une information, dis-le."
```

---

## Checklist de validation

Avant d'utiliser un contenu généré par ChatGPT :

- [ ] J'ai relu et compris le contenu
- [ ] J'ai vérifié les faits importants
- [ ] J'ai adapté le ton à ma marque/contexte
- [ ] J'ai supprimé les formulations trop génériques
- [ ] Je n'ai pas partagé de données sensibles
- [ ] Je peux assumer ce contenu comme le mien

---

# PARTIE 4 : Projet final & évaluation (15 min)

## Projet final : Votre cas d'usage professionnel

**Objectif** : Appliquer toutes les techniques apprises à un cas réel de votre quotidien

**Instructions** :
1. Identifiez une tâche récurrente de votre travail qui pourrait être assistée par ChatGPT
2. Créez un prompt CRAC complet pour cette tâche
3. Testez-le et itérez au moins 2 fois
4. Documentez votre prompt final

**Exemples de cas d'usage** :
- Rédaction d'emails types (relance, remerciement, réclamation)
- Création de contenus marketing (posts, newsletters)
- Analyse de documents (rapports, contrats, feedbacks)
- Préparation de réunions (ordres du jour, comptes-rendus)
- Formation et documentation (procédures, FAQ)

**Livrable attendu** :
```
MON CAS D'USAGE : [Description]

PROMPT FINAL :
[Votre prompt CRAC optimisé]

TECHNIQUES UTILISÉES :
- [ ] CRAC
- [ ] Few-Shot
- [ ] Chain of Thought
- [ ] Contraintes négatives
- [ ] Autre : ___________

RÉSULTAT OBTENU : [Capture ou description]

CE QUE J'AI APPRIS : [1-2 phrases]
```

---

## Grille d'auto-évaluation

Évaluez votre niveau à la fin de la formation :

| Compétence | Non acquis | En cours | Acquis |
|------------|------------|----------|--------|
| Rédiger un prompt clair et précis | ☐ | ☐ | ☐ |
| Utiliser la structure CRAC | ☐ | ☐ | ☐ |
| Demander un format spécifique | ☐ | ☐ | ☐ |
| Itérer pour améliorer les réponses | ☐ | ☐ | ☐ |
| Adapter le ton selon la cible | ☐ | ☐ | ☐ |
| Analyser un document uploadé | ☐ | ☐ | ☐ |
| Générer des images pertinentes | ☐ | ☐ | ☐ |
| Créer un GPT personnalisé | ☐ | ☐ | ☐ |
| Utiliser le Chain of Thought | ☐ | ☐ | ☐ |
| Créer des templates réutilisables | ☐ | ☐ | ☐ |
| Identifier les hallucinations | ☐ | ☐ | ☐ |
| Appliquer les bonnes pratiques éthiques | ☐ | ☐ | ☐ |

---

## Quiz final rapide

Testez vos connaissances (réponses en fin de document) :

**Q1.** Que signifie CRAC ?
- A) Créer, Rédiger, Analyser, Corriger
- B) Contexte, Rôle, Action, Contraintes
- C) ChatGPT, Résultat, Automatisation, Création

**Q2.** Quelle technique utiliser pour obtenir un format de réponse spécifique ?
- A) Zero-Shot
- B) Few-Shot (avec exemples)
- C) Meta-Prompting

**Q3.** Comment réduire les hallucinations ?
- A) Demander plus de détails
- B) Ajouter "Si tu n'es pas sûr, dis-le"
- C) Utiliser un ton formel

**Q4.** Que ne devez-vous JAMAIS partager avec ChatGPT ?
- A) Vos idées de contenu
- B) Des données personnelles de clients
- C) Des questions sur votre secteur

**Q5.** Quelle est la meilleure façon d'améliorer une réponse insatisfaisante ?
- A) Recommencer une nouvelle conversation
- B) Itérer dans la même conversation avec des précisions
- C) Changer de modèle d'IA

---

## Réponses du quiz

Q1: **B** - Contexte, Rôle, Action, Contraintes
Q2: **B** - Few-Shot avec exemples pour guider le format
Q3: **B** - Demander à l'IA d'indiquer son incertitude
Q4: **B** - Jamais de données personnelles ou confidentielles
Q5: **B** - L'itération conserve le contexte et améliore progressivement

---

## Feedback de la formation

Aidez-nous à améliorer cette formation :

| Question | 1 | 2 | 3 | 4 | 5 |
|----------|---|---|---|---|---|
| Clarté des explications | ☐ | ☐ | ☐ | ☐ | ☐ |
| Utilité des exercices | ☐ | ☐ | ☐ | ☐ | ☐ |
| Rythme de la formation | ☐ | ☐ | ☐ | ☐ | ☐ |
| Applicabilité à mon travail | ☐ | ☐ | ☐ | ☐ | ☐ |

**Ce que j'ai le plus apprécié** : _________________________________

**Ce qui pourrait être amélioré** : _________________________________

**Une technique que je vais utiliser dès demain** : _________________________________

---

## Ressources complémentaires

- **Raccourcis utiles** :
  - `Ctrl/Cmd + Shift + C` : Copier la dernière réponse
  - `/` : Accès rapide aux GPTs

- **Bonnes pratiques** :
  - Toujours vérifier les informations factuelles
  - Ne jamais partager de données sensibles
  - Sauvegarder vos meilleurs prompts dans un document

- **Pour aller plus loin** :
  - Tester Claude (claude.ai) pour comparer
  - Explorer les GPTs de la communauté
  - Créer une bibliothèque de prompts par usage

---

## Mémo : Les prompts essentiels à retenir

### Structure CRAC en une ligne
```
[CONTEXTE] + [RÔLE] + [ACTION] + [CONTRAINTES]
```

### Phrases magiques universelles
```
"Explique étape par étape..."
"Donne-moi X alternatives..."
"Si tu n'es pas sûr, dis-le..."
"Sous forme de [tableau/liste/paragraphes]..."
"Pour un public de [cible]..."
"En maximum X mots/phrases..."
```

### Template de prompt universel
```
Contexte : Je suis [rôle] dans [secteur].
Situation : [description du besoin]
Demande : [action précise souhaitée]
Format : [tableau/liste/texte], [X mots], [ton]
Contraintes : [ce qu'il faut inclure/éviter]
```

---

## Récapitulatif des techniques de prompting

| Technique | Description | Quand l'utiliser |
|-----------|-------------|------------------|
| **CRAC** | Contexte-Rôle-Action-Contraintes | Pour tout prompt professionnel |
| **Few-Shot** | Donner des exemples | Quand le format est spécifique |
| **Zero-Shot** | Demande directe | Tâches simples et claires |
| **Chain of Thought** | Raisonnement étape par étape | Problèmes complexes |
| **Role Prompting** | Assigner un persona | Adapter le ton/expertise |
| **Self-Consistency** | Analyses multiples croisées | Décisions importantes |
| **Contraintes négatives** | Dire ce qu'on ne veut pas | Éviter les clichés |
| **Meta-Prompting** | Faire créer le prompt | Découvrir de nouveaux angles |
| **Persona Stacking** | Multi-perspectives | Analyses 360° |
| **Reverse Prompting** | Partir du résultat | Reproduire un style |

---

## Checklist du prompt parfait

Avant d'envoyer un prompt important, vérifiez :

- [ ] **Contexte** : Ai-je expliqué qui je suis et ma situation ?
- [ ] **Rôle** : Ai-je défini l'expertise attendue de ChatGPT ?
- [ ] **Action** : Ma demande est-elle claire et précise ?
- [ ] **Format** : Ai-je spécifié le format de sortie souhaité ?
- [ ] **Longueur** : Ai-je indiqué une contrainte de taille ?
- [ ] **Ton** : Ai-je précisé le style de communication ?
- [ ] **Public** : Ai-je mentionné la cible finale ?
- [ ] **Contraintes** : Ai-je dit ce qu'il faut éviter ?

---

## Glossaire des termes clés

| Terme | Définition |
|-------|------------|
| **Prompt** | Instruction donnée à l'IA |
| **Token** | Unité de texte (~4 caractères en français) |
| **Hallucination** | Information fausse présentée comme vraie |
| **Fine-tuning** | Personnalisation d'un modèle avec des données spécifiques |
| **Température** | Paramètre de créativité (0 = déterministe, 1 = créatif) |
| **Context window** | Quantité de texte que l'IA peut "voir" |
| **GPT** | Generative Pre-trained Transformer |
| **LLM** | Large Language Model |
| **RAG** | Retrieval-Augmented Generation |

---

*Module créé pour la formation IA - Prompt Engineering*
*Durée : 4 heures | Version enrichie*
