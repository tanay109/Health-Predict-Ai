# DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
### [NAME OF INSTITUTE / UNIVERSITY, CITY]

---

# SOFTWARE REQUIREMENTS SPECIFICATION (SRS)
## **Health Predict AI — Intelligent Multi-Symptom Disease Prediction System**

**Standard Academic Compliance:** IEEE Std 830-1998  
**Academic Degree:** Bachelor of Technology (B.Tech in Computer Science & Engineering)  
**Academic Year:** 2026 – 2027  
**Document Status:** 3rd Year Project Specification  
**Date of Submission:** October 2026  

---

### **Submission & Approval Credentials**

| Submitted By (Project Team) | Under the Guidance Of |
| :--- | :--- |
| **Prateek Shukla** (Roll No: **2400320100828**)<br><br>**Degree:** B.Tech (Computer Science & Engineering)<br>**Academic Year:** 2026 – 2027 | **Prof. / Dr. [Supervisor Name]**<br>[Designation / Title]<br>Department of Computer Science & Engineering<br><br>**Review Panel:** Internal Academic Committee<br>**Department:** Computer Science & Engineering |

---

### **Document Revision & Approval History**

| Version | Date | Description / Major Changes | Prepared By | Reviewed By |
| :---: | :---: | :--- | :---: | :---: |
| **0.1** | 15-Sep-2026 | Initial Problem Formulation, Scope Definition & Feasibility Study | Project Team | Project Guide |
| **1.0** | 01-Oct-2026 | Final 3rd Year SRS Baseline: Symptom-Based Naive Bayes Architecture & Glassmorphic UI | Project Team | HOD / Committee |

> **Guidance Note:** This Software Requirements Specification (SRS) conforms strictly to the **IEEE Std 830-1998** recommended practice. All functional modules, external interfaces, non-functional targets, and architectural models are structured for university lab evaluation, departmental project reviews, and system design baselines.

---

## 1. Introduction

### 1.1 Purpose
The purpose of this Software Requirements Specification (SRS) document is to provide a complete, rigorous, and unambiguous definition of the functionality, external interfaces, performance targets, and constraints of **Health Predict AI**. This specification serves as a binding reference agreement between student developers, project evaluators, academic supervisors, and prospective healthcare end-users during the 3rd-year engineering curriculum.

### 1.2 Scope of the System
Health Predict AI is an automated clinical decision-support system designed to solve the critical problem of preliminary healthcare screening by providing immediate, non-invasive, symptom-driven disease diagnosis without requiring patients to enter complex or unavailable numeric laboratory metrics (such as blood pressure in mmHg, fasting glucose, or BMI).

- **In-Scope Capabilities:**
  - Real-time type-ahead search and dynamic selection across **132 validated clinical symptoms**.
  - One-click clinical test scenarios for rapid triage (*Cold Extremities, Cardiac Distress, Malaria, Acid Reflux*).
  - Sparse binary vector transformation and validation mapping.
  - Multi-class probabilistic classification using **Multinomial Naive Bayes (MNB)** across **41 medical conditions**.
  - Triggering biomarker identification and correlation verification.
  - Automated generation of plain-English pathology explanations and structured **4-step medical protocols**.
  - Differential diagnoses probability spectrum visualization rendered on a glassmorphic Streamlit interface.
- **Out-of-Scope Boundaries:**
  - Hardware fabrication beyond standard client compute peripherals.
  - Direct prescription drug dispensing without licensed physician authorization.
  - Invasive surgical robotics control or hospital billing ERP integration.
- **Expected Benefits:**
  - Instantaneous diagnostic triage (< 50 milliseconds).
  - Complete elimination of mathematical and lab testing burden on lay users.
  - Guidance of patients to appropriate care urgency tiers (reducing non-emergency ER congestion).
  - 100.0% benchmark consistency on clinical validation data.

### 1.3 Definitions, Acronyms, and Abbreviations

| Category | Term / Acronym | Definition / Standard Context |
| :--- | :--- | :--- |
| **Standard** | **SRS** | Software Requirements Specification (IEEE Std 830-1998 format). |
| **Machine Learning** | **MNB** | Multinomial Naive Bayes classification algorithm with Laplace smoothing. |
| **Architecture** | **API / Framework** | Streamlit reactive component model communicating via WebSockets. |
| **Data Structure** | **Binary Feature Vector** | 132-element sparse binary array encoding presence (1) or absence (0) of symptoms. |
| **UI/UX Pattern** | **Glassmorphism** | Modern UI styling utilizing CSS backdrop-filter blur, ambient depth, and subtle neon borders. |
| **Clinical Domain** | **Biomarkers & Pathology**| 132 physiological signs mapped to 41 distinct ICD-relevant medical disease categories. |

### 1.4 References
1. **IEEE Std 830-1998:** *IEEE Recommended Practice for Software Requirements Specifications.*
2. **Software Engineering (10th Edition):** *Ian Sommerville, Pearson Education.*
3. **Columbia University / Kaggle:** *Disease Symptom Prediction Benchmark Dataset (4,920 patient instances, 132 symptoms, 41 classes).*
4. **Scikit-Learn:** *Machine Learning in Python*, Pedregosa et al., JMLR 12, pp. 2825-2830.
5. **Streamlit:** *The fastest way to build and share data apps*, Official Documentation and BaseWeb Architecture Manual.

### 1.5 Document Overview
The remainder of this SRS is partitioned into structural sections:
- **Section 2:** Product perspective, target user classes, operating environment, and implementation constraints.
- **Section 3:** Detailed functional requirements organized into three core software modules.
- **Section 4:** External interface requirements (UI wireframe, hardware, software, and communication).
- **Section 5:** Non-functional attributes (Performance, Accuracy, Reliability, and Portability).
- **Section 6:** Standard academic modeling diagrams (Use Case, DFD, Sequence, and Schema).
- **Section 7:** Academic review and formal departmental sign-off table.

---

## 2. Overall Description

### 2.1 Product Perspective
Health Predict AI operates as an autonomous, self-contained multi-tier healthcare application. It comprises:
1. **Presentation Tier:** Streamlit reactive glassmorphic UI executed in any standard modern web browser.
2. **Inference & Application Tier:** Python execution runtime hosting the Scikit-Learn Multinomial Naive Bayes engine.
3. **Model & Knowledge Base Tier:** Local serialized binary models (`.pkl`) and clinical symptom-disease mapping matrices.

```
+-----------------------------------------------------------------------------------------+
|                       SYSTEM CONTEXT DIAGRAM (DFD LEVEL 0)                              |
+-----------------------------------------------------------------------------------------+

   [ Patient / User ]  
           │ 
           │  1. Selects Symptoms / Triggers Scenario Preset
           ▼ 
   +─────────────────────────────────────────────────────────────+
   │                  HEALTH PREDICT AI SYSTEM                   │
   │                                                             │
   │   • Module 1: Dynamic Symptom Search & Vectorization        │
   │   • Module 2: Multinomial Naive Bayes Inference Engine      │
   │   • Module 3: Biomarker Correlation & Medical Protocol Gen  │
   +─────────────────────────────────────────────────────────────+
           │ 
           │  2. Renders Diagnostic Dossier, Severity, Precautions & Differential Spectrum
           ▼ 
   [ User Interface (Streamlit Glassmorphic View) ]
```

### 2.2 User Classes and Characteristics

| User Role / Persona | Technical Proficiency | Core Responsibilities & Rights |
| :--- | :--- | :--- |
| **General Patient / Public User** | Basic | Searches physical symptoms, selects quick test presets, views predicted disease dossier, reads clinical descriptions, and follows medical precaution protocols. |
| **Medical Practitioner / Triage Nurse** | Intermediate | Reviews triggering biomarker correlations, inspects alternative differential diagnoses spectrum, and cross-references preliminary triage probability before clinical lab ordering. |
| **Academic Supervisor / Evaluator** | High (AI / Software Engg.) | Audits training pipeline (`train.py`), inspects confusion matrix / classification report, validates IEEE 830 compliance, and verifies algorithm stability. |

### 2.3 Operating Environment
- **Client Requirements:** Modern web browser (Google Chrome >= v110, Mozilla Firefox >= v108, Microsoft Edge, Apple Safari); responsive down to 360x640 mobile viewports; JavaScript enabled.
- **Server Runtime Environment:** Python 3.10+ execution runtime; compatible across Windows 10/11, Ubuntu Linux 22.04 LTS, and macOS; Streamlit server listening on TCP Port 8501.
- **Model Storage Tier:** Local memory-cached serialized binary assets (`symptom_model.pkl`, `symptoms_list.pkl`, `disease_symptoms_map.pkl`) loaded with sub-millisecond overhead via `@st.cache_resource`.

### 2.4 Design and Implementation Constraints
1. **Non-Invasive Advisory Constraint:** The software functions exclusively as an advisory clinical decision support system and explicitly displays medical disclaimers.
2. **Offline Execution Capability:** The complete ML model and medical knowledge base are self-contained locally without mandatory external cloud API dependencies.
3. **Algorithmic Selection:** Multinomial Naive Bayes was chosen over Decision Trees to eliminate the sparse zero-vector bias that causes false classifications on single symptoms.
4. **Security & Privacy Compliance:** Zero persistent storage of personal health identification (PHI). Session states exist exclusively in volatile memory during active usage.

### 2.5 Assumptions and Dependencies
- **Assumptions:** Users possess basic device literacy and select at least one genuine observed physical symptom.
- **Dependencies:** Availability of local Python runtime dependencies: `pandas`, `numpy`, `scikit-learn`, `streamlit`, and `joblib`.

---

## 3. System Features and Functional Requirements

### 3.1 Module 1: Symptom Ingestion & Dynamic Search Module

| Req ID | Feature Description | Input / Validation Rule | Priority |
| :---: | :--- | :--- | :---: |
| **FR-1.1** | Searchable Multi-Select Autocomplete | Real-time type-ahead search across 132 validated clinical symptoms | **High** |
| **FR-1.2** | One-Click Clinical Preset Scenarios | Instant state injection for Cold Hands/Feet, Cardiac Distress, Malaria, and Acid Reflux | **Medium** |
| **FR-1.3** | Active Biomarker Tagging & Live Counter | Renders dynamic royal blue badge chips and live counter of selected symptoms | **High** |

### 3.2 Module 2: Machine Learning Inference & Diagnostic Engine

| Req ID | Feature Description | Input / Validation Rule | Priority |
| :---: | :--- | :--- | :---: |
| **FR-2.1** | Binary Vector Transformation | Maps selected symptoms into a 132-element sparse binary feature vector (0/1) | **High** |
| **FR-2.2** | Multinomial Naive Bayes Probabilistic Inference | Calculates posterior probabilities $P(\text{Disease} \mid \text{Symptoms})$ across 41 disease classes | **High** |
| **FR-2.3** | Triggering Biomarker Correlation Verification | Cross-references input symptoms against condition profile to extract genuine matching signs | **High** |

### 3.3 Module 3: Clinical Protocol Reporting, Precautions & Differential Diagnosis

| Req ID | Feature Description | Input / Validation Rule | Priority |
| :---: | :--- | :--- | :---: |
| **FR-3.1** | Executive Diagnostic Dossier Card | Displays primary predicted disease, urgency rating badge, and confidence percentage | **High** |
| **FR-3.2** | Clinical Interpretation & 4-Step Protocol | Presents plain-English pathology explanation and structured doctor-recommended precautions | **High** |
| **FR-3.3** | Differential Diagnoses Probability Spectrum | Visualizes top 4 alternative matching conditions with animated progress bars | **Medium** |

---

## 4. External Interface Requirements

### 4.1 User Interfaces (UI) Wireframe Architecture

```
+-----------------------------------------------------------------------------------------+
|                           USER INTERFACE LAYOUT & WIREFRAME                             |
+-----------------------------------------------------------------------------------------+
|  [●] CLINICAL INTELLIGENCE ENGINE v2.4                                                  |
|  # HEALTH PREDICT AI                                                                    |
|  Multi-symptom pattern matching engine correlating 132 markers with 41 pathologies      |
|                                                                                         |
|  +--------------------+  +--------------------+  +--------------------+                 |
|  |   41 PATHOLOGIES   |  |   132 BIOMARKERS   |  |   100% ACCURACY    |                 |
|  +--------------------+  +--------------------+  +--------------------+                 |
|                                                                                         |
|  ⚡ QUICK TEST SCENARIOS:                                                               |
|  [ Cold Hands & Feet ]  [ Malaria / Fever ]  [ Cardiac Distress ]  [ Digestive / Acid ] |
|                                                                                         |
|  🔍 PATIENT SYMPTOMS:                                                                   |
|  [ Type to search symptoms: e.g. cold hands, fever, joint pain, chest pain...         ] |
|  Active: [✓ Cold Hands And Feets] [✓ Fatigue] [✓ Weight Gain]                           |
|                                                                                         |
|  [  ✨ EXECUTE CLINICAL DIAGNOSTIC ENGINE  ]                                            |
|                                                                                         |
|  +───────────────────────────────────────────────────────────────────────────────────+  |
|  │ AI DIAGNOSTIC DOSSIER                             CONFIDENCE: 99.7%               │  |
|  │ Hypothyroidism                                    Severity: 🟡 Moderate           │  |
|  │ Triggering Biomarkers: [✓ Cold Hands And Feets] [✓ Fatigue] [✓ Weight Gain]       │  |
|  │ 📖 Clinical Interpretation: An underactive thyroid gland slowing metabolism...    │  |
|  │ 🛡️ Recommended Protocol: (1) Endocrinologist (2) Thyroid Profile (3) Diet (4) Med │  |
|  │ 📊 Differential Diagnoses: Hypoglycemia (0.2%) | Chronic Fatigue (0.1%)           │  |
|  +───────────────────────────────────────────────────────────────────────────────────+  |
+-----------------------------------------------------------------------------------------+
```

### 4.2 Hardware Interfaces
- **Standard Deployment:** Any standard desktop, laptop, or tablet with x86_64 or ARM64 processor, $\ge$ 2 GB RAM, and display resolution $\ge$ 720p.

### 4.3 Software Interfaces
- **Operating System:** Windows 10/11, Linux (Ubuntu 20.04+), or macOS.
- **Python Runtime:** Python 3.10 to 3.12.
- **Machine Learning Core:** Scikit-Learn 1.4+ (`MultinomialNB`).
- **Web App Server:** Streamlit 1.35+.
- **Model Storage:** Joblib 1.3+.

### 4.4 Communication Interfaces
- **Local IPC:** WebSockets and HTTP over TCP Port 8501.
- **Network Deployment:** TLS 1.3 / HTTPS over Port 443 with encrypted payload exchange.

---

## 5. Non-Functional Requirements (NFRs)

| Attribute | Target Metric / Standard | Verification & Testing Method |
| :--- | :--- | :--- |
| **5.1 Performance & Latency** | Inference turnaround < 50ms; total page render < 250ms under concurrent requests. | Python execution benchmarking with `time.perf_counter()` and client DevTools audit. |
| **5.2 Accuracy & Consistency** | 100.0% validation benchmark accuracy on clinical symptom training matrix; zero sparse-zero leaf bias. | Stratified test-set evaluation using Scikit-Learn `accuracy_score` and classification matrix. |
| **5.3 Reliability & Availability** | System uptime $\ge$ 99.5% during lab evaluations; graceful validation handling when 0 symptoms are selected. | Stress testing with boundary input vectors and synthetic empty-vector injection. |
| **5.4 Usability & Portability** | Fully responsive across mobile ($\ge$ 360px), tablet, and desktop viewports; cross-browser verified. | Viewport testing on Chrome, Edge, Safari, and Firefox responsive mobile simulators. |

---

## 6. System Design and Analysis Models

| Diagram Type | Objective & Scope | Deliverable Format |
| :--- | :--- | :--- |
| **Use Case Diagram** | Maps user actors (Patient, Triage Nurse, Admin) to discrete functional interactions (Select Symptoms, Run Engine, Inspect Spectrum, Retrain Model). | UML Standard diagram + Actor interaction specification tables. |
| **Data Flow Diagram (DFD)** | Illustrates information flow: Level 0 Context interaction and Level 1 modular data flow between Vectorizer, MNB Model, and Dossier Builder. | Standard Gane-Sarson / Yourdon & Coad notation flow chart. |
| **Feature Matrix Architecture** | Maps 132 binary symptom attributes to 41 target disease classifications with discrete feature indexing. | Tabular feature-label mapping schema. |
| **Sequence Diagram** | Chronological sequence: Client UI $\rightarrow$ State Store $\rightarrow$ Vectorizer $\rightarrow$ MNB Engine $\rightarrow$ Dictionary Matcher $\rightarrow$ UI Dossier View. | UML Sequence diagram detailing execution flow and error recovery. |

---

## 7. Academic Review & Sign-Off

This Software Requirements Specification document has been submitted and reviewed by the academic supervisory panel:

| Project Coordinator / Guide | Internal Examiner | Head of Department (HOD) |
| :---: | :---: | :---: |
| <br><br>__________________________<br>**Signature & Date** | <br><br>__________________________<br>**Signature & Date** | <br><br>__________________________<br>**Signature & Date** |
