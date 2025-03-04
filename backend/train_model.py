import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset (adjust path if needed)
df = pd.read_csv('/home/proffessor/phishing-website-detection/backend/data/phishing_site_urls.csv') # Assuming it's in the same directory

# Drop unnecessary columns if needed (like index, etc.)
if 'index' in df.columns:
    df = df.drop(['index'], axis=1)

# Split features and labels
X = df.drop(['Result'], axis=1)
y = df['Result']

# Print the feature columns used in training
print(f"Features used for training: {list(X.columns)}")

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(f"Model accuracy: {accuracy_score(y_test, y_pred)}")

# Save trained model
joblib.dump(model, 'phishing_model.pkl')
print("Model training complete. Saved as 'phishing_model.pkl'.")
