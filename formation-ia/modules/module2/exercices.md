# Module 2 : Exercices pratiques - Prompt Engineering

## 🎯 Exercice 1 : Maîtriser la structure CROFT
**Durée : 45 minutes**

### Objectif
Apprendre à structurer des prompts selon la méthode CROFT (Contexte, Rôle, Objectif, Format, Tonalité).

### Partie A : Analyse de prompts (15 min)

Analysez ces prompts et identifiez les éléments CROFT manquants :

**Prompt 1 :**
"Écris quelque chose sur les voitures électriques"

Éléments présents : ___________
Éléments manquants : ___________

**Prompt 2 :**
"Tu es un journaliste. Fais un article."

Éléments présents : ___________
Éléments manquants : ___________

**Prompt 3 :**
"Analyse les ventes du trimestre et dis-moi ce qui ne va pas. Sois honnête."

Éléments présents : ___________
Éléments manquants : ___________

### Partie B : Construction guidée (15 min)

Complétez ce template pour créer un prompt optimisé :

**Scénario :** Vous devez créer une présentation commerciale

**C**ontexte : _________________________________
(Exemple : Entreprise, secteur, produit, situation actuelle)

**R**ôle : _________________________________
(Exemple : Expert en vente B2B avec 10 ans d'expérience)

**O**bjectif : _________________________________
(Exemple : Créer une présentation qui convertit 30% des prospects)

**F**ormat : _________________________________
(Exemple : 10 slides avec structure spécifique)

**T**onalité : _________________________________
(Exemple : Professionnelle mais accessible)

**Prompt final assemblé :**
_________________________________

### Partie C : Création libre (15 min)

Créez 3 prompts CROFT complets pour ces situations :

1. **Situation :** Rédaction d'un email de réclamation
   - Votre prompt : ___________

2. **Situation :** Création d'un plan de formation
   - Votre prompt : ___________

3. **Situation :** Analyse concurrentielle
   - Votre prompt : ___________

### Grille d'auto-évaluation

| Critère | Prompt 1 | Prompt 2 | Prompt 3 |
|---------|----------|----------|----------|
| Contexte clair | ☐ | ☐ | ☐ |
| Rôle défini | ☐ | ☐ | ☐ |
| Objectif précis | ☐ | ☐ | ☐ |
| Format structuré | ☐ | ☐ | ☐ |
| Tonalité adaptée | ☐ | ☐ | ☐ |

---

## 🎯 Exercice 2 : Laboratoire de techniques avancées
**Durée : 60 minutes**

### Objectif
Expérimenter et comparer différentes techniques de prompting.

### Setup
Choisissez un sujet unique pour tous les tests : _____________
(Exemple : "Lancement d'un nouveau produit cosmétique bio")

### Test 1 : Zero-Shot vs Few-Shot (15 min)

**Zero-Shot (sans exemple) :**
```
Prompt : [Créez votre prompt sans donner d'exemple]
_________________________________

Résultat obtenu :
_________________________________

Score qualité (1-10) : ___
```

**Few-Shot (avec exemples) :**
```
Prompt : [Même demande mais avec 2-3 exemples]
_________________________________

Résultat obtenu :
_________________________________

Score qualité (1-10) : ___
```

**Analyse :** Quelle différence observez-vous ?
_________________________________

### Test 2 : Chain-of-Thought (15 min)

**Sans CoT :**
```
"Calcule le ROI d'une campagne marketing de 50 000€ qui a généré 
200 nouveaux clients avec un panier moyen de 500€"

Résultat : _________________________________
```

**Avec CoT :**
```
"Calcule le ROI d'une campagne marketing étape par étape :
1. Investissement : 50 000€
2. Nouveaux clients : 200
3. Panier moyen : 500€

Montre chaque calcul :
- D'abord, calcule le revenu total
- Ensuite, calcule le profit
- Enfin, calcule le ROI en pourcentage"

Résultat : _________________________________
```

**Comparaison :**
- Clarté : ___/10 vs ___/10
- Précision : ___/10 vs ___/10
- Utilité : ___/10 vs ___/10

### Test 3 : Contraintes négatives (15 min)

Créez deux versions d'un même prompt :

**Version 1 (sans contraintes négatives) :**
"Écris une description de produit pour [VOTRE SUJET]"

**Version 2 (avec contraintes négatives) :**
"Écris une description de produit pour [VOTRE SUJET]
NE PAS :
- Utiliser de clichés marketing
- Dépasser 100 mots
- Mentionner le prix
- Utiliser de superlatifs"

**Comparez les résultats :**

| Aspect | Version 1 | Version 2 |
|--------|-----------|-----------|
| Originalité | ___/10 | ___/10 |
| Précision | ___/10 | ___/10 |
| Pertinence | ___/10 | ___/10 |
| Professionnalisme | ___/10 | ___/10 |

### Test 4 : Itération progressive (15 min)

Partez d'un prompt basique et améliorez-le en 4 itérations :

**Itération 1 (basique) :**
Prompt : _________________________________
Résultat : _________________________________
Note : ___/10

**Itération 2 (+ contexte) :**
Prompt : _________________________________
Résultat : _________________________________
Note : ___/10

**Itération 3 (+ structure) :**
Prompt : _________________________________
Résultat : _________________________________
Note : ___/10

**Itération 4 (+ contraintes) :**
Prompt : _________________________________
Résultat : _________________________________
Note : ___/10

**Courbe de progression :**
```
10 |    ___[I4]
 8 |  ___[I3]
 6 |___[I2]
 4 [I1]
 2 |
 0 |____________
   I1  I2  I3  I4
```

---

## 🎯 Exercice 3 : Création de templates métier
**Durée : 45 minutes**

### Objectif
Développer une bibliothèque de prompts réutilisables pour votre activité.

### Template 1 : Génération de contenu

**Nom du template :** _________________________________

**Variables à définir :**
- {{SUJET}} : _________________________________
- {{AUDIENCE}} : _________________________________
- {{OBJECTIF}} : _________________________________
- {{TONALITE}} : _________________________________
- {{LONGUEUR}} : _________________________________

**Structure du prompt :**
```
Tu es un expert en création de contenu spécialisé dans {{DOMAINE}}.

Contexte : {{CONTEXTE}}

Crée un(e) {{TYPE_CONTENU}} sur {{SUJET}} pour {{AUDIENCE}}.

Objectif : {{OBJECTIF}}

Structure :
1. {{SECTION_1}}
2. {{SECTION_2}}
3. {{SECTION_3}}

Contraintes :
- Ton : {{TONALITE}}
- Longueur : {{LONGUEUR}}
- Inclure : {{ELEMENTS_OBLIGATOIRES}}
- Éviter : {{ELEMENTS_INTERDITS}}

Format de sortie :
{{FORMAT_SPECIFIQUE}}
```

**Test du template :**
Remplissez les variables et testez : _________________________________

### Template 2 : Analyse et rapport

**Créez votre propre template pour l'analyse :**

```
[VOTRE TEMPLATE ICI]
_________________________________
_________________________________
_________________________________
```

### Template 3 : Résolution de problème

**Créez votre propre template pour la résolution :**

```
[VOTRE TEMPLATE ICI]
_________________________________
_________________________________
_________________________________
```

### Documentation de vos templates

Pour chaque template, complétez :

| Template | Cas d'usage | Fréquence | Efficacité | Améliorations |
|----------|-------------|-----------|------------|---------------|
| 1 | | | /10 | |
| 2 | | | /10 | |
| 3 | | | /10 | |

---

## 🎯 Exercice 4 : Challenge - Prompt Battle
**Durée : 30 minutes**

### Objectif
Créer le prompt le plus efficace pour des tâches complexes.

### Round 1 : Créativité (10 min)

**Défi :** Générer 10 idées de noms pour une startup

**Contraintes :**
- Secteur : GreenTech
- Cible : B2B
- Valeurs : Innovation, durabilité, simplicité

**Votre prompt :**
_________________________________

**Évaluation des résultats :**
- Originalité : ___/10
- Pertinence : ___/10
- Mémorabilité : ___/10

### Round 2 : Précision technique (10 min)

**Défi :** Expliquer la blockchain à 3 audiences différentes

**Audiences :**
1. Un enfant de 10 ans
2. Un directeur financier
3. Une grand-mère

**Votre prompt :**
_________________________________

**Évaluation :**
- Adaptation audience 1 : ___/10
- Adaptation audience 2 : ___/10
- Adaptation audience 3 : ___/10

### Round 3 : Efficacité commerciale (10 min)

**Défi :** Transformer des caractéristiques en bénéfices

**Produit :** Montre connectée avec :
- Autonomie 7 jours
- Étanche 50m
- ECG intégré
- Écran AMOLED

**Votre prompt :**
_________________________________

**Évaluation :**
- Persuasion : ___/10
- Émotion : ___/10
- Clarté : ___/10

### Score final : ___/90

---

## 🎯 Exercice 5 : Debugging et optimisation
**Durée : 40 minutes**

### Objectif
Diagnostiquer et corriger des prompts problématiques.

### Cas 1 : Réponse trop générique (10 min)

**Prompt défaillant :**
"Donne-moi des conseils pour améliorer mon entreprise"

**Symptômes observés :**
- [ ] Manque de spécificité
- [ ] Absence de contexte
- [ ] Pas d'objectif clair
- [ ] Format non défini

**Votre correction :**
_________________________________

**Test de la correction :**
- Amélioration spécificité : ____%
- Amélioration pertinence : ____%

### Cas 2 : Hallucinations fréquentes (10 min)

**Prompt défaillant :**
"Raconte-moi l'histoire détaillée de l'entreprise XYZ fondée en 2023 et ses 50 produits innovants"

**Problèmes identifiés :**
_________________________________

**Stratégies de correction :**
1. _________________________________
2. _________________________________
3. _________________________________

**Prompt corrigé :**
_________________________________

### Cas 3 : Format non respecté (10 min)

**Prompt défaillant :**
"Fais-moi un rapport sur les ventes avec intro résumé analyse tableau recommandations conclusion tout ça bien structuré professionnel"

**Reformulation structurée :**
```
[VOTRE VERSION CORRIGÉE]
_________________________________
```

### Cas 4 : Ton inapproprié (10 min)

**Situation :** Email de relance client premium
**Prompt défaillant :**
"Écris un email pour rappeler au client qu'il doit payer"

**Analyse du problème :**
- Ton actuel : _________________________________
- Ton souhaité : _________________________________
- Éléments manquants : _________________________________

**Prompt optimisé :**
_________________________________

---

## 🎯 Exercice 6 : Projet intégré - Création d'une campagne complète
**Durée : 90 minutes**

### Objectif
Utiliser le prompt engineering pour créer tous les éléments d'une campagne marketing.

### Brief client

**Entreprise :** EcoTech Solutions
**Produit :** Application mobile de suivi d'empreinte carbone
**Cible :** Entreprises de 50-500 employés
**Objectif :** Générer 100 demos qualifiées en 30 jours
**Budget :** 15 000€
**Canaux :** LinkedIn, Email, Webinar

### Phase 1 : Stratégie (20 min)

**Prompt pour stratégie :**
```
[Créez votre prompt pour obtenir une stratégie complète]
_________________________________
```

**Output obtenu :**
_________________________________

### Phase 2 : Création de contenu (40 min)

**2.1 Posts LinkedIn (10 min)**
Prompt : _________________________________
Résultat : _________________________________

**2.2 Séquence email (10 min)**
Prompt : _________________________________
Résultat : _________________________________

**2.3 Landing page (10 min)**
Prompt : _________________________________
Résultat : _________________________________

**2.4 Script webinar (10 min)**
Prompt : _________________________________
Résultat : _________________________________

### Phase 3 : Analyse et optimisation (20 min)

**Prompt pour analyse SWOT :**
_________________________________

**Prompt pour KPIs à suivre :**
_________________________________

**Prompt pour plan de contingence :**
_________________________________

### Phase 4 : Présentation finale (10 min)

**Prompt pour executive summary :**
```
Synthétise cette campagne en format suivant :
- Objectif (1 phrase)
- Stratégie (3 bullets)
- Livrables (5 éléments)
- KPIs (3 métriques)
- Budget (répartition)
- Timeline (4 étapes)
- Risques et mitigation (2 points)
```

### Évaluation finale

| Critère | Score | Commentaires |
|---------|-------|--------------|
| Cohérence stratégique | /20 | |
| Qualité du contenu | /20 | |
| Originalité | /20 | |
| Faisabilité | /20 | |
| ROI potentiel | /20 | |
| **Total** | **/100** | |

---

## 📝 Devoir : Constitution de votre "Prompt Book"
**À rendre avant le Module 3**

### Instructions

Créez votre guide personnel de prompts comprenant :

### Section 1 : Prompts quotidiens
10 prompts que vous utilisez régulièrement, documentés ainsi :

```
PROMPT #1
Nom : [Titre descriptif]
Fréquence : [Quotidien/Hebdo/Mensuel]
Contexte : [Quand l'utiliser]
Prompt : [Le prompt complet]
Variables : [Parties à personnaliser]
Exemple : [Un cas d'usage réel]
ROI : [Temps gagné]
```

### Section 2 : Prompts complexes
5 prompts multi-étapes pour tâches complexes :

```
WORKFLOW #1
Nom : [Titre]
Durée totale : [Estimation]
Étapes :
  1. Prompt : [...]
     Output attendu : [...]
  2. Prompt : [...]
     Output attendu : [...]
  3. Prompt : [...]
     Output attendu : [...]
Résultat final : [...]
```

### Section 3 : Prompts d'urgence
3 prompts pour situations critiques :
- Gestion de crise
- Réponse urgente client
- Résolution rapide problème

### Section 4 : Métriques et apprentissages

**Tableau de suivi :**

| Semaine | Prompts créés | Prompts utilisés | Temps gagné | Qualité moyenne |
|---------|---------------|------------------|-------------|-----------------|
| S1 | | | | /10 |
| S2 | | | | /10 |

**Top 3 apprentissages :**
1. _________________________________
2. _________________________________
3. _________________________________

**Évolutions prévues :**
_________________________________

---

## 🏆 Bonus : Certification Prompt Engineer

### Test de certification (30 questions)

Pour valider votre maîtrise, répondez à ces questions :

**Niveau 1 : Fondamentaux (10 questions)**
1. Qu'est-ce que la "température" dans un LLM ?
2. Différence entre zero-shot et few-shot ?
3. [...]

**Niveau 2 : Techniques (10 questions)**
1. Comment éviter les hallucinations ?
2. Qu'est-ce que le chain-of-thought ?
3. [...]

**Niveau 3 : Application (10 questions)**
1. Créez un prompt pour [situation]
2. Optimisez ce prompt : [...]
3. [...]

**Score requis :** 24/30 pour certification

### Badge de compétences

Débloquez des badges en complétant :

🏅 **Prompt Rookie** : 10 prompts créés
🏅 **Prompt Explorer** : 50 prompts testés
🏅 **Prompt Master** : 100 prompts optimisés
🏅 **Prompt Ninja** : 1000+ tokens économisés
🏅 **Prompt Sensei** : Formation d'autres personnes

---

## 💡 Tips de pro

### Les 10 commandements du Prompt Engineer

1. **Tu contextualiseras** toujours tes demandes
2. **Tu définiras** un rôle clair à l'IA
3. **Tu structureras** tes prompts lisiblement
4. **Tu donneras** des exemples quand nécessaire
5. **Tu préciseras** le format de sortie attendu
6. **Tu itéreras** pour améliorer les résultats
7. **Tu testeras** avant de déployer
8. **Tu documenteras** tes prompts efficaces
9. **Tu mesureras** l'impact de tes optimisations
10. **Tu partageras** tes découvertes avec l'équipe

### Raccourcis et astuces

**Pour gagner du temps :**
- Créez des snippets de prompts fréquents
- Utilisez des variables {{}} pour personnalisation rapide
- Gardez un fichier de prompts "qui marchent"
- Automatisez avec des outils comme Zapier + GPT

**Pour améliorer la qualité :**
- Toujours faire 3 versions et comparer
- Demander à l'IA d'évaluer sa propre réponse
- Utiliser "Agis comme si tu étais [expert]"
- Terminer par "Si tu as des questions, demande"

---

## 📚 Ressources pour approfondir

### Outils recommandés
- **Promptperfect.ai** : Optimisation automatique
- **FlowGPT** : Partage de prompts communautaires
- **PromptBase** : Marketplace de prompts
- **Anthropic Workbench** : Test de prompts Claude

### Lectures essentielles
- "The Prompt Engineering Guide" - DAIR.AI
- "Best Practices for Prompt Engineering" - OpenAI
- Documentation Anthropic sur le prompting

### Prochaines étapes
1. Pratiquer quotidiennement (minimum 3 prompts/jour)
2. Tenir un journal de prompts
3. Rejoindre une communauté de prompt engineers
4. Expérimenter avec différents modèles IA