import joblib
from sklearn.metrics import accuracy_score

# Load the model and data
model = joblib.load('phishing_model.pkl')
_, X_test, _, y_test = joblib.load('train_test_data.pkl')

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))