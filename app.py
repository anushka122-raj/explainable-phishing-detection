from urllib.parse import urlparse

import joblib
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🛡️",
)

st.title("🛡️ Explainable Phishing URL Detection")
st.write("Enter a URL below to check whether it may be phishing.")

model = joblib.load("models/ensemble_model.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

SUSPICIOUS_WORDS = [
    "login",
    "verify",
    "verification",
    "update",
    "secure",
    "account",
    "bank",
    "confirm",
    "password",
]

KNOWN_DOMAINS = {
    "google.com",
    "wikipedia.org",
    "microsoft.com",
    "github.com",
    "python.org",
    "stackoverflow.com",
    "apple.com",
}

def extract_features_from_url(url):
    clean_url = url.strip().lower()

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
        "sensitive_words_count": sum(word in clean_url for word in SUSPICIOUS_WORDS),
        "path_length": len(path),
        "isHttps": int(clean_url.startswith("https://")),
        "nb_dots": clean_url.count("."),
        "nb_hyphens": clean_url.count("-"),
        "nb_and": clean_url.count("&"),
        "nb_or": clean_url.count("|"),
        "nb_www": clean_url.count("www"),
        "nb_com": clean_url.count(".com"),
        "nb_underscore": clean_url.count("_"),
    }

    return pd.DataFrame([features])[feature_columns]

url = st.text_input(
    "Enter URL",
    placeholder="https://example.com",
)

if st.button("Check URL"):
    if not url.strip():
        st.warning("Please enter a URL first.")
    else:
        normalized_url = url.strip().lower()

        parsed_url = urlparse(
            normalized_url if "://" in normalized_url else "http://" + normalized_url
        )

        domain = parsed_url.netloc.lower()
        domain = domain.split(":")[0]
        domain = domain.removeprefix("www.")

        input_data = extract_features_from_url(normalized_url)

        if domain in KNOWN_DOMAINS:
            st.info(
                f"ℹ️ {domain} is a commonly recognized domain. "
                "It will be treated as safe."
            )
            st.subheader("Result")
            st.success("✅ The model does not flag this URL as suspicious.")
            st.metric("Phishing probability", "0.00%")
            with st.expander("View extracted features"):
                st.dataframe(input_data)
            st.stop()

        probability = model.predict_proba(input_data)[0][1]
        prediction = 1 if probability >= 0.85 else 0

        st.subheader("Result")

        if prediction == 1:
            st.error("⚠️ The model flags this URL as suspicious.")
        else:
            st.success("✅ The model does not flag this URL as suspicious.")

        st.metric("Phishing probability", f"{probability:.2%}")

        with st.expander("View extracted features"):
            st.dataframe(input_data)