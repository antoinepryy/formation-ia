# Module 3 : Exercices pratiques - IA & Créativité

## 🎨 Exercice 1 : Bootcamp Midjourney - Du débutant au pro
**Durée : 90 minutes**

### Objectif
Maîtriser progressivement toutes les fonctionnalités de Midjourney.

### Phase 1 : Premiers pas (20 min)

**1.1 Génération basique**
Créez 4 images simples sans paramètres :

| Prompt | Résultat obtenu | Note /10 |
|--------|-----------------|----------|
| "a red apple" | | |
| "sunset over mountains" | | |
| "happy dog" | | |
| "futuristic car" | | |

**1.2 Ajout de style**
Reprenez les mêmes sujets avec un style :

| Prompt avec style | Amélioration ? | Note /10 |
|-------------------|---------------|----------|
| "a red apple, oil painting" | | |
| "sunset over mountains, japanese watercolor" | | |
| "happy dog, pixar style" | | |
| "futuristic car, cyberpunk aesthetic" | | |

### Phase 2 : Paramètres essentiels (25 min)

**2.1 Aspect Ratio**
Testez différents ratios pour un portrait :

```
Base : "portrait of a scientist"
```

- [ ] Standard : `--ar 1:1`
- [ ] Portrait : `--ar 2:3`
- [ ] Paysage : `--ar 16:9`
- [ ] Cinémascope : `--ar 21:9`
- [ ] Mobile : `--ar 9:16`

**Meilleur ratio pour ce sujet :** ___________

**2.2 Stylization**
Même prompt, différentes valeurs :

```
"abstract colorful explosion"
```

- [ ] Minimal : `--s 50`
- [ ] Faible : `--s 250`
- [ ] Défaut : `--s 100`
- [ ] Élevé : `--s 750`
- [ ] Maximum : `--s 1000`

**Observations sur l'impact :**
_________________________________

**2.3 Chaos**
Explorez la variabilité :

```
"garden party in wonderland"
```

- [ ] Cohérent : `--chaos 0`
- [ ] Varié : `--chaos 25`
- [ ] Créatif : `--chaos 50`
- [ ] Imprévisible : `--chaos 100`

**Niveau optimal pour ce projet :** ___________

### Phase 3 : Techniques avancées (25 min)

**3.1 Multi-prompting avec poids**

Créez une image équilibrée :
```
Formule : concept1::poids1 concept2::poids2
```

Vos tests :
1. `nature::1 technology::1` = _____________
2. `nature::2 technology::1` = _____________
3. `nature::1 technology::2` = _____________
4. `nature::3 technology::0.5` = _____________

**Ratio optimal découvert :** ___________

**3.2 Exclusions négatives**

Prompt de base : `"busy city street"`

Ajoutez progressivement :
1. `--no people` : Impact = _____________
2. `--no cars` : Impact = _____________
3. `--no buildings` : Impact = _____________
4. `--no people cars signs` : Impact = _____________

**3.3 Image + Text prompting**

Si vous avez une image de référence :
1. Upload image
2. Prompt : `[URL] mixed with [your concept] --iw 0.5`
3. Testez --iw à : 0.25, 0.5, 1, 2
4. Documentez les différences

### Phase 4 : Création de série cohérente (20 min)

**Mission :** Créer 4 images cohérentes pour une marque

**Brief :** Marque de thé premium japonais

Utilisez `--seed [nombre]` pour cohérence :

1. **Packaging :** `[votre prompt] --seed 12345`
2. **Publicité :** `[votre prompt] --seed 12345`
3. **Boutique :** `[votre prompt] --seed 12345`
4. **Site web :** `[votre prompt] --seed 12345`

**Évaluation cohérence série :** ___/10

### Tableau de progression

| Compétence | Niveau atteint | Prochain objectif |
|------------|---------------|-------------------|
| Prompts basiques | ⬜⬜⬜⬜⬜ | |
| Paramètres | ⬜⬜⬜⬜⬜ | |
| Styles artistiques | ⬜⬜⬜⬜⬜ | |
| Techniques avancées | ⬜⬜⬜⬜⬜ | |
| Cohérence de marque | ⬜⬜⬜⬜⬜ | |

---

## 🎨 Exercice 2 : Adobe Firefly - Workflow professionnel complet
**Durée : 75 minutes**

### Objectif
Créer une campagne visuelle complète avec Adobe Firefly et Photoshop.

### Projet : Lancement d'une nouvelle boisson énergétique

### Phase 1 : Génération des assets de base (20 min)

**1.1 Dans Firefly Web**

Générez 5 éléments :

1. **Produit hero**
   ```
   Prompt : "energy drink can, metallic blue and silver, 
   lightning effects, studio lighting, product photography"
   ```
   - [ ] Généré
   - [ ] Téléchargé
   - Qualité : ___/10

2. **Background dynamique**
   ```
   Prompt : "abstract energy waves, electric blue and purple, 
   dynamic motion, particle effects"
   ```
   - [ ] Généré
   - [ ] Téléchargé
   - Qualité : ___/10

3. **Élément graphique 1**
   ```
   Prompt : [votre création]
   ```

4. **Élément graphique 2**
   ```
   Prompt : [votre création]
   ```

5. **Texture/Pattern**
   ```
   Prompt : [votre création]
   ```

### Phase 2 : Composition dans Photoshop (25 min)

**2.1 Setup du document**
- [ ] Nouveau document : 1920x1080px, 300dpi
- [ ] Importer tous les assets
- [ ] Organiser les calques

**2.2 Generative Fill Magic**

**Test 1 : Extension du produit**
1. Sélectionnez le bas de la canette
2. Étendez la sélection vers le bas
3. Generative Fill : "reflection on glossy surface"
4. Note résultat : ___/10

**Test 2 : Ajout d'éléments**
1. Créez une sélection vide
2. Generative Fill : "ice cubes with condensation"
3. Positionnez autour du produit
4. Note intégration : ___/10

**Test 3 : Amélioration du fond**
1. Sélectionnez le background
2. Generative Fill : "add depth and glow effects"
3. Ajustez l'opacité
4. Note amélioration : ___/10

**2.3 Finitions**
- [ ] Ajustement des couleurs
- [ ] Ajout de texte (slogan)
- [ ] Effects de lumière
- [ ] Export final

### Phase 3 : Déclinaisons (20 min)

Créez 3 variantes à partir de votre composition :

1. **Version réseaux sociaux**
   - Format : 1080x1080 (carré)
   - Adaptations : ________________

2. **Version story**
   - Format : 1080x1920 (vertical)
   - Adaptations : ________________

3. **Version banner web**
   - Format : 728x90 (horizontal)
   - Adaptations : ________________

### Phase 4 : Text Effects (10 min)

**Dans Firefly Text Effects :**

Créez 3 variations du slogan "PURE ENERGY" :

1. **Effet 1 :** `[votre prompt effet]`
   - Résultat : ___________

2. **Effet 2 :** `[votre prompt effet]`
   - Résultat : ___________

3. **Effet 3 :** `[votre prompt effet]`
   - Résultat : ___________

### Checklist qualité finale

- [ ] Cohérence visuelle
- [ ] Qualité technique (résolution)
- [ ] Impact visuel
- [ ] Respect du brief
- [ ] Originalité
- [ ] Adaptabilité multi-formats

**Score total : ___/60**

---

## 🎨 Exercice 3 : Gemini - Direction artistique IA
**Durée : 60 minutes**

### Objectif
Utiliser Gemini comme directeur artistique virtuel.

### Projet : Refonte visuelle d'un site e-commerce

### Phase 1 : Analyse de l'existant (15 min)

**1.1 Audit visuel avec Gemini**

Prenez 3 screenshots de sites concurrents et demandez à Gemini :

```
Analyse ces 3 sites e-commerce et identifie :
1. Forces visuelles
2. Faiblesses UX
3. Tendances communes
4. Opportunités de différenciation
```

**Insights obtenus :**
1. _________________________________
2. _________________________________
3. _________________________________

**1.2 Benchmark créatif**

```
Prompt Gemini :
"Liste 5 sites e-commerce reconnus pour leur excellence visuelle en 2024,
avec pour chacun :
- Point fort principal
- Élément innovant
- Leçon à retenir"
```

### Phase 2 : Stratégie créative (20 min)

**2.1 Brief créatif généré**

```
Prompt Gemini :
"Crée un brief créatif pour la refonte d'un site e-commerce de [VOTRE CHOIX] :

BRAND ESSENCE
- Mission :
- Valeurs :
- Personnalité :

DIRECTION VISUELLE
- Mood :
- Couleurs :
- Typographie :
- Imagerie :

PRINCIPES UX
- Navigation :
- Interaction :
- Feedback :
```

**2.2 Moodboard textuel**

Demandez à Gemini de créer un "moodboard en mots" :

```
"Décris en 5 paragraphes visuels détaillés l'atmosphère idéale 
pour ce site, comme si tu décrivais des images"
```

### Phase 3 : Génération et critique (15 min)

**3.1 Prompts pour Midjourney**

Demandez à Gemini :
```
"Génère 5 prompts Midjourney optimisés pour créer :
1. Hero banner homepage
2. Card produit
3. Icônes de catégories
4. Background patterns
5. Images lifestyle"
```

**3.2 Génération dans Midjourney**

Utilisez les prompts et générez les images.

**3.3 Critique constructive**

Montrez les résultats à Gemini :
```
"Voici les images générées. Pour chacune, donne :
- Note /10
- 2 points forts
- 2 améliorations suggérées
- Prompt optimisé v2"
```

### Phase 4 : Synthèse et recommandations (10 min)

**4.1 Design system**

```
Prompt Gemini :
"Basé sur notre travail, crée un mini design system :
- Palette (5 couleurs hex)
- Typographie (titres, corps, CTA)
- Spacing (système 8px)
- Composants clés (5)
- Animations suggérées"
```

**4.2 Roadmap d'implémentation**

```
"Propose une roadmap en 4 sprints pour implémenter cette refonte"
```

### Livrables finaux

- [ ] Document de stratégie créative
- [ ] 10 images générées et approuvées
- [ ] Design system basique
- [ ] Plan d'action

---

## 🎨 Exercice 4 : Moodboard professionnel complet
**Durée : 90 minutes**

### Objectif
Créer un moodboard de niveau agence pour un client réel.

### Client : Nouvelle marque de cosmétiques naturels

### Phase 1 : Research & Discovery (20 min)

**1.1 Analyse de marché**

Tableau de positionnement :

| Concurrent | Style visuel | Palette | Points forts | Faiblesses |
|------------|--------------|---------|--------------|------------|
| Marque A | | | | |
| Marque B | | | | |
| Marque C | | | | |

**1.2 Tendances 2024**

Identifiez 5 tendances visuelles pertinentes :
1. _________________________________
2. _________________________________
3. _________________________________
4. _________________________________
5. _________________________________

### Phase 2 : Génération d'assets (40 min)

**2.1 Images conceptuelles (Midjourney)**

Générez 15 images dans ces catégories :

**Textures naturelles (3 images)**
```
Prompts :
1. ________________________________
2. ________________________________
3. ________________________________
```

**Portraits lifestyle (3 images)**
```
Prompts :
1. ________________________________
2. ________________________________
3. ________________________________
```

**Produits en situation (3 images)**
```
Prompts :
1. ________________________________
2. ________________________________
3. ________________________________
```

**Ingrédients (3 images)**
```
Prompts :
1. ________________________________
2. ________________________________
3. ________________________________
```

**Ambiances abstraites (3 images)**
```
Prompts :
1. ________________________________
2. ________________________________
3. ________________________________
```

**2.2 Palette de couleurs**

Extrayez 5 couleurs dominantes :

| Couleur | Hex | Nom | Usage | Émotion |
|---------|-----|-----|-------|---------|
| Primaire | #______ | | | |
| Secondaire | #______ | | | |
| Accent | #______ | | | |
| Neutre 1 | #______ | | | |
| Neutre 2 | #______ | | | |

### Phase 3 : Composition (20 min)

**3.1 Structure du moodboard**

```
┌─────────────────────────────────┐
│         HERO IMAGE              │
├────────┬────────┬────────┬──────┤
│ IMG 1  │ IMG 2  │ IMG 3  │ PAL  │
├────────┴────────┼────────┼──────┤
│    TEXTURES     │ IMG 4  │ TYPO │
├─────────────────┼────────┼──────┤
│     KEYWORDS    │ IMG 5  │ IMG6 │
└─────────────────┴────────┴──────┘
```

**3.2 Hiérarchie visuelle**

Organisez par importance :
1. Élément focal : ________________
2. Support niveau 2 : ________________
3. Détails niveau 3 : ________________

### Phase 4 : Présentation (10 min)

**4.1 Titre et description**

```
Titre : ________________________________
Tagline : ________________________________
Description (50 mots) : ________________________________
```

**4.2 Justification créative**

Pour chaque élément, expliquez :

| Élément | Pourquoi | Message véhiculé |
|---------|----------|------------------|
| Hero | | |
| Palette | | |
| Textures | | |
| Typography | | |

### Grille d'évaluation

| Critère | Score | Commentaires |
|---------|-------|--------------|
| Cohérence | /20 | |
| Originalité | /20 | |
| Pertinence | /20 | |
| Qualité technique | /20 | |
| Impact émotionnel | /20 | |
| **TOTAL** | **/100** | |

---

## 🎨 Exercice 5 : Challenge intégration multi-outils
**Durée : 120 minutes**

### Objectif
Créer une campagne publicitaire complète en combinant tous les outils.

### Mission : Campagne "Back to School" pour une marque de papeterie

### Phase 1 : Stratégie avec Gemini (20 min)

**Brief initial pour Gemini :**
```
Crée une stratégie de campagne "Back to School" pour une papeterie premium :
- 3 concepts créatifs différents
- Messages clés pour chaque concept
- Canaux de diffusion
- KPIs suggérés
```

**Concept retenu :** ________________________________

### Phase 2 : Création visuelle Midjourney (30 min)

**Générez pour le concept retenu :**

1. **Visual hero** (affiche principale)
2. **Série de 3 produits**
3. **Scène lifestyle**
4. **Pattern décoratif**
5. **Éléments graphiques**

Documentez vos prompts gagnants :
```
1. ________________________________
2. ________________________________
3. ________________________________
4. ________________________________
5. ________________________________
```

### Phase 3 : Refinement Adobe (40 min)

**Dans Photoshop/Firefly :**

1. **Composition affiche A3**
   - [ ] Import des visuels Midjourney
   - [ ] Generative Fill pour ajustements
   - [ ] Ajout du texte et logo
   - [ ] Export haute résolution

2. **Bannière web animée**
   - [ ] Adaptation format 728x90
   - [ ] 3 frames d'animation
   - [ ] Export GIF/HTML5

3. **Post réseaux sociaux**
   - [ ] Format carré Instagram
   - [ ] Format story
   - [ ] Cover Facebook

### Phase 4 : Copywriting avec ChatGPT/Claude (15 min)

Générez :
1. **Headline principal** : ________________
2. **Tagline** : ________________
3. **Body copy** (50 mots) : ________________
4. **CTA** : ________________
5. **Hashtags** (10) : ________________

### Phase 5 : Présentation finale (15 min)

**Mockups de présentation :**
- [ ] Affiche en situation urbaine
- [ ] Site web avec bannière
- [ ] Feed Instagram
- [ ] Email marketing

### Deliverables checklist

- [ ] Stratégie documentée (1 page)
- [ ] Affiche principale (A3, 300dpi)
- [ ] Bannière web (3 formats)
- [ ] Posts sociaux (5 minimum)
- [ ] Copy complet
- [ ] Mockups de présentation
- [ ] Guide d'utilisation des visuels

### Évaluation 360°

| Aspect | Note | Justification |
|--------|------|---------------|
| Créativité | /25 | |
| Cohérence | /25 | |
| Exécution technique | /25 | |
| Potentiel commercial | /25 | |
| **TOTAL** | **/100** | |

---

## 📝 Projet final : Portfolio créatif IA
**À rendre avant le Module 4**

### Objectif
Constituer un portfolio de 10 créations IA professionnelles.

### Structure du portfolio

#### Section 1 : Projets commerciaux (4 créations)
1. **Branding complet**
   - Logo variations
   - Palette et typo
   - Applications

2. **Campagne publicitaire**
   - 3 visuels cohérents
   - Déclinaisons formats

3. **Packaging produit**
   - Vue 3D
   - Flat design
   - Mockup contextuel

4. **Design web**
   - Homepage
   - Components UI
   - Illustrations custom

#### Section 2 : Explorations artistiques (3 créations)
1. **Série conceptuelle**
2. **Expérimentation de style**
3. **Projet personnel**

#### Section 3 : Cas d'étude détaillé (3 créations)

Pour UN projet, documentez :
- Brief initial
- Process créatif (prompts, iterations)
- Décisions et pivots
- Résultat final
- Apprentissages

### Format de présentation

```
Pour chaque création :

TITRE : [Nom du projet]
CLIENT : [Réel ou fictif]
OUTILS : [Liste des IA utilisées]
TEMPS : [Durée de création]
PROMPT CLÉ : [Le prompt le plus efficace]

[Visuel principal]

CONTEXTE : [2-3 phrases]
DÉFI : [Principal challenge]
SOLUTION : [Approche créative]
RÉSULTAT : [Impact ou feedback]

[Visuels secondaires]

APPRENTISSAGE : [1 point clé retenu]
```

### Critères d'évaluation

| Critère | Points | Vos notes |
|---------|--------|-----------|
| Diversité des styles | 20 | |
| Maîtrise technique | 20 | |
| Originalité | 20 | |
| Présentation | 20 | |
| Documentation | 20 | |
| **TOTAL** | **100** | |

### Bonus créatif (+20 points)

Créez une expérience interactive :
- Site web de portfolio
- Présentation vidéo
- AR/VR showcase
- Installation digitale

---

## 🏆 Défis hebdomadaires

### Semaine 1 : Speed Creation
Créez 1 visuel par jour en moins de 15 minutes

### Semaine 2 : Style Master
Reproduisez 5 styles artistiques célèbres

### Semaine 3 : Constraint Challenge
Créez avec des limitations (ex: 2 couleurs max)

### Semaine 4 : Collaboration
Projet en équipe utilisant tous les outils

---

## 💡 Ressources et inspiration

### Prompts de démarrage testés

**Pour Midjourney :**
```
"[subject], golden ratio composition, 
rule of thirds, leading lines, 
depth of field, cinematic lighting, 
8k resolution, hyperrealistic details --ar 16:9 --v 6 --q 2"
```

**Pour Adobe Firefly :**
```
"Professional product photography style, 
clean minimal background, 
soft box lighting, 
subtle shadows, 
commercial quality"
```

### Combinaisons de styles gagnantes

1. **Cinématique** : "cinematic + anamorphic + film grain"
2. **Éditorial** : "editorial + minimalist + high contrast"
3. **Luxe** : "luxury + gold accents + elegant typography"
4. **Tech** : "futuristic + holographic + neon accents"
5. **Organique** : "organic shapes + earth tones + natural textures"

### Workflow optimisé

```
1. Idéation (Gemini) : 10 min
2. Exploration (Midjourney) : 20 min
3. Sélection : 5 min
4. Refinement (Adobe) : 20 min
5. Finalisation : 10 min
Total : 65 min par projet
```