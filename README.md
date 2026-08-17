# 🛡️ Explainable Phishing URL Detection

### An Explainable Machine Learning Framework for Real-Time Phishing Website and URL Detection Using Ensemble Classifiers

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Ensemble-orange)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-ML-red)](https://xgboost.readthedocs.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Explainable AI](https://img.shields.io/badge/XAI-SHAP-purple)](https://shap.readthedocs.io/)

> A machine learning-powered web application that analyzes URLs in real time and predicts whether they are potentially **phishing or legitimate**, while exposing the URL characteristics used for the prediction.

---

## 📌 Overview

Phishing attacks use deceptive URLs and websites to trick users into revealing sensitive information such as passwords, financial details, and personal credentials.

Traditional blacklist-based approaches can struggle with newly created or previously unseen phishing URLs.

This project explores a **machine learning-based approach to phishing URL detection** by extracting meaningful features from URLs and using an **ensemble classifier** to identify suspicious patterns.

The system provides an interactive web interface where a user can enter a URL and receive:

- 🔍 URL analysis
- 🧠 Machine learning prediction
- 📊 Phishing probability
- 🛡️ Safe/suspicious classification
- 🔬 Extracted URL features
- 💡 Explainability-oriented insights

---

# 🎯 Objectives

The primary objectives of this project are:

1. Detect potentially malicious URLs using machine learning.
2. Extract meaningful structural and lexical characteristics from URLs.
3. Improve classification using ensemble learning.
4. Provide real-time predictions through an interactive web application.
5. Evaluate the model using multiple validation strategies.
6. Improve transparency by exposing the features contributing to predictions.
7. Evaluate model behavior on external URL datasets.

---

# 🧠 How It Works

The application follows the following pipeline:

```text
                    ┌─────────────────────┐
                    │     User enters     │
                    │        URL          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   URL Validation    │
                    │   & Preprocessing   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Feature           │
                    │   Extraction        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Ensemble ML Model   │
                    │      Prediction     │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
             ┌─────────────┐       ┌─────────────┐
             │ Legitimate  │       │   Phishing  │
             │    URL      │       │     URL     │
             └─────────────┘       └─────────────┘
                    │                     │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Probability +       │
                    │ Extracted Features  │
                    └─────────────────────┘
## ✨ Key Features

- 🛡️ **Real-Time URL Detection** — Analyze a URL and receive an immediate phishing/legitimate prediction.
- 🔍 **Automated Feature Extraction** — Converts raw URLs into meaningful machine-learning features.
- 🤖 **Ensemble Machine Learning** — Uses a trained ensemble classifier for robust phishing detection.
- 📊 **Probability-Based Prediction** — Displays the model's estimated phishing probability.
- 🔬 **Explainable Predictions** — Allows users to inspect extracted URL characteristics behind the prediction.
- 🌐 **Interactive Web Interface** — Built with Streamlit for simple and accessible URL analysis.
- 🧪 **Model Evaluation** — Includes cross-validation, model comparison, confusion matrix analysis, and external evaluation.
- 🌍 **External Dataset Testing** — Evaluates model behavior on data outside the primary dataset.

## 🌐 Application Demo

The project provides an interactive web interface where users can enter a URL and receive an immediate prediction.

### Example: Legitimate URL

**Input**

```text
https://github.com

✅ The model does not flag this URL as suspicious.

Phishing probability:
0.00%

### 🖥️ Application Interface

![Phishing Detection Dashboard](results/app-home.png)

### ✅ Legitimate URL Prediction

![Legitimate URL Result](results/legitimate-result.png)

### 🚨 Phishing URL Prediction

![Phishing URL Result](results/phishing-result.png)

## 🧠 Machine Learning Pipeline

The complete detection pipeline consists of the following stages:

```text
Raw URL
   │
   ▼
URL Preprocessing
   │
   ▼
Feature Extraction
   │
   ▼
Feature Vector
   │
   ▼
Machine Learning Models
   │
   ├── Random Forest
   │
   ├── XGBoost
   │
   └── Ensemble Classifier
   │
   ▼
Prediction Probability
   │
   ▼
Phishing / Legitimate
   │
   ▼
Feature-Level Interpretation

## 📊 Model Evaluation

The project evaluates the classification system using multiple complementary techniques.

### Evaluation Methods

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Cross-Validation
- External Dataset Evaluation

### Model Comparison

The repository contains comparative evaluation results for the implemented machine learning approaches.

![Model Comparison](results/model_comparison.png)

### Confusion Matrix

![Confusion Matrix](results/confusion_matrix.png)

## 🔬 Explainable AI

A key objective of this project is to move beyond a simple binary prediction.

Instead of only answering:

> "Is this URL phishing?"

the system is designed to help answer:

> "What characteristics of this URL contributed to the prediction?"

The extracted URL features provide an interpretable representation of the input used by the machine learning model.

This explainability-oriented design can help researchers and security analysts understand model behavior, investigate suspicious URL characteristics, and improve trust in automated predictions.

### Why Explainability Matters

Cybersecurity decisions can have significant consequences. A transparent model can help users and analysts:

- Understand suspicious URL characteristics
- Investigate model predictions
- Identify potentially important features
- Debug unexpected classifications
- Improve confidence in machine learning-assisted security systems

## 🛠️ Technology Stack

The project combines **machine learning, cybersecurity-oriented feature engineering, explainable AI, data processing, and an interactive web interface** into a single end-to-end detection system.

### 💻 Core Technologies

| 🧩 Category | ⚙️ Technology | 🎯 Role in the Project |
|---|---|---|
| 🐍 Programming Language | **Python** | Core language used to build the detection pipeline |
| 🌐 Web Application | **Streamlit** | Provides the interactive phishing URL detection interface |
| 🤖 Machine Learning | **Scikit-learn** | Model training, evaluation, preprocessing, and classification |
| 🚀 Gradient Boosting | **XGBoost** | High-performance machine learning model for phishing classification |
| 🌳 Ensemble Learning | **Random Forest + Ensemble Model** | Learns complex patterns from URL-based features |
| 🔍 Feature Engineering | **Custom Python Feature Extractor** | Converts raw URLs into structured ML features |
| 📊 Data Processing | **Pandas** | Dataset manipulation and analysis |
| 🔢 Numerical Computing | **NumPy** | Numerical operations and feature processing |
| 📈 Visualization | **Matplotlib** | Confusion matrices, model comparison, and result visualization |
| 🔬 Explainable AI | **SHAP / Feature Analysis** | Helps interpret model behavior and feature contributions |
| 💾 Model Persistence | **Joblib** | Saves and loads trained machine learning models |
| 🗂️ Version Control | **Git & GitHub** | Source-code management and project versioning |

---

### 🧠 Machine Learning Layer

```text
🔗 Raw URL
     │
     ▼
🔍 Feature Extraction
     │
     ▼
📊 Structured Feature Vector
     │
     ├───────────────┐
     ▼               ▼
🌳 Random Forest   🚀 XGBoost
     │               │
     └───────┬───────┘
             ▼
       🤖 Ensemble Model
             │
             ▼
      🎯 Final Prediction

🌐 Application Layer
The user interacts with the system through a Streamlit-based web interface.

👤 User
  │
  │ Enter URL
  ▼
🌐 Streamlit Interface
  │
  ▼
🔍 Feature Extraction
  │
  ▼
🤖 Ensemble Model
  │
  ▼
📊 Prediction Probability
  │
  ├── 🟢 Legitimate
  │
  └── 🔴 Phishing

🔬 Explainability Layer

The explainability component complements the prediction by exposing the URL characteristics used during analysis.

🤖 Model Prediction
        │
        ▼
🔬 Explainability Analysis
        │
        ▼
📊 Feature-Level Insights
        │
        ▼
💡 More Interpretable Prediction

📦 Key Python Libraries
Python
│
├── 🧠 scikit-learn
├── 🚀 xgboost
├── 📊 pandas
├── 🔢 numpy
├── 📈 matplotlib
├── 💾 joblib
├── 🌐 streamlit
└── 🔬 shap


## 📊 Results & Analysis

The proposed phishing URL detection system was evaluated using multiple experimental approaches to assess its classification performance, robustness, and generalization capability.

### 🏆 Performance Overview

| 📌 Evaluation | 🔍 Purpose |
|---|---|
| 🎯 Accuracy | Measures overall classification correctness |
| 🎣 Precision | Measures how reliably phishing predictions are identified |
| 🔎 Recall | Measures the ability to detect phishing URLs |
| ⚖️ F1-Score | Balances precision and recall |
| 🧩 Confusion Matrix | Analyzes correct and incorrect classifications |
| 🔄 Cross-Validation | Evaluates model stability across different data splits |
| 🌍 External Evaluation | Tests generalization on external URL data |

---

## 🤖 Model Comparison

Multiple machine learning approaches were evaluated to investigate their effectiveness for phishing URL classification.

The experimental workflow compares different classifiers and evaluates their performance using multiple metrics. The final web application uses the trained **ensemble classifier** for real-time URL prediction.

### 📈 Comparative Performance

The following visualization summarizes the experimental comparison between the implemented machine learning approaches.

![Model Comparison](results/model_comparison.png)

> 💡 Why **ensemble learning**?
> The ensemble approach combines the predictive capabilities of multiple learners to capture complementary patterns in URL-based features and provide the final classification used by the application.

### 🔎** Evaluation Metrics**

The comparison considers metrics such as:

- 🎯 **Accuracy** — Overall classification correctness
- 🎣 **Precision** — Reliability of phishing predictions
- 🔍 **Recall** — Ability to identify phishing URLs
- ⚖️ **F1-Score** — Balance between precision and recall

The underlying numerical results are available in:

```text
results/model_comparison.csv
📈 **Model comparison visualization:**

![Model Comparison](results/model_comparison.png)

---

### 🧩 **Confusion Matrix**

The confusion matrix provides a detailed view of the model's classification behavior, including:

- 🟢 Correctly identified legitimate URLs
- 🔴 Correctly identified phishing URLs
- ⚠️ Legitimate URLs incorrectly classified as phishing
- 🚨 Phishing URLs incorrectly classified as legitimate

![Confusion Matrix](results/confusion_matrix.png)

---

### 🌍 **External Evaluation**

To examine how the model performs beyond the primary dataset, an external evaluation workflow was implemented.

The external evaluation process helps investigate the model's ability to generalize to previously unseen URL samples.

```text
                 🧪 External URLs
                        │
                        ▼
               🔍 Feature Extraction
                        │
                        ▼
                 🤖 Trained Model
                        │
                        ▼
               📊 Prediction Results
                        │
                        ▼
             ┌──────────┴──────────┐
             ▼                     ▼
        🟢 Legitimate          🔴 Phishing

## ⚠️** Limitations**

While the proposed system provides an effective machine-learning-based approach for phishing URL detection, several limitations remain.

### 🔗 1.** URL-Level Analysis**

The current system primarily analyzes **URL-based features**. It does not fully inspect the visual appearance, HTML structure, JavaScript behavior, or complete content of the webpage.

### 🆕 2. **Zero-Day Phishing**

Newly generated phishing URLs may exhibit patterns that differ significantly from those present in the training data. Therefore, completely novel attack patterns may be challenging for a trained model to identify.

### 🌐 3.** Dataset Dependency**

Machine learning performance depends heavily on the quality, diversity, and representativeness of the datasets used for training and evaluation.

### 🔄 4.** Concept Drift**

Phishing techniques continuously evolve. URL structures and attacker strategies may change over time, which can reduce model performance if the model is not periodically retrained.

### 🧩 5.** Limited Contextual Information**

URL-level features alone may not capture important contextual information such as:

- 🌍 Domain reputation
- 🔐 SSL/TLS certificate information
- 🕐 Domain age
- 🌐 DNS characteristics
- 📄 Website content
- 🔀 Redirect behavior
- 🧠 JavaScript activity

### ⚖️ 6. False Positives and False Negatives

No machine learning classifier is perfect.

A legitimate URL may occasionally be classified as suspicious (**false positive**), while a sophisticated phishing URL may be classified as legitimate (**false negative**).

For this reason, the system should be considered a **decision-support tool rather than a standalone security mechanism**.

### 🔬 7. **Explainability Scope**

The current explainability approach focuses primarily on the **features extracted from the URL**. Future versions can provide richer model-level explanations and more detailed visual interpretations of individual predictions.

### 🖥️ 8. **Deployment Scope**

The current implementation is primarily designed as an interactive research and demonstration application using Streamlit. Production deployment would require additional considerations such as scalability, authentication, monitoring, security hardening, and continuous model updates.

---

### 💡 **Research Perspective**

These limitations also identify opportunities for future development. Extending the system with **website-content analysis, domain intelligence, DNS information, real-time threat feeds, continuous learning, and richer XAI techniques** could make the detection framework more comprehensive and robust.

---

## 🚀 **Future Improvements**

Future development could extend the system with:

- 🌐 Website content analysis
- 🔐 SSL/TLS certificate analysis
- 🌍 DNS and domain-age information
- 🧠 Advanced deep learning models
- 🔎 Real-time threat intelligence feeds
- 🧩 Browser extension integration
- ☁️ Cloud/API deployment
- 🔄 Continuous model retraining
- 📊 Advanced SHAP visualizations
- ⚡ Real-time monitoring and alerting
