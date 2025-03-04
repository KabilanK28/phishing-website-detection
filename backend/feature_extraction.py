import numpy as np
from urllib.parse import urlparse

# Corrected EXPECTED_FEATURES list
EXPECTED_FEATURES = [
    'having_IP_Address', 'URL_Length', 'Shortining_Service',
    'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix',
    'having_Sub_Domain', 'SSLfinal_State', 'Domain_registeration_length',
    'Favicon', 'port', 'HTTPS_token', 'Request_URL', 'URL_of_Anchor',
    'Links_in_tags', 'SFH', 'Submitting_to_email', 'Abnormal_URL', 'Redirect',
    'on_mouseover', 'RightClick', 'popUpWidnow', 'Iframe', 'age_of_domain',
    'DNSRecord', 'web_traffic', 'Page_Rank', 'Google_Index',
    'Links_pointing_to_page', 'Statistical_report'
]

# Whitelisted domains (optional for trusted URLs)
WHITELISTED_DOMAINS = [
    "paypal.com",
    "google.com",
    "amazon.com",
    "microsoft.com",
    "facebook.com"
]

def is_whitelisted_domain(url):
    hostname = urlparse(url).hostname
    return any(domain in hostname for domain in WHITELISTED_DOMAINS)


# Dummy placeholder - you should replace with your real feature extraction functions
def extract_features(url):
    # Example feature values (replace with actual feature extraction logic)
    extracted_features = {
        'having_IP_Address': 1,
        'URL_Length': 0,
        'Shortining_Service': 1,
        'having_At_Symbol': 0,
        'double_slash_redirecting': 0,
        'Prefix_Suffix': 1,
        'having_Sub_Domain': 2,
        'SSLfinal_State': 1,
        'Domain_registeration_length': 1,
        'Favicon': 1,
        'port': 0,
        'HTTPS_token': 1,
        'Request_URL': 1,
        'URL_of_Anchor': 1,
        'Links_in_tags': 1,
        'SFH': 1,
        'Submitting_to_email': 0,
        'Abnormal_URL': 1,
        'Redirect': 0,
        'on_mouseover': 0,
        'RightClick': 1,
        'popUpWidnow': 0,
        'Iframe': 0,
        'age_of_domain': 1,
        'DNSRecord': 1,
        'web_traffic': 1,
        'Page_Rank': 1,
        'Google_Index': 1,
        'Links_pointing_to_page': 1,
        'Statistical_report': 1
    }
    return extracted_features


def generate_features_for_url(url):
    # If the URL is from a trusted (whitelisted) domain, return all zero features (optional logic)
    if is_whitelisted_domain(url):
        return np.array([[0] * len(EXPECTED_FEATURES)])

    # Otherwise, extract real features
    extracted_features = extract_features(url)

    # Make sure all expected features exist, filling in any missing with 0
    complete_features = {feature: extracted_features.get(feature, 0) for feature in EXPECTED_FEATURES}

    # Convert the features into a numpy array for prediction (shape: 1 row of features)
    return np.array([list(complete_features.values())])
