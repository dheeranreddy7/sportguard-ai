from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

def preprocess(data):
    X = data.drop("injury", axis=1)
    y = data["injury"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    joblib.dump(scaler, "scaler.pkl")  # SAVE scaler

    return train_test_split(X_scaled, y, test_size=0.2)