from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get('url')

    # Placeholder logic (replace with actual ML logic later)
    result = {
        "url": url,
        "phishing": False,
        "confidence": 0.0,
        "explanation": "Model not implemented yet"
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
