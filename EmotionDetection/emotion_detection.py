import requests
import json

def emotion_detector(text_to_analyze): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json =  { "raw_document": { "text": text_to_analyze }}
    response = requests.post(url, headers=headers, json=input_json)
    formatted_response = json.loads(response.text)
    formatted_dict = {}
    if response.status_code == 400:
        formatted_dict['anger'] = None
        formatted_dict['disgust'] = None
        formatted_dict['fear'] = None
        formatted_dict['joy'] = None
        formatted_dict['sadness'] = None
        formatted_dict['dominant_emotion'] = None
    else:
        emotions = formatted_response.get('emotionPredictions')[0].get('emotion')
        max_value = 0
        dom_emotion = ''
        for key, value in emotions.items():
            formatted_dict[key] = value
            if value > max_value:
                max_value = value
                dom_emotion = key
        formatted_dict['dominant_emotion'] = dom_emotion

    return formatted_dict
