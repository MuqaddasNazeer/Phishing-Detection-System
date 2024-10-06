document.addEventListener('DOMContentLoaded', function() {
    const checkButton = document.getElementById('checkEmail');

    checkButton.addEventListener('click', function() {
        const emailText = document.getElementById('emailText').value;
        fetch('/predict', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: 'email=' + encodeURIComponent(emailText)
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerHTML = `<strong>Prediction:</strong> ${data.prediction}<br><strong>Confidence:</strong> ${data.confidence}%<br><strong>Link Analysis:</strong> ${data.link_message}`;
            const phishingLink = document.getElementById('reportPhishingLink');
            if (data.prediction.toLowerCase() === 'phishing') {
                phishingLink.href = "https://safebrowsing.google.com/safebrowsing/report_phish/?hl=en";  // Change to actual URL if needed
                phishingLink.textContent = 'Report Phishing Here';
                phishingLink.style.display = 'inline';  // Make it visible as an inline element
            } else {
                phishingLink.style.display = 'none';  // Hide it if not phishing
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
