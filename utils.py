# utils.py
import re

def analyze_links(text):
    # This is a simple example to find URLs in the given text
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return {"urls": urls, "analysis": "Suspicious" if urls else "No links found"}

def user_guidance(prediction):
    if prediction == 'phishing':
        return "This email is suspicious. Do not click on any links or download attachments without verifying the source."
    else:
        return "This email appears to be safe. Always stay vigilant against potential threats."
