from data_loader import load_data
from preprocessor import preprocess
from train_models import train_model
from evaluate import evaluate_model

data = load_data("player_injuries.csv")

X_train, X_test, y_train, y_test = preprocess(data)

model = train_model(X_train, y_train)

evaluate_model(model, X_test, y_test)