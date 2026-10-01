# 📋 Product Requirement Document (PRD)
## **Health Predict AI — Intelligent Multi-Symptom Diagnostic System**

---

### **Document Control**
| Property | Value |
| :--- | :--- |
| **Product Name** | **Health Predict AI** |
| **Product Version** | **v2.4 (Production Baseline)** |
| **Document Status** | **Approved / Active** |
| **Product Owner & Author** | **Prateek Shukla** (Roll No: **2400320100828**) |
| **Department** | Computer Science & Engineering |
| **Academic Context** | B.Tech 3rd Year Capstone / System Design Specification |
| **Date of Publication** | October 2026 |

---

## 1. Executive Summary & Product Vision

### 1.1 Executive Summary
**Health Predict AI** is a lightweight, non-invasive, AI-assisted symptom triage application designed to bridge the gap between initial symptom onset and clinical medical consultation. By correlating **132 clinical biomarkers and physical sensations** with **41 validated disease classifications**, the application delivers real-time probabilistic diagnosis, emergency severity ratings, matched biomarker insights, and actionable medical precautions within **< 50 milliseconds**.

### 1.2 Product Vision
> *"To provide every individual with immediate, accessible, and scientifically sound preliminary healthcare intelligence—demystifying personal health without the intimidation of complex laboratory numbers or ambiguous search-engine results."*

---

## 2. Problem Statement & Market Opportunity

### 2.1 The Problem
1. **Google Self-Diagnosis Trap ("Cyberchondria"):** Searching vague symptoms on traditional search engines often surfaces worst-case conditions (e.g., mistaking tension headaches for brain tumors), causing severe patient anxiety.
2. **The Numeric Metric Barrier:** Most digital health prediction tools require patients to enter specific clinical laboratory numbers (e.g., Blood Pressure in mmHg, BMI, Fasting Glucose, Cholesterol). Everyday users do not possess home blood analyzers or BP monitors.
3. **Emergency Room & Clinic Overcrowding:** Triage delays and patient panic lead to hospital congestion for self-limiting or mild conditions (e.g., Common Cold, Acid Reflux), while severe acute conditions (e.g., Heart Attack, Dengue) often suffer delayed intervention.

### 2.2 The Solution
A purely **symptom-driven**, autocomplete-enabled diagnostic engine that:
- Requires **zero clinical laboratory numbers**.
- Evaluates full multi-symptom patterns simultaneously using **Multinomial Naive Bayes (MNB)**.
- Explains **why** a disease was predicted by highlighting triggering biomarkers.
- Categorizes conditions into actionable urgency tiers (Mild, Moderate, High, Emergency).

---

## 3. Target User Personas & User Stories

### 3.1 User Personas

```
+-----------------------------------------------------------------------------------+
| PERSONA 1: The General Citizen (Primary User)                                     |
| • Name: Rahul (Age 28, IT Professional)                                           |
| • Context: Experiencing sudden cold hands/feet, unexplained fatigue, and sluggishness. |
| • Pain Point: Unsure whether to visit an emergency room, clinic, or wait it out.   |
| • Goal: Quick, zero-friction guidance on what conditions could cause these signs. |
+-----------------------------------------------------------------------------------+
| PERSONA 2: The Triage Healthcare Worker / Nurse                                   |
| • Name: Sister Mary (Age 36, Community Clinic Nurse)                              |
| • Context: Screening rural patients in high-throughput preliminary queues.        |
| • Pain Point: Needs rapid differential screening before sending for blood work.   |
| • Goal: Explore alternative matching diagnoses to prioritize doctor consultations.|
+-----------------------------------------------------------------------------------+
```

### 3.2 Core User Stories
- **US-01 (Symptom Search):** *As a user feeling unwell, I want to type keywords (e.g., "fever", "chest pain", "acidity") and select my symptoms from an intuitive search dropdown so that I don't have to scroll through hundreds of medical terms.*
- **US-02 (Diagnostic Dossier):** *As a user, I want to receive an immediate diagnosis with an explicit confidence score so that I understand the likelihood of the assessment.*
- **US-03 (Biomarker Matching):** *As a user, I want to see which of my specific symptoms triggered the result so that I can verify the AI understood my condition.*
- **US-04 (Medical Protocol):** *As a patient, I want 4 concrete medical precautions and next steps so that I know what actions to take before seeing a physician.*
- **US-05 (Differential Diagnoses):** *As a healthcare triage worker, I want to view a ranked spectrum of secondary probable conditions to prevent diagnostic blind spots.*

---

## 4. Product Goals & Key Performance Indicators (KPIs)

| Metric Category | Key Performance Indicator (KPI) | Target Baseline |
| :--- | :--- | :--- |
| **Diagnostic Latency** | Time taken from button click to dossier display | **< 50 milliseconds** |
| **Algorithm Accuracy** | Categorical accuracy on clinical validation matrices | **100.0% Benchmark** |
| **Symptom Coverage** | Breadth of indexed physiological biomarkers | **132 Symptoms** |
| **Pathology Coverage** | Diversity of supported conditions across ICD domains | **41 Conditions** |
| **System Uptime** | Availability during university and live demo sessions | **≥ 99.5% Uptime** |
| **Zero Numeric Hassle** | Percentage of features requiring blood/lab hardware | **0% (Pure Symptoms)** |

---

## 5. Feature Requirements & MoSCoW Prioritization

### 5.1 MoSCoW Feature Matrix

| Priority | Feature ID | Feature Name | Description & Acceptance Criteria |
| :---: | :---: | :--- | :--- |
| **Must-Have** | **FEAT-01** | Multi-Select Autocomplete Search | Search bar with type-ahead filtering across all 132 indexed symptoms; supports multiple selections. |
| **Must-Have** | **FEAT-02** | Multinomial Naive Bayes Inference | Probability calculation $P(\text{Disease} \mid \text{Symptoms})$ with Laplace smoothing to prevent sparse zero-vector bias. |
| **Must-Have** | **FEAT-03** | Triggering Biomarker Correlation | Identifies and displays user symptoms matching the condition's clinical symptom profile. |
| **Must-Have** | **FEAT-04** | Actionable Protocol & Precautions | Generates pathology descriptions and 4 distinct, medically vetted next-step protocols. |
| **Should-Have**| **FEAT-05** | One-Click Clinical Presets | Quick buttons for common scenarios (*Cold Extremities, Cardiac Distress, Malaria, Acid Reflux*). |
| **Should-Have**| **FEAT-06** | Differential Diagnoses Spectrum | Visual probability progress bars for top-4 alternative matching conditions. |
| **Should-Have**| **FEAT-07** | Glassmorphic Dark UI | Custom CSS theme with frosted glass containers, glowing beacons, and keyframe animations. |
| **Could-Have** | **FEAT-08** | Multi-Language Support | Localized Hindi and regional Indian language support for rural triage accessibility. |
| **Could-Have** | **FEAT-09** | Exportable PDF Clinical Dossier | One-click download of the generated diagnosis card for physician hand-off. |
| **Won't-Have**  | **FEAT-10** | E-Pharmacy Drug Dispensation | Automated medicine ordering (excluded for medical ethics and safety compliance). |

---

## 6. User Journey & Workflow Architecture

```
[ STEP 1: LANDING & DISCOVERY ]
User enters Health Predict AI portal.
Sees KPI metrics (41 Pathologies, 132 Biomarkers) and Live Status Beacon.
                     │
                     ▼
[ STEP 2: SYMPTOM INGESTION ]
User either:
  (A) Types keywords in the searchable dropdown (e.g., "Cold hands", "Fatigue", "Weight gain")
  (B) Clicks a 1-Click Quick Scenario (e.g., "🧊 Cold Hands & Feet")
Active symptoms appear as royal blue chips with a live counter.
                     │
                     ▼
[ STEP 3: EXECUTION & INFERENCE ]
User clicks "✨ Execute Clinical Diagnostic Engine".
Input is vectorized into a 132-element binary array (0/1).
Multinomial Naive Bayes calculates posterior probability spectrum across 41 classes.
Turnaround time: < 35ms.
                     │
                     ▼
[ STEP 4: DIAGNOSTIC DOSSIER RENDERING ]
App presents the Frosted Glass Dossier:
  • Primary Disease Classification (e.g., Hypothyroidism)
  • Severity Rating (🟡 Moderate) & Confidence Score (99.7%)
  • Matched Biomarker badges (✓ Cold Hands And Feets, ✓ Fatigue, ✓ Weight Gain)
  • 📖 Clinical Interpretation (Pathological summary)
  • 🛡️ Doctor-Recommended 4-Step Protocol (Endocrinologist, TSH test, Diet, Medication)
  • 📊 Differential Diagnosis Spectrum (Alternative condition probabilities)
```

---

## 7. UX / UI Design Specifications

### 7.1 Visual Design Tokens
- **Background Architecture:** Radial midnight gradient (`radial-gradient(circle at 50% -15%, #0f2347 0%, #080d1a 50%, #030712 100%)`).
- **Cards & Containers:** Frosted glassmorphism (`background: rgba(15, 23, 42, 0.70)`, `backdrop-filter: blur(18px)`, border `rgba(56, 189, 248, 0.25)`).
- **Primary Accent:** Electric Cyan (`#38bdf8`) & Royal Medical Blue (`#2563eb`).
- **Typography:** `Plus Jakarta Sans`, modern clean sans-serif with high contrast and legible line heights.
- **Animations:** Subtle keyframe transitions (`fadeInSlide 0.5s`, `pulseBeacon 2s`).

### 7.2 UI Wireframe Specification

```
+---------------------------------------------------------------------------------------+
|                               HEALTH PREDICT AI PORTAL                                |
+---------------------------------------------------------------------------------------+
|  [●] CLINICAL INTELLIGENCE ENGINE v2.4                                                |
|  HEALTH PREDICT AI                                                                    |
|  Multi-symptom pattern matching engine correlating 132 markers with 41 pathologies    |
|                                                                                       |
|  [ 41 CONDITIONS ]             [ 132 BIOMARKERS ]             [ 100% ACCURACY ]       |
|                                                                                       |
|  ⚡ QUICK TEST SCENARIOS:                                                             |
|  [ Cold Hands & Feet ]   [ Malaria / Fever ]   [ Cardiac Distress ]   [ Acid Reflux ] |
|                                                                                       |
|  🔍 PATIENT SYMPTOMS:                                                                 |
|  [ Type to search symptoms...                                                       ] |
|  Selected: [✓ Cold Hands And Feets] [✓ Fatigue] [✓ Weight Gain]                       |
|                                                                                       |
|  [                     ✨ EXECUTE CLINICAL DIAGNOSTIC ENGINE                         ] |
|                                                                                       |
|  +─────────────────────────────────────────────────────────────────────────────────+  |
|  │ AI DIAGNOSTIC DOSSIER                                   CONFIDENCE: 99.7%       │  |
|  │ Hypothyroidism                                          Severity: 🟡 Moderate   │  |
|  │ Triggering Biomarkers: [✓ Cold Hands And Feets] [✓ Fatigue] [✓ Weight Gain]     │  |
|  │ 📖 Clinical Interpretation: An underactive thyroid gland slowing metabolism...  │  |
|  │ 🛡️ Recommended Protocol: (1) Endocrinologist (2) Thyroid Profile (3) Diet       │  |
|  │ 📊 Differential Diagnoses: Hypoglycemia (0.2%) | Chronic Fatigue (0.1%)         │  |
|  +─────────────────────────────────────────────────────────────────────────────────+  |
+---------------------------------------------------------------------------------------+
```

---

## 8. Technical Architecture & Tech Stack

```
+─────────────────────────────────────────────────────────────+
|                    PRESENTATION LAYER                       |
|  • Streamlit Reactive UI (Port 8501)                        |
|  • Glassmorphic CSS Engine & BaseWeb Components             |
+──────────────────────────────┬──────────────────────────────+
                               │ WebSockets / HTTP
+──────────────────────────────▼──────────────────────────────+
|                    APPLICATION LAYER                        |
|  • Python 3.10+ Runtime Environment                         |
|  • Binary Feature Vectorizer (132-element Encoder)          |
|  • Biomarker Mapping & Correlation Subsystem                |
+──────────────────────────────┬──────────────────────────────+
                               │ In-Memory Binary Interface
+──────────────────────────────▼──────────────────────────────+
|                    MODEL & DATA LAYER                       |
|  • Multinomial Naive Bayes Classifier (symptom_model.pkl)   |
|  • Feature Schema Dictionary (symptoms_list.pkl)            |
|  • Clinical Pathology Knowledge Base (disease_symptoms_map) |
+─────────────────────────────────────────────────────────────+
```

### 8.1 Technology Components
- **Language:** Python 3.10+
- **Data Engineering:** Pandas 2.0+, NumPy 1.24+
- **Machine Learning Engine:** Scikit-Learn 1.3+
- **Frontend Framework:** Streamlit 1.35+
- **Serialization & Caching:** Joblib with `@st.cache_resource`

---

## 9. Risk Analysis, Ethical Safeguards & Medical Disclaimer

### 9.1 Risk Assessment

| Risk Description | Severity | Probability | Mitigation Strategy |
| :--- | :---: | :---: | :--- |
| **False Reassurance / Over-Reliance** | High | Low | Prominently display persistent medical disclaimers on every diagnostic card. |
| **Rare Condition Misclassification** | Medium | Low | Integrate Differential Diagnosis spectrum showing all alternative probabilities > 2%. |
| **Sparse Input Anomaly** | Medium | Very Low | Migrated from Decision Trees to **Multinomial Naive Bayes** to prevent random leaf bias on 1-symptom inputs. |
| **Patient Privacy Violation** | Critical | None | **Zero PII collection.** All inference executed in volatile RAM; no database logging of patient identities. |

### 9.2 Statutory Medical Disclaimer
> **MANDATORY NOTICE:** Health Predict AI is an educational, technological decision-support prototype. It does not constitute medical advice, a definitive clinical diagnosis, or a certified treatment plan. Users experiencing acute distress, chest pain, difficulty breathing, or severe trauma must contact emergency health services (**112 / 911**) immediately.

---

## 10. Product Roadmap & Future Enhancements

```
+───────────────────────+   +───────────────────────+   +───────────────────────+
|      PHASE 1: MVP     |   |   PHASE 2: ENHANCED   |   |   PHASE 3: ENTERPRISE |
|   (Current Baseline)  |   |      (Q1 2027)        |   |       (Q3 2027)       |
+───────────────────────+   +───────────────────────+   +───────────────────────+
| • 132 Symptoms Engine |   | • Voice Symptom Input |   | • Telemedicine Booking|
| • 41 Disease MNB Model|   | • Multi-Language UI   |   | • Electronic Health   |
| • Glassmorphic Dark UI|   | • PDF Report Export   |   |   Record (EHR) Export |
| • Zero-Numeric Input  |   | • Severity Alerts API |   | • Wearable Sensor Sync|
+───────────────────────+   +───────────────────────+   +───────────────────────+
```

---

## 11. Sign-Off & Project Approval

| Role | Name & Title | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Product Author & Developer** | **Prateek Shukla** (Roll No: 2400320100828) | ______________________ | 01-Oct-2026 |
| **Project Guide / Supervisor** | **Prof. / Dr. [Supervisor Name]** | ______________________ | 01-Oct-2026 |
| **Academic Department Head** | **Head of Department (HOD - CSE)** | ______________________ | 01-Oct-2026 |
