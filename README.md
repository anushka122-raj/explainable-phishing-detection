# 🛡️ Explainable Phishing URL Detection

### 🤖 An Explainable Machine Learning Framework for Real-Time Phishing Website and URL Detection Using Ensemble Classifiers

<p align="center">

🔍 **Detect** &nbsp; • &nbsp;
🤖 **Predict** &nbsp; • &nbsp;
🔬 **Explain** &nbsp; • &nbsp;
🛡️ **Protect**

</p>

---

## 🌐 Project Overview

Phishing attacks are among the most common cybersecurity threats, where attackers use deceptive websites and URLs to trick users into revealing sensitive information such as passwords, financial credentials, and personal data.

This project presents an **Explainable Machine Learning-based phishing URL detection system** capable of analyzing URLs and predicting whether they are potentially **legitimate or phishing**.

The system combines:

**🔗 URL Feature Engineering + 🤖 Ensemble Machine Learning + 📊 Model Evaluation + 🔬 Explainability + 🌐 Interactive Web Application**

to create an end-to-end phishing detection framework.

---

## 🎯 Project Objectives

The main objectives of this project are:

- 🛡️ Detect potentially malicious and phishing URLs.
- 🔍 Extract meaningful structural and lexical characteristics from URLs.
- 🤖 Apply machine learning techniques for URL classification.
- 🧩 Improve prediction using ensemble learning.
- 📊 Evaluate models using multiple performance metrics.
- 🌍 Test model behavior on external URL datasets.
- 🔬 Improve transparency through feature-level analysis.
- 🌐 Provide an easy-to-use real-time web interface.

---

# ⚡ Key Features

| Feature | Description |
|---|---|
| 🛡️ **Real-Time Detection** | Analyze a URL and receive an immediate prediction. |
| 🔍 **Automatic Feature Extraction** | Converts raw URLs into structured ML features. |
| 🤖 **Ensemble Classification** | Uses an ensemble-based classifier for final prediction. |
| 📊 **Probability Estimation** | Displays the estimated phishing probability. |
| 🔬 **Explainability** | Allows inspection of extracted URL characteristics. |
| 🌐 **Interactive Interface** | Simple Streamlit-based web application. |
| 🧪 **Model Evaluation** | Includes model comparison and validation experiments. |
| 🌍 **External Testing** | Evaluates model behavior on external URL samples. |

---

# 🧠 How It Works

The system follows a complete machine learning pipeline from URL input to final prediction.

```text
                    👤 USER
                      │
                      ▼
              🔗 Enter URL
                      │
                      ▼
          🧹 URL Validation & Processing
                      │
                      ▼
             🔍 Feature Extraction
                      │
                      ▼
             📊 Feature Vector
                      │
                      ▼
             🤖 Ensemble Model
                      │
              ┌───────┴───────┐
              ▼               ▼
        🟢 LEGITIMATE     🔴 PHISHING
              │               │
              └───────┬───────┘
                      ▼
             📊 Probability
                      │
                      ▼
             🔬 Feature Insights

🔄DETECTION PIPELINE

Step 1 — 🔗 URL Input

The user enters a website URL into the Streamlit interface.

Step 2 — 🧹 Preprocessing

The URL is validated and prepared for feature extraction.

Step 3 — 🔍 Feature Extraction

Relevant structural and lexical characteristics are extracted from the URL.

Step 4 — 📊 Feature Representation

The extracted information is converted into a structured feature vector.

Step 5 — 🤖 Machine Learning Prediction

The feature vector is passed to the trained ensemble classifier.

Step 6 — 🎯 Final Classification

The system predicts whether the URL is:

🟢 Legitimate

or

🔴 Phishing

Step 7 — 🔬 Interpretation

The application provides feature-level information to help understand the characteristics of the analyzed URL.

🔍 URL Feature Engineering

A raw URL contains several structural and lexical patterns that can provide useful signals for phishing detection.

The system converts these characteristics into machine-learning features.

🧩 Feature Categories

| Category                      | Examples                                  |
| ----------------------------- | ----------------------------------------- |
| 🔗 **URL Structure**          | URL length, path length                   |
| 🌐 **Domain Characteristics** | Dots, subdomains, domain structure        |
| 🔣 **Special Characters**     | `@`, `-`, `_`, `?`, `=` and other symbols |
| 🔐 **Security Indicators**    | HTTPS-related characteristics             |
| 🖥️ **Host Information**      | IP-address based URLs                     |
| 🔎 **Query Characteristics**  | Query length and parameters               |
| 🧠 **Lexical Patterns**       | Character and token-level properties      |

These features transform an unstructured URL into a numerical representation suitable for machine learning.

🤖 Machine Learning Approach

The project uses an ensemble machine learning approach for phishing URL classification.

The repository contains trained models and evaluation workflows for investigating different machine learning approaches.

🧠 Implemented Models

🌳 Random Forest

A tree-based ensemble algorithm capable of learning nonlinear relationships between URL characteristics.

🚀 XGBoost

A gradient boosting algorithm designed to capture complex patterns in structured data.

🤖 Ensemble Classifier

The final application uses a trained ensemble model to generate the prediction shown to the user.

🧩 Ensemble Architecture

The ensemble approach combines information learned from multiple machine learning models.
                    🔗 URL
                      │
                      ▼
              🔍 Feature Extraction
                      │
                      ▼
              📊 Feature Vector
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
       🌳 Random Forest    🚀 XGBoost
             │                 │
             └────────┬────────┘
                      ▼
              🤖 Ensemble Model
                      │
                      ▼
                🎯 Prediction
                      │
             ┌────────┴────────┐
             ▼                 ▼
       🟢 Legitimate      🔴 Phishing

🔬 Explainable AI:---

A major focus of this project is interpretability.
A traditional classifier may simply return
🔗 URL
   ↓
🔴 PHISHING
However, a more useful cybersecurity system should also help investigate:

💡 Why was this URL considered suspicious?
The project therefore exposes the URL characteristics used during the prediction process.
🔗 URL
  │
  ▼
🔍 Feature Extraction
  │
  ├── 📏 Length Characteristics
  ├── 🌐 Domain Characteristics
  ├── 🔣 Special Characters
  ├── 🔎 Lexical Patterns
  └── 🔐 Security Indicators
  │
  ▼
🤖 Ensemble Model
  │
  ▼
📊 Prediction Probability
  │
  ▼
🔬 Feature-Level Interpretation

💡 Why Explainability Matters

Explainability can help:---

🔎 Understand suspicious URL characteristics.
📊 Investigate model predictions.
🧪 Analyze unexpected classifications.
🛡️ Support cybersecurity investigations.
🧠 Improve trust in machine learning systems.
🔬 Support further research and model development.

🛡️ The objective is not only to predict phishing URLs, but also to make the prediction process more understandable.

🌐 Interactive Web Application

The project includes a Streamlit-based interface that allows users to analyze URLs in real time.

🖥️ Example
Input: https://github.com
Prediction:--
ℹ️ github.com is a commonly recognized domain.

✅ The model does not flag this URL as suspicious.

📊 Phishing probability
0.00%
The application also provides an option to inspect the extracted URL features.

📸 Application Preview

Add screenshots of your actual Streamlit application here.

🏠 Main Detection Interface

🟢 Legitimate URL Prediction

🔴 Phishing URL Prediction

📊 Results & Analysis

The proposed system is evaluated using multiple experimental approaches to investigate classification performance, model stability, and generalization.

🏆 Evaluation Metrics

| Metric                     | Purpose                                        |
| -------------------------- | ---------------------------------------------- |
| 🎯 **Accuracy**            | Measures overall classification correctness    |
| 🎣 **Precision**           | Measures reliability of phishing predictions   |
| 🔎 **Recall**              | Measures the ability to identify phishing URLs |
| ⚖️ **F1-Score**            | Balances precision and recall                  |
| 🧩 **Confusion Matrix**    | Shows detailed classification behavior         |
| 🔄 **Cross-Validation**    | Evaluates model stability                      |
| 🌍 **External Evaluation** | Tests generalization on external data          |

🤖 Model Comparison

Multiple machine learning approaches were evaluated to investigate their effectiveness for phishing URL classification.

The final web application uses the trained ensemble classifier for real-time prediction.

📈 Comparative Performance

📄 Numerical Results
The underlying numerical evaluation results are available in:
results/model_comparison.csv
This allows the graphical results to be inspected alongside the original experimental values.

🧩 Confusion Matrix

The confusion matrix provides a detailed view of the classifier's predictions.

It helps identify:

🟢 Correctly classified legitimate URLs
🔴 Correctly classified phishing URLs
⚠️ Legitimate URLs incorrectly classified as phishing
🚨 Phishing URLs incorrectly classified as legitimate
📊 Confusion Matrix Visualization

🌍 External Evaluation
The project also includes an external evaluation workflow to investigate how the trained model behaves on URL samples outside the primary evaluation dataset.
                 🧪 External URLs
                        │
                        ▼
               🔍 Feature Extraction
                        │
                        ▼
                 🤖 Trained Model
                        │
                        ▼
                📊 Prediction
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
        🟢 Legitimate         🔴 Phishing
External evaluation artifacts are available in:external_data/
This provides an additional perspective on model generalization.

📈 Experimental Artifacts
The repository contains the generated evaluation outputs:
results/
│
├── 📊 model_comparison.csv
├── 📈 model_comparison.png
└── 🧩 confusion_matrix.png
These artifacts make the experimental workflow more transparent and reproducible.

🛠️ Technology Stack

| Category                   | Technology                     | Role                            |
| -------------------------- | ------------------------------ | ------------------------------- |
| 🐍 **Programming**         | Python                         | Core development language       |
| 🌐 **Web Application**     | Streamlit                      | Interactive detection interface |
| 🤖 **Machine Learning**    | Scikit-learn                   | Model training and evaluation   |
| 🚀 **Gradient Boosting**   | XGBoost                        | Machine learning classification |
| 🌳 **Ensemble Learning**   | Random Forest + Ensemble Model | Pattern learning and prediction |
| 🔍 **Feature Engineering** | Custom Python Extractor        | URL feature extraction          |
| 📊 **Data Processing**     | Pandas                         | Dataset processing              |
| 🔢 **Numerical Computing** | NumPy                          | Numerical operations            |
| 📈 **Visualization**       | Matplotlib                     | Experimental visualizations     |
| 🔬 **Explainability**      | Feature-Level Analysis / SHAP  | Model interpretation            |
| 💾 **Model Persistence**   | Joblib                         | Model loading and storage       |
| 🗂️ **Version Control**    | Git & GitHub                   | Source-code management          |

🏗️ Project Architecture

                         🛡️ PHISHING DETECTION SYSTEM
                                      │
             ┌────────────────────────┼────────────────────────┐
             │                        │                        │
             ▼                        ▼                        ▼
       🌐 Web Interface         🔍 Feature Engine          📊 Dataset
        (Streamlit)                    │                        │
             │                         │                        │
             └───────────────┬─────────┴────────────────────────┘
                             ▼
                     🤖 ML Classification
                             │
                  ┌──────────┴──────────┐
                  ▼                     ▼
            🌳 Random Forest       🚀 XGBoost
                  │                     │
                  └──────────┬──────────┘
                             ▼
                    🤖 Ensemble Model
                             │
                             ▼
                    🎯 Final Prediction
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
           🟢 Legitimate             🔴 Phishing
                 │                       │
                 └───────────┬───────────┘
                             ▼
                      🔬 Explainability

📁 Project Structure

Explainable-Phishing-Detection/
│
├── 🖥️ app.py
│
├── 🔍 feature_extractor.py
├── 🤖 train_model.py
├── 📊 evaluate_models.py
├── 🔄 cross_validation.py
├── 🧩 confusion_matrix.py
├── 🌍 external_evaluation.py
├── 📈 model_results.py
│
├── 📂 data/
│   ├── phishing_urls.csv
│   ├── phishing_urls_old.csv
│   └── validation_urls.csv
│
├── 🌍 external_data/
│   ├── external_test.csv
│   ├── final_external_test.csv
│   ├── external_results.csv
│   ├── real_external_results.csv
│   └── ...
│
├── 🧠 models/
│   ├── ensemble_model.pkl
│   └── feature_columns.pkl
│
├── 📊 results/
│   ├── confusion_matrix.png
│   ├── model_comparison.csv
│   └── model_comparison.png
│
├── 📂 src/
│
├── 📦 requirements.txt
├── 🚫 .gitignore
└── 📖 README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/anushka122-raj/explainable-phishing-detection.git

2️⃣ Navigate to the Project
cd explainable-phishing-detection

3️⃣ Create a Virtual Environment
python -m venv .venv

4️⃣ Activate the Environment
🪟 Windows
.venv\Scripts\activate

🐧 Linux / macOS
source .venv/bin/activate

5️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
streamlit run app.py
The application will provide a local URL in the terminal.

Open the URL in your browser and enter a website URL to begin the analysis.

🧪 Example Detection Workflow
👤 User
   │
   ▼
🔗 Enter URL
   │
   ▼
🔍 Extract URL Features
   │
   ▼
📊 Generate Feature Vector
   │
   ▼
🤖 Ensemble Prediction
   │
   ▼
📈 Calculate Probability
   │
   ▼
┌──────────────────────────┐
│                          │
│ 🟢 LEGITIMATE            │
│          OR              │
│ 🔴 PHISHING              │
│                          │
└──────────────────────────┘
   │
   ▼
🔬 View Extracted Features
⚠️ Limitations

Although the system provides a machine-learning-based approach to phishing URL detection, several limitations remain.

🔗 1. URL-Level Analysis

The current system primarily focuses on URL-based characteristics. It does not completely analyze webpage HTML, JavaScript behavior, visual similarity, or the full content of a website.

🆕 2. Zero-Day Phishing

New phishing campaigns may introduce URL patterns that differ significantly from the training data. Completely novel attack patterns can therefore be challenging to detect.

📚 3. Dataset Dependency

Machine learning performance depends strongly on the quality, diversity, and representativeness of the datasets used for training and evaluation.

🔄 4. Concept Drift

Phishing techniques continuously evolve. Changes in attacker strategies can reduce model performance over time if the model is not periodically retrained.

🌐 5. Limited Contextual Information

URL-level analysis does not fully incorporate information such as:

🌍 Domain reputation
🕐 Domain age
🔐 SSL/TLS certificate information
🌐 DNS characteristics
📄 Website content
🔀 Redirect behavior
🧠 JavaScript activity
⚖️ 6. False Positives & False Negatives

No machine learning classifier is perfect.

A legitimate URL may occasionally be classified as suspicious (false positive), while a sophisticated phishing URL may be classified as legitimate (false negative).

Therefore, the system should be considered a decision-support tool rather than a standalone cybersecurity solution.

🔬 7. Explainability Scope

The current explainability approach focuses primarily on extracted URL-level characteristics. Future versions can provide richer model-level explanations and more detailed visual interpretations.

🖥️ 8. Deployment Scope

The current implementation is primarily designed as a research and demonstration application. Production deployment would require additional security hardening, monitoring, scalability, authentication, and continuous model updates.

🚀 Future Improvements

The project can be extended into a more comprehensive cybersecurity platform.

🌐 Website Intelligence
HTML and DOM analysis
JavaScript behavior analysis
Website screenshot analysis
Visual similarity detection
🔐 Domain Intelligence
Domain age
DNS information
SSL/TLS certificate analysis
WHOIS-based features
Domain reputation
🧠 Advanced AI
Deep learning-based URL representations
Transformer-based models
Advanced ensemble strategies
Rich SHAP visualizations
⚡ Real-Time Security
Threat intelligence integration
Continuous URL monitoring
Browser extension
Real-time alerts
☁️ Deployment
REST API
Cloud deployment
Scalable inference service
Production monitoring
🔐 Security Disclaimer

This project is intended for:

🎓 Educational • 🔬 Research • 🛡️ Defensive Cybersecurity

The prediction generated by the system should not be treated as an absolute guarantee that a website is safe or malicious.

Users should not enter passwords, financial information, API keys, or other sensitive information into websites solely because the model classifies them as legitimate.


📚 Research Connection
This implementation supports the research work:

"An Explainable Machine Learning Framework for Real-Time Phishing Website and URL Detection Using Ensemble Classifiers"

The project demonstrates the practical implementation of:

🔍 URL Feature Engineering

→ 🤖 Ensemble Classification

→ 📊 Model Evaluation

→ 🌍 External Testing

→ 🔬 Explainability

→ 🌐 Interactive Deployment

🎓 Research Contributions

The project focuses on the following contributions:

🧩 1. URL-Centric Feature Engineering

Transforms raw URLs into structured machine-learning representations.

🤖 2. Ensemble-Based Detection

Uses ensemble learning to capture complementary patterns within URL features.

🔬 3. Explainability-Oriented Analysis

Moves beyond binary classification by exposing feature-level information.

🌍 4. External Evaluation

Investigates model behavior using external URL samples.

🌐 5. Practical Deployment

Transforms the research pipeline into an interactive web-based application.

🗺️ Project Roadmap
✅ URL Feature Engineering
       ↓
✅ Machine Learning Models
       ↓
✅ Ensemble Classification
       ↓
✅ Model Evaluation
       ↓
✅ External Evaluation
       ↓
✅ Interactive Streamlit Application
       ↓
🔄 Advanced Explainability
       ↓
🔮 Real-Time Threat Intelligence
       ↓
🔮 Browser Extension
       ↓
🔮 Production Deployment

👩‍💻 Author
Anushka Raj

🎓 Computer Science Engineering

💡 Interests:
Machine Learning • Explainable AI • Cybersecurity • Intelligent Systems

🔗 GitHub:
https://github.com/anushka122-raj

⭐ Support the Project

If you find this project useful for:

🎓 Learning
🔬 Research
🛡️ Cybersecurity
🤖 Machine Learning

consider giving the repository a ⭐ on GitHub!
