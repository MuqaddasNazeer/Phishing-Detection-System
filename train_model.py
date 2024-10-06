import joblib
from sklearn.ensemble import RandomForestClassifier

# Load the split data
X_train, X_test, y_train, y_test = joblib.load('train_test_data.pkl')

# Create and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'phishing_model.pkl')