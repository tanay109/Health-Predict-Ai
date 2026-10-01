# 💼 Business Requirement Document (BRD)
## **Health Predict AI — Intelligent Multi-Symptom Diagnostic System**

---

### **Document Control**
| Property | Value |
| :--- | :--- |
| **Project / Initiative** | **Health Predict AI** |
| **Document Classification** | **Business Requirement Document (BRD)** |
| **Document Version** | **v1.0 (Final Academic & Business Baseline)** |
| **Business Owner & Author** | **Prateek Shukla** (Roll No: **2400320100828**) |
| **Academic Department** | Department of Computer Science & Engineering |
| **Course & Specialization** | B.Tech 3rd Year Capstone / Systems Engineering |
| **Effective Date** | October 2026 |

---

## 1. Executive Summary

Healthcare systems globally face severe strain due to inefficient preliminary triage, delayed chronic condition diagnosis, and non-emergency overcrowding in urgent care clinics. Patients frequently attempt self-diagnosis via standard search engines—a practice that often leads to health anxiety ("cyberchondria") or dangerous complacency.

**Health Predict AI** addresses this systemic healthcare inefficiency by introducing an automated, non-invasive, AI-assisted business solution. By leveraging probabilistic machine learning (Multinomial Naive Bayes), the system matches **132 validated patient symptoms** against **41 medical conditions** in under **50 milliseconds**, requiring **zero numeric lab measurements**. 

This initiative optimizes preliminary patient routing, provides structured 4-step medical protocols, and delivers high societal and business ROI by curbing avoidable emergency room visits and improving early disease detection rates.

---

## 2. Business Objectives & Strategic Alignment

### 2.1 Strategic Drivers
1. **Universal Healthcare Accessibility:** Deliver preliminary clinical screening to individuals regardless of geographical or financial barriers, accessible on standard mobile and desktop browsers.
2. **Operational Efficiency in Primary Care:** Streamline clinic waiting lines by allowing patients and triage nurses to pre-screen symptoms and prioritize consultations based on emergency severity tiers.
3. **Reduction of Unnecessary Clinical Visits:** Guide patients with self-limiting conditions (e.g., Common Cold, Acid Reflux) toward home-care protocols, conserving hospital resources for acute emergencies (e.g., Heart Attacks, Malaria).

### 2.2 S.M.A.R.T. Business Goals

| Goal Dimension | Specific Target Metric | Timeline |
| :--- | :--- | :--- |
| **Diagnostic Latency** | Complete preliminary probability evaluation in **< 50ms**. | Immediate (v1.0 Baseline) |
| **Zero Numeric Friction** | **0% dependency** on clinical lab numbers (blood pressure, BMI, glucose). | Immediate (v1.0 Baseline) |
| **Algorithmic Reliability**| Maintain **100% benchmark consistency** on standard clinical symptom datasets. | Immediate (v1.0 Baseline) |
| **Triage Time Reduction**| Reduce patient symptom-intake consultation time by **40%**. | Q1 2027 |
| **Deployment Cost** | Leverage a **100% open-source software stack** with $0 licensing overhead. | Continuous |

---

## 3. Gap Analysis: Current State (AS-IS) vs. Future State (TO-BE)

```
+─────────────────────────────────────────+      +─────────────────────────────────────────+
|         CURRENT STATE (AS-IS)           |      |          FUTURE STATE (TO-BE)           |
|                                         |      |                                         |
| 1. Google / Web Search Triage           |      | 1. Health Predict AI Triage Engine      |
|    • Unranked, terrifying search hits   |      |    • Ranked probabilistic match spectrum|
|    • Extreme health anxiety             |      |    • Clear clinical interpretations     |
|                                         |      |                                         |
| 2. Numeric Health Apps                  |      | 2. Pure Symptom-Driven Interface        |
|    • Demands BP (mmHg), Glucose, BMI    | ===> |    • Zero lab hardware required         |
|    • High barrier to entry              |      |    • 132 searchable clinical symptoms   |
|                                         |      |                                         |
| 3. Unregulated Clinic Arrivals          |      | 3. Structured Care Protocols            |
|    • Non-emergencies clog ER waiting    |      |    • Explicit urgency classifications   |
|    • Delayed acute emergency care       |      |    • Actionable 4-step medical protocols|
+─────────────────────────────────────────+      +─────────────────────────────────────────+
```

---

## 4. Stakeholder Analysis & RACI Matrix

### 4.1 Stakeholder Profiles
- **General Public / Patients:** Individuals seeking non-intimidating, instant symptom assessments.
- **Triage Healthcare Professionals:** Community health workers and nurses requiring rapid multi-symptom pattern verification before physician escalation.
- **Academic Evaluators / Supervisors:** Departmental faculty assessing architectural scalability, algorithmic soundess, and project viability.
- **Business & System Owner (Prateek Shukla):** Oversees end-to-end design, implementation, testing, and continuous deployment.

### 4.2 RACI Governance Matrix
*(R = Responsible, A = Accountable, C = Consulted, I = Informed)*

| Project Deliverable / Function | Patient (End User) | Triage Nurse | Project Lead (Prateek Shukla) | Academic Guide / HOD |
| :--- | :---: | :---: | :---: | :---: |
| **Business Requirements Formulation** | C | C | **R / A** | I |
| **Dataset Ingestion & Model Training** | I | I | **R / A** | C |
| **UI/UX Glassmorphic Design** | C | I | **R / A** | I |
| **Clinical Protocol Verification** | I | C | **R** | **A** |
| **System Testing & Sign-Off** | I | I | **R** | **A** |

---

## 5. High-Level Business Rules & Requirements

| Rule ID | Business Rule Title | Description & Regulatory Policy |
| :---: | :--- | :--- |
| **BR-01** | **Zero Laboratory Hardware Barrier** | The system must never reject or block a user due to absent physical lab parameters (e.g. mmHg, BMI). All decisions must evaluate pure physical/somatic symptoms. |
| **BR-02** | **Mandatory Medical Disclaimer** | The interface must prominently display a persistent disclaimer indicating that the AI is an educational decision-support tool, not a licensed medical prescription. |
| **BR-03** | **Emergency Escalation Protocol** | When symptoms indicate acute critical conditions (e.g. Heart Attack, Severe Pneumonia), the system must highlight emergency contact badges (112 / 911). |
| **BR-04** | **Data Privacy & Zero PII Logging** | In compliance with healthcare privacy principles, user sessions must not record patient names, emails, or personal identification in persistent databases. |
| **BR-05** | **Algorithmic Objectivity** | Models must be trained using mathematical smoothing (Laplace smoothing) to eliminate bias on single-symptom queries. |

---

## 6. Cost-Benefit Analysis & Return on Investment (ROI)

### 6.1 Cost Breakdown (Capital & Operational Expenditure)

| Expense Item | Traditional Commercial Triage Suite | Health Predict AI Implementation |
| :--- | :---: | :---: |
| **Software Licensing (SaaS)** | $12,000 – $35,000 / year | **$0.00** (Open-Source Python, Scikit-Learn) |
| **Client Device Terminals** | Specialized Medical Tablets ($3,000) | **$0.00** (Compatible with existing browsers) |
| **Hosting & Compute Infrastructure** | High-end Cloud GPUs ($250 / month) | **$0.00** (Local CPU execution / Free tier) |
| **User Onboarding & Training** | Formal Clinical Training Sessions | **Zero Friction** (Self-explanatory UI) |
| **Total Estimated First-Year Cost** | **$18,000+** | **$0.00 (Self-Contained Academic Project)** |

### 6.2 Tangible & Intangible Business Benefits
- **Tangible Benefits:**
  - 100% reduction in software licensing expenditures.
  - Sub-50ms inference throughput supporting rapid client query handling.
- **Intangible Benefits:**
  - **Diminished Anxiety:** Prevents misdirected panic through clear clinical descriptions and probability spectrums.
  - **Empowerment:** Equips patients with informed questions and precautions prior to doctor appointments.
  - **Educational Value:** Serves as a modular, reproducible engineering template for 3rd-year university curricula.

---

## 7. Business Process Workflow (BPMN)

```
[ START: Patient Experiences Symptoms ]
                  │
                  ▼
[ Step 1: Portal Access ] ──> Opens Health Predict AI (Localhost / Web)
                  │
                  ▼
[ Step 2: Symptom Input ] ──> Selects symptoms via Autocomplete OR Preset Scenarios
                  │
                  ▼
[ Step 3: Automated Validation ] 
   ├── Is at least 1 symptom selected?
   │     ├── NO  ──> Display Warning: "Select at least one symptom"
   │     └── YES ──> Trigger Machine Learning Inference Engine
                  │
                  ▼
[ Step 4: Diagnostic Processing ] ──> Vectorize 132 features ──> Multinomial NB ──> Generate Probabilities
                  │
                  ▼
[ Step 5: Clinical Dossier Delivery ]
   ├── Displays Primary Disease & Confidence Score
   ├── Highlights Triggering Biomarkers (✓ Symptom Tags)
   ├── Presents 4-Step Medical Precautions
   └── Displays Alternative Differential Diagnoses Spectrum
                  │
                  ▼
[ Step 6: Patient Action ] 
   ├── Mild/Moderate ──> Follows home precautions, schedules routine clinic visit
   └── High/Emergency ──> Calls emergency services (112 / 911) or visits nearest ER
                  │
                  ▼
[ END: Informed Clinical Outcome ]
```

---

## 8. Risk, Assumption, Issue & Dependency (RAID) Analysis

| Risk ID | Risk Description | Likelihood | Impact | Mitigation Strategy |
| :---: | :--- | :---: | :---: | :--- |
| **R-01** | **User Misinterprets Guidance as Prescription** | Low | High | Prominently display persistent statutory medical disclaimers on every result dossier. |
| **R-02** | **Sparse Input False Positive** | Very Low | Medium | Replaced Decision Trees with **Multinomial Naive Bayes** to eliminate zero-vector bias. |
| **R-03** | **Network / Offline Usage Constraint** | Low | Low | System functions 100% offline with locally cached `.pkl` model binaries. |
| **R-04** | **Browser Incompatibility** | Very Low | Low | Verified cross-browser performance on Chromium, Gecko, and WebKit rendering engines. |

---

## 9. Success Criteria & Project Sign-Off

The business initiative is deemed successful upon fulfilling the following milestones:
- [x] Zero numerical laboratory parameters required from users.
- [x] Sub-50ms diagnostic latency achieved.
- [x] 100% benchmark consistency on standard 4,920-patient clinical dataset.
- [x] Responsive glassmorphic dark interface verified on mobile and desktop viewports.
- [x] Comprehensive documentation delivered (SRS, PRD, and BRD).

---

### **Executive Approval & Formal Sign-Off**

| Signatory Role | Name & Title | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Project Lead & Author** | **Prateek Shukla** (Roll No: **2400320100828**) | ______________________ | 01-Oct-2026 |
| **Academic Supervisor** | **Prof. / Dr. [Supervisor Name]** | ______________________ | 01-Oct-2026 |
| **Department Head** | **Head of Department (HOD - CSE)** | ______________________ | 01-Oct-2026 |
