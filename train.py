import os
import urllib.request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import joblib

os.makedirs("data", exist_ok=True)
os.makedirs("model", exist_ok=True)

raw_data_path = "data/symptom_training.csv"
DATASET_URL = "https://raw.githubusercontent.com/itachi9604/healthcare-chatbot/master/Data/Training.csv"

# 1. DOWNLOAD THE OFFICIAL SYMPTOM-DISEASE DATASET
if not os.path.exists(raw_data_path):
    print("🌐 Downloading symptom-disease dataset...")
    urllib.request.urlretrieve(DATASET_URL, raw_data_path)
    print("✅ Download completed.")

# 2. LOAD & CLEAN
df = pd.read_csv(raw_data_path)
df = df.loc[:, ~df.columns.duplicated()]
df = df.drop(columns=[col for col in df.columns if 'Unnamed' in col], errors='ignore')

X = df.drop(columns=['prognosis'])
y = df['prognosis']
symptoms_list = list(X.columns)

# 3. BUILD A CLINICAL SYMPTOM PROFILE FOR EACH DISEASE
disease_symptoms_map = {}
for disease, group in df.groupby('prognosis'):
    # Grab all symptoms that belong to this disease in the dataset
    active_symptoms = [col for col in X.columns if (group[col] == 1).any()]
    disease_symptoms_map[disease] = active_symptoms

print(f"📊 Dataset Loaded: {df.shape[0]} patients, {len(symptoms_list)} symptoms, {y.nunique()} diseases.")

# 4. TRAIN MULTINOMIAL NAIVE BAYES (Clinically accurate for symptom matching)
print("🧠 Training Multinomial Naive Bayes diagnostic model...")
model = MultinomialNB(alpha=0.01)
model.fit(X, y)

# 5. TEST ACCURACY
y_pred = model.predict(X)
acc = accuracy_score(y, y_pred)
print(f"🎯 Model Accuracy on Dataset: {acc * 100:.2f}%")

# 6. SAVE ARTIFACTS
joblib.dump(model, "model/symptom_model.pkl")
joblib.dump(symptoms_list, "model/symptoms_list.pkl")
joblib.dump(disease_symptoms_map, "model/disease_symptoms_map.pkl")
print("🚀 Saved 'model/symptom_model.pkl', 'symptoms_list.pkl', and 'disease_symptoms_map.pkl'!")