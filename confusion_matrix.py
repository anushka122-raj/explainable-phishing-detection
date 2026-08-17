import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

ensemble = joblib.load("models/ensemble_model.pkl")
X_test, y_test = joblib.load("models/test_data.pkl")

predictions = ensemble.predict(X_test)
matrix = confusion_matrix(y_test, predictions)

plt.figure(figsize=(7, 5))
sns.heatmap(
    matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Legitimate", "Phishing"],
    yticklabels=["Legitimate", "Phishing"]
)

plt.xlabel("Predicted label")
plt.ylabel("Actual label")
plt.title("Ensemble Model Confusion Matrix")
plt.tight_layout()
plt.savefig("results/confusion_matrix.png", dpi=300)
plt.show()
