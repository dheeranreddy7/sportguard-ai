import joblib
import numpy as np

def predict(data):
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")  # load scaler

    data = np.array(data).reshape(1, -1)
    data = scaler.transform(data)  # apply scaling

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return prediction, probability