# Module 7 : Ressources visuelles - IA pour Comptables

---

## Schémas et infographies

### 1. Workflow comptable augmenté par l'IA

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PROCESSUS COMPTABLE AVEC IA                       │
└─────────────────────────────────────────────────────────────────────┘

    ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
    │ COLLECTE │ ──── │ SAISIE   │ ──── │ CONTRÔLE │ ──── │ ANALYSE  │
    │          │      │          │      │          │      │          │
    └──────────┘      └──────────┘      └──────────┘      └──────────┘
         │                 │                 │                 │
         ▼                 ▼                 ▼                 ▼
    ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
    │ OCR +    │      │ Auto-    │      │ Détection│      │ Rapports │
    │ Dext     │      │ catégo-  │      │ anomalies│      │ IA       │
    │          │      │ risation │      │          │      │          │
    └──────────┘      └──────────┘      └──────────┘      └──────────┘
    
    ⏱️ -80%          ⏱️ -70%          ⏱️ -60%          ⏱️ -50%
    temps             temps             temps             temps
```

---

### 2. Matrice des outils IA par usage comptable

```
                        COMPLEXITÉ DE LA TÂCHE
                    Simple ◄─────────────────► Complexe
                    
    F   │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
    R   │  │    DEXT     │    │  PENNYLANE  │    │   CLAUDE    │
    É   │  │  Capture    │    │  Compta IA  │    │  Analyse    │
    Q H │  │  factures   │    │  intégrée   │    │  complexe   │
    U a │  └─────────────┘    └─────────────┘    └─────────────┘
    E u │
    N t │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
    C e │  │   EXCEL     │    │   COPILOT   │    │  CHATGPT    │
    E   │  │  + formules │    │  Microsoft  │    │  Rédaction  │
      B │  │   simples   │    │   365       │    │  rapports   │
      a │  └─────────────┘    └─────────────┘    └─────────────┘
      s │
```

---

### 3. Arbre de décision : Quel outil IA utiliser ?

```
                          ┌─────────────────┐
                          │ Quelle tâche ?  │
                          └────────┬────────┘
                                   │
           ┌───────────────────────┼───────────────────────┐
           │                       │                       │
           ▼                       ▼                       ▼
    ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
    │   Capture    │       │   Analyse    │       │   Rédaction  │
    │   documents  │       │   données    │       │   documents  │
    └──────┬───────┘       └──────┬───────┘       └──────┬───────┘
           │                      │                      │
           ▼                      │                      ▼
    ┌──────────────┐              │               ┌──────────────┐
    │    DEXT      │              │               │   ChatGPT    │
    │   ou Indy    │              │               │   ou Claude  │
    └──────────────┘              │               └──────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
             ┌──────────────┐           ┌──────────────┐
             │    Excel     │           │    Gros      │
             │   Copilot    │           │   volumes    │
             │   (données   │           │   (Claude/   │
             │   tabulaires)│           │   ChatGPT)   │
             └──────────────┘           └──────────────┘
```

---

### 4. Pyramide des compétences IA pour comptables

```
                           /\
                          /  \
                         /    \
                        / STRA \
                       / TÉGIE  \
                      /  IA      \
                     /────────────\
                    /   ANALYSE    \
                   /   AVANCÉE      \
                  /   (Prévisions,   \
                 /    Optimisation)   \
                /──────────────────────\
               /    AUTOMATISATION      \
              /    (Workflows, Macros,   \
             /     Prompts avancés)       \
            /──────────────────────────────\
           /        UTILISATION BASIQUE     \
          /    (Prompts simples, Capture,    \
         /           Catégorisation)          \
        /──────────────────────────────────────\
```

---

### 5. Checklist de conformité RGPD pour l'IA

```
┌────────────────────────────────────────────────────────────────┐
│              CHECKLIST RGPD - USAGE IA EN CABINET              │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  □  Anonymiser les données avant saisie dans l'IA             │
│     ├── Remplacer noms par "Client A", "Client B"             │
│     ├── Masquer les numéros SIRET/SIREN                       │
│     └── Supprimer adresses et contacts                        │
│                                                                │
│  □  Utiliser des outils conformes                             │
│     ├── ChatGPT Team/Enterprise (pas la version gratuite)     │
│     ├── Claude Pro avec données non utilisées pour training   │
│     └── Copilot Microsoft 365 (données restent dans tenant)   │
│                                                                │
│  □  Documenter l'usage                                        │
│     ├── Registre des traitements IA                           │
│     ├── Information des clients (lettre de mission)           │
│     └── Process de vérification humaine                       │
│                                                                │
│  □  Former les collaborateurs                                 │
│     ├── Bonnes pratiques de saisie                           │
│     ├── Données interdites (RIB, mots de passe, etc.)        │
│     └── Signalement des incidents                             │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

### 6. Comparatif des assistants IA pour comptables

```
┌─────────────────┬────────────┬────────────┬────────────┬────────────┐
│                 │  ChatGPT   │   Claude   │  Copilot   │   Gemini   │
│                 │   (GPT-4)  │   (3.5)    │  (M365)    │   (2.0)    │
├─────────────────┼────────────┼────────────┼────────────┼────────────┤
│ Calculs         │    ★★★★☆   │   ★★★★★    │   ★★★★☆    │   ★★★★☆    │
│ complexes       │            │            │            │            │
├─────────────────┼────────────┼────────────┼────────────┼────────────┤
│ Analyse         │    ★★★★☆   │   ★★★★★    │   ★★★☆☆    │   ★★★★☆    │
│ documents       │            │            │            │            │
├─────────────────┼────────────┼────────────┼────────────┼────────────┤
│ Intégration     │    ★★☆☆☆   │   ★★☆☆☆    │   ★★★★★    │   ★★★☆☆    │
│ Office          │            │            │            │            │
├─────────────────┼────────────┼────────────┼────────────┼────────────┤
│ Rédaction       │    ★★★★★   │   ★★★★★    │   ★★★★☆    │   ★★★★☆    │
│ professionnelle │            │            │            │            │
├─────────────────┼────────────┼────────────┼────────────┼────────────┤
│ Confidentialité │    ★★★☆☆   │   ★★★★☆    │   ★★★★★    │   ★★★☆☆    │
│ données         │  (Team+)   │   (Pro)    │  (tenant)  │            │
├─────────────────┼────────────┼────────────┼────────────┼────────────┤
│ Prix/mois       │   20-25€   │   18-20€   │   12-22€   │   Gratuit+ │
└─────────────────┴────────────┴────────────┴────────────┴────────────┘
```

---

### 7. Timeline d'adoption de l'IA en cabinet

```
        MOIS 1              MOIS 2-3            MOIS 4-6           MOIS 7+
    ┌───────────┐       ┌───────────┐       ┌───────────┐      ┌───────────┐
    │DÉCOUVERTE │       │ ADOPTION  │       │OPTIMISATION      │INTÉGRATION│
    │           │       │           │       │           │      │  TOTALE   │
    │• Tests    │──────▶│• Usage    │──────▶│• Prompts  │─────▶│• IA dans  │
    │  outils   │       │  quotidien│       │  avancés  │      │  tous les │
    │• Formation│       │• Premiers │       │• Workflows│      │  process  │
    │  équipe   │       │  gains    │       │  auto     │      │• ROI      │
    │           │       │           │       │           │      │  mesuré   │
    └───────────┘       └───────────┘       └───────────┘      └───────────┘
    
    Investissement:      Gains temps:        Gains temps:       Gains temps:
    Formation 8h        15-20%              30-40%             50%+
```

---

### 8. Carte mentale : Applications IA en comptabilité

```
                              ┌─────────────────┐
                              │   IA POUR       │
                              │   COMPTABLES    │
                              └────────┬────────┘
                                       │
        ┌──────────────┬───────────────┼───────────────┬──────────────┐
        │              │               │               │              │
        ▼              ▼               ▼               ▼              ▼
   ┌─────────┐   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
   │ SAISIE  │   │ ANALYSE │    │RÉDACTION│    │ CONSEIL │    │ VEILLE  │
   └────┬────┘   └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘
        │             │              │              │              │
   ┌────┴────┐   ┌────┴────┐   ┌────┴────┐   ┌────┴────┐   ┌────┴────┐
   │• OCR    │   │• Bilans │   │• Notes  │   │• Optim. │   │• Lois   │
   │• Catégo.│   │• Ratios │   │• Lettres│   │  fiscale│   │• Juris. │
   │• Rappro.│   │• Prévis.│   │• Rapports   │• Simul. │   │• Actus  │
   └─────────┘   └─────────┘   └─────────┘   └─────────┘   └─────────┘
```

---

### 9. Exemple de tableau de bord IA

```
┌────────────────────────────────────────────────────────────────────────┐
│                     TABLEAU DE BORD - CABINET IA                       │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   TEMPS GAGNÉ CE MOIS                    TÂCHES AUTOMATISÉES           │
│   ┌─────────────────────┐               ┌─────────────────────┐        │
│   │  ████████████░░░░   │  47h          │  Saisie      ████░  │  82%   │
│   │  Objectif: 60h      │               │  Rapproch.   ███░░  │  65%   │
│   └─────────────────────┘               │  Rapports    ██░░░  │  45%   │
│                                         │  Analyse     █░░░░  │  30%   │
│   PROMPTS UTILISÉS                      └─────────────────────┘        │
│   ┌─────────────────────┐                                              │
│   │  Cette semaine: 156 │               SATISFACTION ÉQUIPE            │
│   │  ▲ +23% vs sem-1    │               ┌─────────────────────┐        │
│   └─────────────────────┘               │  ★★★★☆  4.2/5       │        │
│                                         │  "Gain de temps     │        │
│   TOP 3 USAGES                          │   significatif"     │        │
│   1. Catégorisation (45%)               └─────────────────────┘        │
│   2. Rédaction notes (30%)                                             │
│   3. Calculs fiscaux (25%)                                             │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

### 10. Fiche mémo : Structure d'un bon prompt comptable

```
┌────────────────────────────────────────────────────────────────────────┐
│                    STRUCTURE DU PROMPT PARFAIT                         │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  1️⃣  RÔLE                                                              │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ "Tu es un expert-comptable français inscrit à l'Ordre..."       │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  2️⃣  CONTEXTE                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ "Mon client est une SARL soumise à l'IS, CA 500K€, secteur..."  │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  3️⃣  TÂCHE PRÉCISE                                                     │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ "Analyse ce bilan et identifie les 3 principaux risques..."     │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  4️⃣  FORMAT SOUHAITÉ                                                   │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ "Présente ta réponse sous forme de tableau avec colonnes..."    │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
│  5️⃣  CONTRAINTES                                                       │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │ "Cite les articles du CGI pertinents. Maximum 500 mots."        │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Liens vers ressources externes

### Vidéos recommandées
- Ordre des Experts-Comptables - Webinaires IA
- Pennylane Academy - Tutoriels
- LinkedIn Learning - IA pour la finance

### Outils à tester
- [Dext](https://dext.com) - Essai gratuit 14 jours
- [Pennylane](https://pennylane.com) - Démo disponible
- [Claude](https://claude.ai) - Version Pro recommandée

---

*Ressources créées par Antoine AP - Formation IA & Transformation Digitale*
*Dernière mise à jour : Janvier 2025*
