let RunSentimentAnalysis = () => {
    // Get the text value from the input field
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    // Encode the text to handle special characters in the URL
    let encodedText = encodeURIComponent(textToAnalyze);

    // Create a new XMLHttpRequest object
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Update the 'system_response' div with the server's response
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };

    // Open a GET request to the Flask route with the encoded text
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodedText, true);
    xhttp.send();
};