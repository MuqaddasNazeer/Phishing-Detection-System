import re

def analyze_links(text):
    # Regex to find URLs
    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
    urls = url_pattern.findall(text)
    if not urls:
        return {"found": False, "urls": [], "message": "No URLs found."}
    
    # Example: Check if any URLs are considered suspicious
    suspicious_urls = [url for url in urls if "bit.ly" in url]
    if suspicious_urls:
        return {"found": True, "urls": suspicious_urls, "message": "Suspicious URLs found: " + ", ".join(suspicious_urls)}
    
    return {"found": True, "urls": urls, "message": "No suspicious URLs detected."}
