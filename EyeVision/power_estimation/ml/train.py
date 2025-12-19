import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# X = [age, axial_length]
X = np.array([
    [10, 23.5],
    [15, 24.0],
    [20, 24.8],
    [25, 25.5],
    [30, 26.2],
    [35, 26.8],
])

# Corresponding power (diopters)
y = np.array([-0.5, -1.0, -2.0, -3.0, -4.5, -6.0])

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_scaled, y)

# Save model & scaler
joblib.dump(model, "power_estimation/ml/model.pkl")
joblib.dump(scaler, "power_estimation/ml/scaler.pkl")

print("✅ Model trained with AGE + AXIAL LENGTH")
