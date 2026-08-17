import re
from urllib.parse import urlparse

SUSPICIOUS_WORDS = [
    "login", "verify", "verification", "update",
    "secure", "account", "bank", "confirm", "password"
]

def extract_features(url):
    parsed = urlparse(url if "://" in url else "http://" + url)
    domain = parsed.netloc
    path = parsed.path
    full_url = url.lower()

    return {
        "url_length": len(url),
        "domain_length": len(domain),
        "path_length": len(path),
        "dot_count": url.count("."),
        "hyphen_count": url.count("-"),
        "underscore_count": url.count("_"),
        "slash_count": url.count("/"),
        "question_count": url.count("?"),
        "equal_count": url.count("="),
        "at_count": url.count("@"),
        "digit_count": sum(c.isdigit() for c in url),
        "special_char_count": len(re.findall(r"[^a-zA-Z0-9]", url)),
        "subdomain_count": max(0, len(domain.split(".")) - 2),
        "has_https": int(url.lower().startswith("https")),
        "has_ip": int(bool(re.search(r"(\d{1,3}\.){3}\d{1,3}", domain))),
        "has_suspicious_word": int(any(word in full_url for word in SUSPICIOUS_WORDS))
    }