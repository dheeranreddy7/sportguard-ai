import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("player_data.csv")

# Features & Target
X = data[['Age', 'Training', 'Injuries', 'Sleep', 'Hydration']]
y = data['Risk']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved!")