import pandas as pd
import matplotlib.pyplot as plt

results = pd.DataFrame({
    "Model": ["Random Forest", "XGBoost", "Ensemble"],
    "Accuracy": [0.8976, 0.8956, 0.9076],
    "Precision": [0.9144, 0.9336, 0.9437],
    "Recall": [0.8638, 0.8383, 0.8553],
    "F1-score": [0.8884, 0.8834, 0.8973],
    "ROC-AUC": [0.9659, 0.9663, 0.9712]
})

results.to_csv("results/model_comparison.csv", index=False)

results.plot(
    x="Model",
    y=["Accuracy", "Precision", "Recall", "F1-score", "ROC-AUC"],
    kind="bar",
    figsize=(12, 7)
)

plt.title("Performance Comparison of Phishing Detection Models")
plt.ylabel("Score")
plt.ylim(0, 1)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.legend(loc="lower right")
plt.tight_layout()

plt.savefig("results/model_comparison.png", dpi=300)
plt.show()