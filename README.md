# Sentiment Analysis System

A web-based Sentiment Analysis System developed using Python, Flask, and TextBlob. The application analyzes user-provided text and determines whether the sentiment is Positive, Negative, or Neutral.

## Features

* Simple and user-friendly web interface
* Accepts text input from users
* Performs sentiment analysis
* Classifies text as Positive, Negative, or Neutral
* Displays polarity score
* Displays subjectivity score
* Flask-based web application
* NLP-based text analysis using TextBlob

## Technologies Used

* Python
* Flask
* TextBlob
* HTML
* CSS
* Natural Language Processing (NLP)

## Project Structure

```text
Sentiment-Analysis-System/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the following command:

```bash
python app.py
```

Open the application in a web browser:

```text
http://127.0.0.1:5000
```

## Example

### Input

```text
I really enjoyed this movie. It was amazing!
```

### Output

```text
Sentiment: Positive
```

The system also displays polarity and subjectivity scores.

## How It Works

1. The user enters text into the webpage.
2. The text is sent to the Flask backend.
3. TextBlob analyzes the text.
4. A polarity score is calculated.
5. The polarity score is used to classify the sentiment.
6. The result is displayed on the webpage.

## Applications

Sentiment analysis can be used for:

* Customer review analysis
* Social media monitoring
* Product feedback analysis
* Movie and restaurant reviews
* Customer satisfaction analysis

## Purpose

This project demonstrates the use of Natural Language Processing and Text Analysis techniques in a web-based application.

## License

This project is licensed under the MIT License.
