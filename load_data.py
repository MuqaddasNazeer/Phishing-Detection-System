from ucimlrepo import fetch_ucirepo
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

# Fetch and prepare data
spambase = fetch_ucirepo(id=94)
X = spambase.data['features']
y = spambase.data['targets']['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the split data
joblib.dump((X_train, X_test, y_train, y_test), 'train_test_data.pkl')