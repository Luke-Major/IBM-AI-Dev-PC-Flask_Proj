"""
Flask server for emotion detection
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/")
def home():
    """
    Render the home page.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    """
    Endpoint for emotion detection.
    """
    # Get the 'textToAnalyze' query parameter from the request
    text = request.args.get('textToAnalyze')

    # Handle the case where no text is provided or only whitespace
    if not text or not text.strip():
        return "Invalid text! Please try again!", 400

    # Call the emotion_detector function and capture its output
    result = emotion_detector(text)

    # Check if the result is None, indicating an invalid or blank input
    if all(value is None for value in result.values()):
        return "Invalid text! Please try again!", 400

    # Return the result as a string
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
