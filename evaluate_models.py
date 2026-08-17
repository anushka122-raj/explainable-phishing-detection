import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

rf = joblib.load("models/random_forest.pkl")
xgb = joblib.load("models/xgboost.pkl")
ensemble = joblib.load("models/ensemble_model.pkl")
X_test, y_test = joblib.load("models/test_data.pkl")

models = {
    "Random Forest": rf,
    "XGBoost": xgb,
    "Ensemble": ensemble
}

for name, model in models.items():
    pred = model.predict(X_test)
    prob = model.predict_proba(X_test)[:, 1]

    print("\n", name)
    print("Accuracy:", accuracy_score(y_test, pred))
    print("Precision:", precision_score(y_test, pred))
    print("Recall:", recall_score(y_test, pred))
    print("F1-score:", f1_score(y_test, pred))
    print("ROC-AUC:", roc_auc_score(y_test, prob))
    print("Confusion Matrix:\n", confusion_matrix(y_test, pred))