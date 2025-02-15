import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()
        
        if "emotionPredictions" in response_json and len(response_json["emotionPredictions"]) > 0:
            emotions = response_json["emotionPredictions"][0]["emotion"]
            dominant_emotion = max(emotions, key=emotions.get)  # Find the highest scoring emotion
            emotions["dominant_emotion"] = dominant_emotion
            return emotions
        else:
            return {"error": "Unexpected response format", "response": response_json}
    else:
        return {"error": f"Error: {response.status_code}, {response.text}"}

# Testing the function
if __name__ == "__main__":
    test_text = "I am so happy I am doing this."
    print(emotion_detector(test_text))
