from tensorflow import keras
import joblib

model = keras.models.load_model("models/ann_soc_soh_model.keras")
print("✅ Model Loaded Successfully")

scaler = joblib.load("models/scaler.pkl")
print("✅ Scaler Loaded Successfully")

features = joblib.load("models/feature_columns.pkl")
print(features)
print("✅ Feature Mapping Loaded Successfully")