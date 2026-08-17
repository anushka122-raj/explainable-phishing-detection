from pathlib import Path
from urllib.parse import urlparse

import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)


SUSPICIOUS_WORDS = [
    "login",
    "verify",
    "verification",
    "update",
    "secure",
    "account",
    "bank",
    "confirm",
    "password"
]


def extract_features_from_url(url):
    clean_url = str(url).strip().lower()

    if not clean_url.startswith(("http://", "https://")):
        parsed_url = urlparse("http://" + clean_url)
    else:
        parsed_url = urlparse(clean_url)

    domain = parsed_url.netloc
    path = parsed_url.path

    features = {
        "url_length": len(clean_url),
        "valid_url": int(bool(domain)),
        "at_symbol": clean_url.count("@"),
        "sensitive_words_count": sum(
            word in clean_url
            for word in SUSPICIOUS_WORDS
        ),
        "path_length": len(path),
        "isHttps": int(
            clean_url.startswith("https://")
        ),
        "nb_dots": clean_url.count("."),
        "nb_hyphens": clean_url.count("-"),
        "nb_and": clean_url.count("&"),
        "nb_or": clean_url.count("|"),
        "nb_www": clean_url.count("www"),
        "nb_com": clean_url.count(".com"),
        "nb_underscore": clean_url.count("_")
    }

    return features


external_file = Path(
    "external_data/real_external_test.csv"
)

if not external_file.is_file():
    print(
        f"File not found: "
        f"{external_file.resolve()}"
    )
    raise SystemExit(
        "Create external_data/"
        "real_external_test.csv first."
    )


try:
    external_data = pd.read_csv(external_file)
except pd.errors.EmptyDataError:
    raise SystemExit(
        "The CSV file is empty. Add the header "
        "'url,target' and data rows."
    )


required_columns = {"url", "target"}

missing_columns = required_columns - set(
    external_data.columns
)

if missing_columns:
    raise SystemExit(
        f"Missing columns: {missing_columns}. "
        "The CSV must contain url,target."
    )

if external_data.empty:
    raise SystemExit(
        "The CSV has no data rows."
    )


model = joblib.load(
    "models/ensemble_model.pkl"
)

feature_columns = joblib.load(
    "models/feature_columns.pkl"
)


feature_rows = [
    extract_features_from_url(url)
    for url in external_data["url"]
]

X_external = pd.DataFrame(feature_rows)

missing_features = set(feature_columns) - set(
    X_external.columns
)

if missing_features:
    raise SystemExit(
        f"Missing feature columns: "
        f"{missing_features}"
    )

X_external = X_external[feature_columns]

print("\nExternal feature values:")
print(X_external.to_string())


y_external = external_data["target"].astype(int)

probabilities = model.predict_proba(
    X_external
)[:, 1]

threshold = 0.90

predictions = (
    probabilities >= threshold
).astype(int)


print("\nPrediction probabilities:")

for url, target, probability, prediction in zip(
    external_data["url"],
    y_external,
    probabilities,
    predictions
):
    print(
        f"{target} | {prediction} | "
        f"{probability:.6f} | {url}"
    )


print("\nExternal validation results")
print("---------------------------")

print(
    f"Accuracy:  "
    f"{accuracy_score(y_external, predictions):.4f}"
)

print(
    f"Precision: "
    f"{precision_score(y_external, predictions, zero_division=0):.4f}"
)

print(
    f"Recall:    "
    f"{recall_score(y_external, predictions, zero_division=0):.4f}"
)

print(
    f"F1-score:  "
    f"{f1_score(y_external, predictions, zero_division=0):.4f}"
)

if len(set(y_external)) == 2:
    print(
        f"ROC-AUC:   "
        f"{roc_auc_score(y_external, probabilities):.4f}"
    )
else:
    print(
        "ROC-AUC:   Not available "
        "(only one class is present)"
    )


print("\nConfusion matrix")
print(confusion_matrix(y_external, predictions))


print("\nClassification report")
print(
    classification_report(
        y_external,
        predictions,
        target_names=[
            "Legitimate",
            "Phishing"
        ],
        zero_division=0
    )
)


results = external_data.copy()

results["prediction"] = predictions

results["phishing_probability"] = probabilities

output_file = Path(
    "external_data/real_external_results.csv"
)

results.to_csv(
    output_file,
    index=False
)

print("\nDetailed results saved to:")
print(output_file)