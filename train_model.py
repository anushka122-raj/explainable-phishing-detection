import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

from xgboost import XGBClassifier

os.makedirs("models", exist_ok=True)

data = pd.read_csv("data/phishing_urls.csv")

print("Dataset shape:", data.shape)
print("Columns:", data.columns.tolist())

data = data.dropna()
data["target"] = data["target"].astype(int)

X = data.drop(columns=["target"])
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced",
    n_jobs=-1
)

xgb = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    random_state=42,
    eval_metric="logloss"
)

rf.fit(X_train, y_train)
xgb.fit(X_train, y_train)

ensemble = VotingClassifier(
    estimators=[
        ("random_forest", rf),
        ("xgboost", xgb)
    ],
    voting="soft"
)

ensemble.fit(X_train, y_train)

joblib.dump(rf, "models/random_forest.pkl")
joblib.dump(xgb, "models/xgboost.pkl")
joblib.dump(ensemble, "models/ensemble_model.pkl")
joblib.dump(list(X.columns), "models/feature_columns.pkl")
joblib.dump((X_test, y_test), "models/test_data.pkl")

print("Training complete.")
print("Models saved successfully.")