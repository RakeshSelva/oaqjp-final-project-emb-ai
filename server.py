"""
    This module is used to integrate the emotion detection NLP
    Application into a Flask Web Application
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route("/")
def render_index_page():
    """
        This function is used to render the index.html page
        as the home page of the application
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """
        This function is used to handle the GET request received
        at the endpoint 'emotionDetector'
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    out = 'For the given statement, the system response is '
    count = 0
    for key, value in response.items():
        if value is None:
            out = 'Invalid text! Please try again!.'
            break
        count += 1
        if key not in ['dominant_emotion']:
            if count < 5:
                out += "'" + key + "': " + str(value) + ', '
            else:
                out += "and '" + key + "': " + str(value) + '.  '
        else:
            out += f'The dominant emotion is {value}.'

    return out

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
