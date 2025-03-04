# Phishing Website Detection using AI

## Project Overview
This project aims to detect phishing websites using Machine Learning models. It analyzes website URLs, content, and domain information to classify them as either phishing or legitimate.

## Folder Structure
- `backend/`: Contains Python Flask API and ML scripts.
- `backend/feature_extraction/`: Placeholder for feature extraction scripts.
- `backend/data/`: Folder to hold phishing and legitimate datasets.
- `backend/models/`: Folder to store trained models.

## Setup Instructions
1. Create a virtual environment.
2. Install dependencies:
    ```
    pip install -r backend/requirements.txt
    ```
3. Run the Flask API:
    ```
    python backend/app.py
    ```
4. Test the API with a POST request to:
    ```
    http://localhost:5000/predict
    ```

## Future Scope
- Adding real ML models for URL and content analysis.
- Developing a frontend UI (React.js).
- Adding a Chrome Extension for real-time phishing detection.
