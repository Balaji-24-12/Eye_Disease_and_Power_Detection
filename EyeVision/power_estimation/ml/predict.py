import joblib
import numpy as np

model = joblib.load("power_estimation/ml/model.pkl")
scaler = joblib.load("power_estimation/ml/scaler.pkl")

def predict_power(age, axial_length):
    data = np.array([[age, axial_length]])
    data = scaler.transform(data)
    power = model.predict(data)
    return round(float(power[0]), 2)



