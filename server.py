"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the emotion detection home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """Analyze the text provided by the user."""
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Please enter some text to analyze."

    response = emotion_detector(text_to_analyze)
    return str(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
