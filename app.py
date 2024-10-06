from flask import Flask, request, jsonify, render_template
import joblib
from link_analysis import analyze_links

app = Flask(__name__)

# Load the trained model
model = joblib.load('model/phishing_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form.get('email', '')
    if not email_text:
        return jsonify({"error": "No email text provided"}), 400

    # Predict the category of the email
    prediction = model.predict([email_text])[0]
    proba = model.predict_proba([email_text])[0]
    max_proba = max(proba)

    response = {
        'prediction': prediction,
        'confidence': f"{max_proba:.2%}",
    }

    # Only provide link analysis and phishing reporting link if predicted as phishing
    if prediction.lower() == 'phishing':
        link_analysis_result = analyze_links(email_text)
        response.update({
            'links': link_analysis_result['urls'],  # List of URLs found
            'link_message': link_analysis_result['message'],  # Message about the nature of the URLs
            'report_phishing_url': "https://safebrowsing.google.com/safebrowsing/report_phish/?hl=en"  # Google's phishing report URL
        })
    else:
        response.update({
            'links': [],
            'link_message': "No suspicious links detected as the email is not identified as phishing.",
            'report_phishing_url': None  # No link provided for safe emails
        })

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
