"""
Server module for emotion detection web application.

This module contains a Flask web server that serves as an API
for detecting emotions in text using the EmotionDetection package.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

def create_app():
    """Creates and configures the Flask app."""
    return app

@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_api():
    """Handles emotion detection requests via GET and POST methods."""
    if request.method == 'GET':
        text = request.args.get("text", "").strip()
    else:
        data = request.get_json()
        text = data.get("text", "").strip()

    if not text:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    emotions = emotion_detector(text)
    
    if emotions.get("dominant_emotion") is None:
        return jsonify({"response": "Invalid text! Please try again!"}), 400
    
    response_text = (
        f"For the given statement, the system response is 'anger': {emotions.get('anger')}, "
        f"'disgust': {emotions.get('disgust')}, 'fear': {emotions.get('fear')}, "
        f"'joy': {emotions.get('joy')} and 'sadness': {emotions.get('sadness')}. "
        f"The dominant emotion is {emotions.get('dominant_emotion')}."
    )

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)



