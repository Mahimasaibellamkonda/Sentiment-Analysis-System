from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, round(polarity, 2), round(subjectivity, 2)


@app.route("/", methods=["GET", "POST"])
def index():

    text = ""
    sentiment = None
    polarity = None
    subjectivity = None

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if text:
            sentiment, polarity, subjectivity = analyze_sentiment(text)

    return render_template(
        "index.html",
        text=text,
        sentiment=sentiment,
        polarity=polarity,
        subjectivity=subjectivity
    )


if __name__ == "__main__":
    app.run(debug=True)
