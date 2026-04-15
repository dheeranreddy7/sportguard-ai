from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=200, max_depth=5)
    model.fit(X_train, y_train)

    joblib.dump(model, "model.pkl")
    return model