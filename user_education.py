def get_education_content(prediction):
    if prediction == 1:
        return ("This email is flagged as phishing. Do not click on any links or download attachments.")
    else:
        return ("This email appears to be legitimate. Always stay cautious and verify emails.")
