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
