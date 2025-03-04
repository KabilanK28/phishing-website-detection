from flask import Flask, request, jsonify
import joblib
import numpy as np
from feature_extraction import generate_features_for_url, EXPECTED_FEATURES

app = Flask(__name__)

# Load the trained model
model = joblib.load('phishing_model.pkl')

@app.route('/')
def home():
    return "Phishing Detection API is running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        url = data.get('url')

        if not url:
            return jsonify({'error': 'Missing URL'}), 400

        features = generate_features_for_url(url)

        # Ensure feature count matches model expectation
        if features.shape[1] != len(EXPECTED_FEATURES):
            return jsonify({
                'error': f'Feature mismatch. Expected {len(EXPECTED_FEATURES)}, got {features.shape[1]}'
            }), 500

        prediction = model.predict(features)[0]
        prediction_label = 'Phishing' if prediction == 1 else 'Legitimate'

        return jsonify({'prediction': prediction_label})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
