import pandas as pd

from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.model_selection import StratifiedKFold, cross_validate
from xgboost import XGBClassifier


data = pd.read_csv("data/phishing_urls.csv")
data = data.dropna()

X = data.drop(columns=["target"])
y = data["target"].astype(int)

random_forest = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced",
    n_jobs=-1
)

xgboost = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    random_state=42,
    eval_metric="logloss"
)

ensemble = VotingClassifier(
    estimators=[
        ("random_forest", random_forest),
        ("xgboost", xgboost)
    ],
    voting="soft"
)

cv = StratifiedKFold(
    n_splits=10,
    shuffle=True,
    random_state=42
)

scores = cross_validate(
    ensemble,
    X,
    y,
    cv=cv,
    scoring=[
        "accuracy",
        "precision",
        "recall",
        "f1",
        "roc_auc"
    ],
    n_jobs=-1
)

for metric in ["accuracy", "precision", "recall", "f1", "roc_auc"]:
    values = scores[f"test_{metric}"]
    print(
        f"{metric}: "
        f"{values.mean():.4f} +/- {values.std():.4f}"
    )