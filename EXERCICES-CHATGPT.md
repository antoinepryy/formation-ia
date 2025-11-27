# Module d'Exercices Pratiques ChatGPT

**Public cible** : 3 participants (débutant à utilisateur régulier)
**Durée estimée** : 2h30 - 3h
**Prérequis** : Compte ChatGPT créé (gratuit ou Plus)

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

## Grille d'auto-évaluation

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

*Module créé pour la formation IA - Prompt Engineering*
