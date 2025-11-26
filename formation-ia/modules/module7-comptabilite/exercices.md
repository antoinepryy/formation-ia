# Module 7 : Exercices pratiques - IA pour Comptables

---

## Exercice 1 : Catégorisation automatique de factures

### Objectif
Apprendre à utiliser l'IA pour catégoriser automatiquement des pièces comptables.

### Consignes

1. Utilisez ChatGPT ou Claude avec le prompt suivant :

```
Tu es un expert-comptable français spécialisé en PME. 
Pour chaque facture que je te présente, indique :
- Le compte de charge PCG (6xxxxx)
- Le compte de TVA déductible
- La nature de la dépense
- Si déductible du résultat fiscal (oui/non et pourquoi)

Réponds sous forme de tableau.
```

2. Testez avec ces 5 factures :

| # | Description |
|---|-------------|
| 1 | Facture Amazon : Cartouches d'encre - 89,90€ TTC |
| 2 | Facture restaurant : Déjeuner client - 127,50€ TTC |
| 3 | Facture Orange : Abonnement téléphone pro - 45€ HT |
| 4 | Facture garage : Réparation véhicule société - 890€ TTC |
| 5 | Facture avocat : Conseil juridique création filiale - 2 400€ HT |

### Résultat attendu
Un tableau complet avec la catégorisation correcte selon le PCG.

### Critères de réussite
- Comptes corrects à 80%
- TVA bien identifiée
- Justification de la déductibilité fiscale

---

## Exercice 2 : Analyse d'écarts de rapprochement bancaire

### Objectif
Utiliser l'IA pour diagnostiquer des écarts de rapprochement.

### Consignes

Utilisez ce prompt avec les données ci-dessous :

```
Je suis comptable et j'ai un écart de rapprochement bancaire inexpliqué.

Solde relevé bancaire au 31/12 : 45 678,23€
Solde comptable (512) au 31/12 : 47 234,56€
Écart : -1 556,33€

Opérations en rapprochement :
- Chèque n°125 émis le 28/12 non débité : 2 340,00€
- Virement client reçu le 31/12 non comptabilisé : 890,00€
- Frais bancaires décembre non comptabilisés : 45,67€

Calcule si ces éléments expliquent l'écart. 
Si non, propose des hypothèses pour l'écart résiduel.
```

### Questions
1. L'écart est-il entièrement expliqué ?
2. Quelles vérifications supplémentaires proposer ?
3. Quelles écritures de régularisation passer ?

---

## Exercice 3 : Rédaction d'une note de synthèse mensuelle

### Objectif
Générer un rapport de gestion clair pour un dirigeant non-comptable.

### Données du cas

```
Société : DURAND MENUISERIE SARL
Activité : Fabrication de meubles sur mesure
Effectif : 8 salariés

Données octobre 2024 :
- CA HT : 87 500€ (octobre 2023 : 72 300€)
- Achats matières : 31 200€
- Masse salariale : 28 400€
- Charges externes : 12 800€
- Trésorerie fin de mois : 23 450€
- Encours clients : 67 800€ (dont 12 400€ > 60 jours)
```

### Consignes

1. Créez un prompt pour générer une note de synthèse incluant :
   - Analyse du CA et de la marge
   - Points positifs
   - Points d'alerte
   - Recommandations concrètes

2. La note doit être compréhensible par un non-comptable

3. Maximum 1 page

### Critères d'évaluation
- Clarté du langage
- Pertinence des analyses
- Qualité des recommandations

---

## Exercice 4 : Détection d'anomalies dans un grand livre

### Objectif
Identifier des écritures suspectes ou des erreurs potentielles.

### Données

```
Extrait du compte 625 - Déplacements et réceptions (2024) :

Date       | Libellé                      | Montant
-----------|------------------------------|----------
15/01      | Restaurant Le Gourmet        | 89,50€
22/01      | SNCF Paris-Lyon             | 156,00€
03/02      | Carrefour                    | 234,67€
18/02      | Hôtel Mercure Lyon          | 189,00€
05/03      | Amazon - Livre management    | 29,90€
12/03      | Restaurant équipe            | 567,00€
28/03      | Péage autoroute             | 23,40€
15/04      | Apple Store                  | 1 299,00€
22/04      | Station Total               | 78,50€
30/04      | Restaurant client VIP        | 890,00€
```

### Consignes

1. Demandez à l'IA d'analyser ce compte et d'identifier :
   - Les écritures potentiellement mal imputées
   - Les montants inhabituels
   - Les libellés à clarifier

2. Pour chaque anomalie, proposez :
   - Le compte correct si mauvaise imputation
   - Les questions à poser au client
   - Les risques fiscaux éventuels

---

## Exercice 5 : Simulation d'optimisation fiscale

### Objectif
Utiliser l'IA pour comparer différents scénarios fiscaux.

### Cas pratique

```
Situation :
- EURL à l'IS
- Résultat avant IS et rémunération gérant : 120 000€
- Gérant majoritaire, marié, 2 enfants
- Pas d'autre revenu du foyer

Scénarios à comparer :
A) Rémunération gérant : 60 000€ / Reste en société
B) Rémunération gérant : 80 000€ / Reste en société
C) Rémunération gérant : 40 000€ + Dividendes : 30 000€
```

### Consignes

1. Créez un prompt demandant à l'IA de calculer pour chaque scénario :
   - Charges sociales du gérant
   - IS de la société
   - IR du foyer fiscal
   - Coût global (charges + IS + IR)
   - Net disponible pour le dirigeant

2. Demandez une recommandation argumentée

### Points d'attention
- Vérifiez les calculs de l'IA
- Tenez compte du PFU sur dividendes
- Considérez l'impact retraite

---

## Exercice 6 : Préparation d'un contrôle fiscal

### Objectif
Anticiper les questions d'un vérificateur et préparer les justificatifs.

### Contexte

```
Votre client (restaurant) fait l'objet d'un contrôle fiscal sur N-1 et N-2.

Éléments du dossier :
- CA en hausse de 40% entre N-2 et N-1
- Marge brute passée de 68% à 72%
- Coulage déclaré : 3% du CA
- Ratio masse salariale/CA : 32%
- Nombreux paiements en espèces
```

### Consignes

1. Demandez à l'IA d'identifier les points que le vérificateur va probablement examiner

2. Pour chaque point sensible, préparez :
   - Les justificatifs à rassembler
   - Les explications à fournir
   - Les ratios du secteur pour comparaison

3. Créez une checklist de préparation au contrôle

---

## Exercice 7 : Analyse d'un dossier de reprise d'entreprise

### Objectif
Produire une analyse financière synthétique pour un repreneur.

### Données (simplifiées)

```
Société cible : IMPRIM'EXPRESS SAS
Activité : Imprimerie numérique
Effectif : 12 personnes

Bilans simplifiés (K€) :
                    N-2     N-1     N
CA                  890     920     875
EBE                 78      82      45
Résultat net        42      48      12
Capitaux propres    180     210     205
Dettes financières  120     95      85
Trésorerie          45      52      28
BFR                 95      110     125
```

### Consignes

1. Faites analyser ces données par l'IA en demandant :
   - Évolution de la rentabilité
   - Analyse de la structure financière
   - Points de vigilance pour un repreneur
   - Valorisation indicative (multiples EBE et CA)

2. Rédigez une note de synthèse de 2 pages maximum

3. Listez les informations complémentaires à demander

---

## Exercice 8 : Création d'un prompt réutilisable

### Objectif
Développer un "super prompt" pour votre usage quotidien.

### Consignes

Créez un prompt structuré incluant :

1. **Contexte permanent** : votre rôle, le cadre réglementaire français

2. **Instructions de format** : tableaux, langue, niveau de détail

3. **Garde-fous** : rappel des limites, demande de vérification humaine

4. **Template de réponse** : structure attendue

### Exemple de structure

```
[CONTEXTE]
Tu es un assistant pour expert-comptable français...

[RÈGLES]
- Toujours citer les articles de loi/CGI pertinents
- Signaler quand une vérification humaine est nécessaire
- ...

[FORMAT DE RÉPONSE]
1. Synthèse (3 lignes max)
2. Analyse détaillée
3. Recommandations
4. Points de vigilance

[MA QUESTION]
{question}
```

---

## Grille d'auto-évaluation

Pour chaque exercice, évaluez-vous :

| Critère | 1 | 2 | 3 | 4 |
|---------|---|---|---|---|
| Qualité du prompt rédigé | Basique | Correct | Bon | Excellent |
| Pertinence de l'analyse IA | Faible | Moyenne | Bonne | Très bonne |
| Vérification des résultats | Non faite | Partielle | Complète | Avec corrections |
| Application métier | Théorique | Partiellement applicable | Applicable | Immédiatement utilisable |

**Objectif : Score moyen ≥ 3 sur tous les exercices**

---

## Conseils pour réussir

1. **Soyez précis** dans vos prompts : contexte + demande claire + format souhaité

2. **Itérez** : si la première réponse n'est pas satisfaisante, affinez votre demande

3. **Vérifiez toujours** les calculs et les références réglementaires

4. **Adaptez** les prompts à votre pratique et vos clients

5. **Documentez** vos meilleurs prompts pour les réutiliser

---

*Exercices créés par Antoine AP - Formation IA & Transformation Digitale*
*Dernière mise à jour : Janvier 2025*
