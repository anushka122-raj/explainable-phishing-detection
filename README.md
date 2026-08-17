\# Explainable Phishing Website and URL Detection



An explainable machine learning framework for real-time phishing website and URL detection using ensemble classifiers and explainable AI techniques.



\## 📌 Overview



Phishing attacks are one of the most common cybersecurity threats, where attackers create malicious websites or URLs that imitate legitimate services to steal sensitive information.



This project implements a machine learning-based phishing detection system that analyzes URL characteristics and predicts whether a given URL is:



\- 🟢 Legitimate

\- 🔴 Phishing



The system uses an ensemble machine learning model to improve detection performance and provides an interactive web interface for real-time URL analysis.



\## ✨ Features



\- Real-time phishing URL detection

\- URL feature extraction

\- Ensemble machine learning classification

\- Explainable AI-based predictions

\- Interactive web interface

\- Model evaluation and comparison

\- External dataset evaluation

\- Confusion matrix and performance analysis



\## 🧠 Machine Learning Approach



The system extracts multiple features from URLs and uses them as inputs to the trained machine learning model.



The project includes an ensemble classifier trained for phishing detection.



\### Main Components



1\. \*\*URL Feature Extraction\*\*

&#x20;  - Extracts structural and lexical characteristics from URLs.

&#x20;  - Converts raw URLs into machine-learning features.



2\. \*\*Ensemble Classification\*\*

&#x20;  - Uses a trained ensemble model to classify URLs.

&#x20;  - The trained model is stored in the `models/` directory.



3\. \*\*Prediction\*\*

&#x20;  - The user enters a URL through the web application.

&#x20;  - Features are extracted automatically.

&#x20;  - The trained model predicts whether the URL is phishing or legitimate.



4\. \*\*Explainability\*\*

&#x20;  - Explainable AI techniques are used to improve the interpretability of model predictions.



\## 🏗️ Project Structure



```text

Explainable-Phishing-Detection/

│

├── app.py

├── feature\_extractor.py

├── train\_model.py

├── evaluate\_models.py

├── cross\_validation.py

├── confusion\_matrix.py

├── external\_evaluation.py

├── model\_results.py

├── requirements.txt

│

├── data/

│   ├── phishing\_urls.csv

│   └── validation\_urls.csv

│

├── external\_data/

│   ├── external\_test.csv

│   ├── final\_external\_test.csv

│   ├── external\_results.csv

│   └── real\_external\_results.csv

│

├── models/

│   ├── ensemble\_model.pkl

│   └── feature\_columns.pkl

│

├── results/

│   ├── confusion\_matrix.png

│   ├── model\_comparison.png

│   └── model\_comparison.csv

│

└── src/

