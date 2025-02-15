from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_api():
    if request.method == 'GET':
        text = request.args.get("text", "")
    else:
        data = request.get_json()
        text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    emotions = emotion_detector(text)
    response_text = (f"For the given statement, the system response is 'anger': {emotions['anger']}, "
                     f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, "
                     f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
                     f"The dominant emotion is {emotions['dominant_emotion']}.")

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

