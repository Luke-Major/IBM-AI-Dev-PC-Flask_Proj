import requests
import json
# Define the emotion detector function
def emotion_detector(text_to_analyze):
    # Check if the input text is blank
    if not text_to_analyze.strip():
        # Return a dictionary with None values for blank input
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "surprise": None
        }
    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    # Prepare the input data in the required JSON format
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    # Make the POST request to the API
    response = requests.post(url, headers=headers, data=json.dumps(input_data))
    # Check the response status code
    if response.status_code == 400:
        # Return a dictionary with None values if the server returns status code 400
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "surprise": None
        }
    # Parse the response JSON and extract the emotion predictions
    response_json = response.json()
    emotion_predictions = response_json["emotionPredictions"][0]["emotion"]
    return emotion_predictions