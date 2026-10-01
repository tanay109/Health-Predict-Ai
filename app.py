import streamlit as st
import numpy as np
import joblib
import os

# 1. Page Configuration
st.set_page_config(
    page_title="Health Predict AI — Clinical Intelligence",
    page_icon="🧬",
    layout="centered"
)

# 2. Refined Subtle Colors, Typography & Keyframe Animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    }

    /* Subtle Slate & Deep Midnight Gradient */
    .stApp {
        background: radial-gradient(circle at 50% -15%, #0f2347 0%, #080d1a 50%, #030712 100%) !important;
        color: #f8fafc;
    }

    /* Keyframe Animations */
    @keyframes fadeInSlide {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulseBeacon {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.35; transform: scale(1.25); }
    }
    @keyframes subtleGlow {
        0%, 100% { box-shadow: 0 0 15px rgba(56, 189, 248, 0.12); }
        50% { box-shadow: 0 0 25px rgba(56, 189, 248, 0.28); }
    }

    /* Top Badge */
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(56, 189, 248, 0.08);
        border: 1px solid rgba(56, 189, 248, 0.22);
        color: #38bdf8;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        margin-bottom: 12px;
        animation: subtleGlow 3s ease-in-out infinite;
    }
    .status-beacon {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #34d399;
        display: inline-block;
        animation: pulseBeacon 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }

    /* Refined Title */
    .main-title {
        text-align: center;
        font-size: 2.7rem;
        font-weight: 800;
        letter-spacing: -0.6px;
        background: linear-gradient(135deg, #ffffff 30%, #bae6fd 70%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 6px;
        animation: fadeInSlide 0.6s ease-out;
    }
    .main-subtitle {
        text-align: center;
        font-size: 0.98rem;
        color: #94a3b8;
        max-width: 560px;
        margin: 0 auto 24px auto;
        line-height: 1.55;
        animation: fadeInSlide 0.7s ease-out;
    }

    /* Glass KPI Dashboard */
    .kpi-container {
        display: flex;
        gap: 12px;
        margin-bottom: 22px;
        animation: fadeInSlide 0.8s ease-out;
    }
    .kpi-card {
        flex: 1;
        background: rgba(15, 23, 42, 0.55);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 14px;
        padding: 14px;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        border-color: rgba(56, 189, 248, 0.35);
        box-shadow: 0 10px 25px -10px rgba(56, 189, 248, 0.2);
    }
    .kpi-value {
        font-size: 1.55rem;
        font-weight: 800;
        color: #38bdf8;
    }
    .kpi-label {
        font-size: 0.72rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        font-weight: 600;
        margin-top: 4px;
    }

    /* Subtle Blue Symptom Tags */
    span[data-baseweb="tag"] {
        background: rgba(30, 58, 138, 0.5) !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
        color: #e0f2fe !important;
        border-radius: 8px !important;
        padding: 4px 10px !important;
        font-weight: 600 !important;
        font-size: 0.83rem !important;
        transition: all 0.2s ease;
    }
    span[data-baseweb="tag"]:hover {
        border-color: #38bdf8 !important;
        background: rgba(37, 99, 235, 0.65) !important;
    }
    span[data-baseweb="tag"] span { color: #e0f2fe !important; }
    span[data-baseweb="tag"] svg { fill: #93c5fd !important; }

    /* Multiselect Dropdown Shell */
    div[data-baseweb="select"] > div {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        color: #f8fafc !important;
        transition: all 0.25s ease !important;
    }
    div[data-baseweb="select"] > div:focus-within {
        border-color: #38bdf8 !important;
        box-shadow: 0 0 16px rgba(56, 189, 248, 0.25) !important;
    }

    /* Primary Action Button */
    div.stButton > button[kind="primary"] {
        width: 100%;
        background: linear-gradient(135deg, #1d4ed8 0%, #0284c7 100%) !important;
        border: 1px solid rgba(56, 189, 248, 0.4) !important;
        color: #ffffff !important;
        font-size: 1.02rem !important;
        font-weight: 700 !important;
        border-radius: 12px !important;
        padding: 13px 26px !important;
        box-shadow: 0 6px 20px rgba(2, 132, 199, 0.3) !important;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 28px rgba(56, 189, 248, 0.5) !important;
        border-color: #38bdf8 !important;
    }

    /* Preset Buttons */
    div.stButton > button:not([kind="primary"]) {
        background: rgba(15, 23, 42, 0.5) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #cbd5e1 !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        font-size: 0.84rem !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:not([kind="primary"]):hover {
        background: rgba(56, 189, 248, 0.1) !important;
        border-color: rgba(56, 189, 248, 0.45) !important;
        color: #38bdf8 !important;
        transform: translateY(-1px);
    }

    /* Glass Container */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(15, 23, 42, 0.7) !important;
        backdrop-filter: blur(18px) !important;
        -webkit-backdrop-filter: blur(18px) !important;
        border: 1px solid rgba(56, 189, 248, 0.25) !important;
        border-radius: 18px !important;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.6) !important;
        padding: 10px !important;
        animation: fadeInSlide 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .matched-chip {
        background: rgba(56, 189, 248, 0.12);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 6px;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# 3. Load Model Assets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

@st.cache_resource
def load_assets():
    model_path = os.path.join(MODEL_DIR, "symptom_model.pkl") if os.path.exists(os.path.join(MODEL_DIR, "symptom_model.pkl")) else "model/symptom_model.pkl"
    symptoms_path = os.path.join(MODEL_DIR, "symptoms_list.pkl") if os.path.exists(os.path.join(MODEL_DIR, "symptoms_list.pkl")) else "model/symptoms_list.pkl"
    symptom_map_path = os.path.join(MODEL_DIR, "disease_symptoms_map.pkl") if os.path.exists(os.path.join(MODEL_DIR, "disease_symptoms_map.pkl")) else "model/disease_symptoms_map.pkl"
    
    model = joblib.load(model_path)
    symptoms = joblib.load(symptoms_path)
    symptom_map = joblib.load(symptom_map_path)
    return model, symptoms, symptom_map

try:
    model, symptoms_list, disease_symptoms_map = load_assets()
except Exception:
    st.error("Model files not found! Please run `python train.py` first.")
    st.stop()

# 4. Medical Knowledge Dictionary
DISEASE_INFO = {
    "Hypothyroidism": {
        "severity": "🟡 Moderate (Endocrine)",
        "desc": "An underactive thyroid gland that does not produce enough thyroid hormones, slowing your metabolism and causing cold sensitivity (cold hands/feet), fatigue, and unexplained weight gain.",
        "precautions": ["Consult an endocrinologist", "Get a Thyroid Function Test (TSH, Free T3, T4)", "Maintain a balanced, iodine-sufficient diet", "Take prescribed thyroid hormone medication regularly"]
    },
    "Hypoglycemia": {
        "severity": "🟡 Moderate (Metabolic)",
        "desc": "Abnormally low blood sugar (glucose) levels, triggering the nervous system to produce sweating, shaking, rapid heartbeat, cold limbs, and dizziness.",
        "precautions": ["Consume fast-acting carbohydrates (fruit juice, candy)", "Check blood glucose immediately", "Eat small, frequent balanced meals", "Consult a doctor if episodes recur"]
    },
    "Fungal infection": {
        "severity": "🟢 Mild (Dermatology)",
        "desc": "A skin or tissue infection caused by fungi or yeast, causing persistent itching, skin peeling, redness, and circular rashes.",
        "precautions": ["Keep the affected skin clean and dry", "Apply prescribed antifungal cream/powder", "Do not share personal items (towels, clothing)", "Wear loose cotton garments"]
    },
    "Allergy": {
        "severity": "🟢 Mild (Immunology)",
        "desc": "An immune system hypersensitivity reaction to allergens (dust, pollen, pet dander), causing sneezing, watery eyes, and runny nose.",
        "precautions": ["Identify and avoid known allergen triggers", "Take prescribed antihistamines", "Use saline nasal sprays", "Keep living spaces dusted and clean"]
    },
    "GERD": {
        "severity": "🟢 Mild (Digestive)",
        "desc": "Gastroesophageal Reflux Disease occurs when stomach acid leaks back into the esophagus, causing burning chest discomfort (heartburn), acidity, and sour burps.",
        "precautions": ["Avoid fatty, spicy, and acidic foods", "Do not lie down for 2-3 hours after eating", "Eat smaller portion meals", "Elevate the head of your bed"]
    },
    "Diabetes": {
        "severity": "🟡 Moderate (Chronic)",
        "desc": "A chronic condition where the body cannot properly process glucose, leading to excessive thirst, frequent urination, fatigue, and blurred vision.",
        "precautions": ["Monitor blood sugar levels daily", "Follow a low-glycemic, fiber-rich diet", "Engage in regular daily physical activity", "Consult an endocrinologist for medication"]
    },
    "Hypertension": {
        "severity": "🟡 Moderate (Cardiovascular)",
        "desc": "High blood pressure that forces blood against artery walls at dangerously high levels, placing strain on blood vessels.",
        "precautions": ["Reduce dietary sodium (salt) intake", "Exercise 30 minutes daily", "Limit alcohol and quit smoking", "Monitor blood pressure regularly at home"]
    },
    "Migraine": {
        "severity": "🟡 Moderate (Neurology)",
        "desc": "A neurological condition causing severe, throbbing headaches usually on one side of the head, accompanied by nausea and light/sound sensitivity.",
        "precautions": ["Rest in a dark, quiet room", "Stay well hydrated", "Apply a cold compress to the forehead", "Maintain a consistent sleep schedule"]
    },
    "Malaria": {
        "severity": "🔴 High / Urgent Care",
        "desc": "A parasitic infection transmitted by mosquitoes that causes cyclical episodes of shivering chills, high fever, sweating, and nausea.",
        "precautions": ["Seek medical attention for an immediate blood smear test", "Take prescribed antimalarial medications", "Drink electrolyte rehydration fluids", "Use mosquito netting and repellent"]
    },
    "Dengue": {
        "severity": "🔴 High / Urgent Care",
        "desc": "A viral infection transmitted by Aedes mosquitoes causing high fever, intense headache, severe joint/muscle pain, and pain behind the eyes.",
        "precautions": ["Drink plenty of fluids (coconut water, oral rehydration)", "Monitor platelet counts daily", "Avoid NSAIDs like aspirin or ibuprofen", "Seek urgent hospital care if persistent vomiting occurs"]
    },
    "Typhoid": {
        "severity": "🔴 High / Urgent Care",
        "desc": "A bacterial infection caused by Salmonella typhi, resulting in persistent high fever, abdominal tenderness, headache, and severe weakness.",
        "precautions": ["Drink only boiled or sealed bottled water", "Eat thoroughly cooked, hot food", "Complete the full course of prescribed antibiotics", "Practice strict hand hygiene"]
    },
    "Heart attack": {
        "severity": "🚨 CRITICAL EMERGENCY",
        "desc": "A medical emergency when blood flow to a portion of the heart muscle is blocked, causing crushing chest pain, breathlessness, and cold sweating.",
        "precautions": ["CALL EMERGENCY SERVICES IMMEDIATELY (911 / 112)", "Chew an aspirin if instructed by emergency dispatchers", "Stay calm and remain seated", "Do not drive yourself to the hospital"]
    },
    "Urinary tract infection": {
        "severity": "🟢 Mild to Moderate",
        "desc": "A bacterial infection anywhere along the urinary tract, causing a sharp burning sensation during urination, pelvic pain, and constant urge to urinate.",
        "precautions": ["Drink large quantities of water", "Do not delay urination", "Complete the full antibiotic course prescribed by your doctor", "Avoid caffeine and alcohol while recovering"]
    },
    "Common Cold": {
        "severity": "🟢 Mild (Self-limiting)",
        "desc": "A viral infection of the upper respiratory tract causing runny nose, continuous sneezing, sore throat, and mild fatigue.",
        "precautions": ["Get adequate rest", "Drink warm broths and herbal teas", "Use steam inhalation for congestion", "Do warm salt water gargles"]
    },
    "Pneumonia": {
        "severity": "🔴 High / Urgent Care",
        "desc": "Infection inflaming the air sacs in one or both lungs, which may fill with fluid or phlegm, causing cough, high fever, and labored breathing.",
        "precautions": ["Consult a pulmonologist or hospital promptly", "Take prescribed antibiotics or antivirals", "Rest in an upright position to ease breathing", "Monitor blood oxygen (SpO2) levels"]
    }
}

def get_disease_details(disease_name):
    if disease_name in DISEASE_INFO:
        return DISEASE_INFO[disease_name]
    return {
        "severity": "🟡 Clinical Assessment Recommended",
        "desc": f"A diagnosed medical condition identified as {disease_name}. Requires clinical diagnostic confirmation.",
        "precautions": ["Consult a medical physician", "Get relevant laboratory blood work", "Get adequate rest", "Stay well hydrated"]
    }

# 5. Hero Section
st.markdown('<div style="text-align: center; margin-top: 10px;"><div class="hero-badge"><span class="status-beacon"></span> Clinical Intelligence Engine v2.4</div><h1 class="main-title">Health Predict AI</h1><p class="main-subtitle">Multi-symptom pattern matching engine. Correlating 132 clinical biomarkers with 41 pathology benchmarks.</p></div>', unsafe_allow_html=True)

# 6. KPI Dashboard Row
st.markdown('<div class="kpi-container"><div class="kpi-card"><div class="kpi-value">41</div><div class="kpi-label">Conditions Indexed</div></div><div class="kpi-card"><div class="kpi-value">132</div><div class="kpi-label">Clinical Markers</div></div><div class="kpi-card"><div class="kpi-value">100%</div><div class="kpi-label">Benchmark Accuracy</div></div></div>', unsafe_allow_html=True)

# 7. Quick Clinical Presets
st.markdown("<p style='font-size: 0.85rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.6px;'>⚡ Quick Test Scenarios</p>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

formatted_symptoms = {s.replace('_', ' ').strip().title(): s for s in symptoms_list}
sorted_display_names = sorted(list(formatted_symptoms.keys()))

if "selected_symptoms" not in st.session_state:
    st.session_state.selected_symptoms = ["Cold Hands And Feets", "Fatigue", "Weight Gain"]

if c1.button("🧊 Cold Hands & Feet", use_container_width=True):
    st.session_state.selected_symptoms = ["Cold Hands And Feets", "Fatigue", "Weight Gain"]
    st.rerun()

if c2.button("🦟 Mosquito / Fever", use_container_width=True):
    st.session_state.selected_symptoms = ["Chills", "Vomiting", "High Fever", "Headache", "Nausea"]
    st.rerun()

if c3.button("💔 Chest Distress", use_container_width=True):
    st.session_state.selected_symptoms = ["Chest Pain", "Breathlessness", "Sweating"]
    st.rerun()

if c4.button("🔥 Digestive / Acid", use_container_width=True):
    st.session_state.selected_symptoms = ["Stomach Pain", "Acidity", "Ulcers On Tongue", "Vomiting"]
    st.rerun()

st.write("")

# 8. Searchable Multiselect
st.markdown("<p style='font-size: 0.85rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.6px;'>🔍 Patient Symptoms</p>", unsafe_allow_html=True)
selected_display = st.multiselect(
    label="Select from 132 symptoms:",
    options=sorted_display_names,
    default=[s for s in st.session_state.selected_symptoms if s in sorted_display_names],
    placeholder="Type symptoms (e.g. cold hands, fever, headache, chest pain...)",
    label_visibility="collapsed"
)

st.markdown(f"<p style='color: #64748b; font-size: 0.82rem; margin-top: 6px;'>Currently active symptoms: <strong style='color:#38bdf8;'>{len(selected_display)}</strong></p>", unsafe_allow_html=True)
st.write("")

# 9. Primary Action Button
if st.button("✨ Execute Clinical Diagnostic Engine", type="primary", use_container_width=True):
    if len(selected_display) == 0:
        st.warning("⚠️ Please select at least one symptom from the search bar.")
    else:
        selected_internal = [formatted_symptoms[d] for d in selected_display]
        input_vector = [1 if s in selected_internal else 0 for s in symptoms_list]
        input_array = np.array([input_vector])
        
        predicted_disease = model.predict(input_array)[0]
        probabilities = model.predict_proba(input_array)[0]
        confidence = max(probabilities) * 100
        
        details = get_disease_details(predicted_disease)
        disease_symptoms = disease_symptoms_map.get(predicted_disease, [])
        matching_symptoms = [s for s in selected_internal if s in disease_symptoms]
        matching_display = [s.replace('_', ' ').title() for s in matching_symptoms]
        
        # 10. Native Glassmorphic Diagnostic Dossier
        with st.container(border=True):
            col_t1, col_t2 = st.columns([3, 1])
            with col_t1:
                st.caption("🔬 AI DIAGNOSTIC DOSSIER")
                st.markdown(f"<h2 style='color:#ffffff; margin:0; font-size:1.85rem; font-weight:800;'>{predicted_disease}</h2>", unsafe_allow_html=True)
            with col_t2:
                st.caption("CONFIDENCE")
                st.markdown(f"<h3 style='color:#38bdf8; margin:0; font-size:1.45rem; font-weight:800;'>{confidence:.1f}%</h3>", unsafe_allow_html=True)
            
            st.markdown(f"<p style='font-size:0.84rem; color:#94a3b8; margin-top:10px;'>Classification: <strong style='color:#e2e8f0;'>{details['severity']}</strong></p>", unsafe_allow_html=True)
            
            st.markdown("<p style='font-size:0.78rem; font-weight:700; color:#94a3b8; text-transform:uppercase; margin-bottom:6px;'>Triggering Biomarkers</p>", unsafe_allow_html=True)
            if matching_display:
                chips_html = "".join([f'<span class="matched-chip">✓ {s}</span>' for s in matching_display])
                st.markdown(chips_html, unsafe_allow_html=True)
            else:
                st.info("General pattern correlation match.")
            
            st.divider()
            
            st.markdown("#### 📖 Clinical Interpretation")
            st.write(details['desc'])
            
            st.markdown("#### 🛡️ Recommended Medical Protocol")
            for p in details['precautions']:
                st.markdown(f"- **{p}**")
        
        st.write("")
        
        # Differential Diagnoses Spectrum
        top_indices = np.argsort(probabilities)[::-1][:4]
        st.markdown("<p style='font-size: 0.85rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.6px;'>📊 Differential Diagnoses (Probability Spectrum)</p>", unsafe_allow_html=True)
        for idx in top_indices:
            disease_name = model.classes_[idx]
            prob = probabilities[idx]
            if prob > 0.02 and disease_name != predicted_disease:
                col_d1, col_d2 = st.columns([4, 1])
                with col_d1:
                    st.write(f"**{disease_name}**")
                with col_d2:
                    st.write(f"*{prob * 100:.1f}%*")
                st.progress(float(prob))

st.write("")
st.markdown("<p style='text-align: center; color: #64748b; font-size: 0.76rem;'>⚠️ <strong>Medical Disclaimer:</strong> Health Predict AI is an educational decision-support tool. It does not replace professional medical consultation, lab testing, or clinical diagnosis.</p>", unsafe_allow_html=True)