import speech_recognition as sr
from flask import logging, Flask, render_template, request, flash
from textblob import TextBlob
import nltk
import pygame
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

app = Flask(__name__)
app.secret_key = "VatsalParsaniya"

@app.route('/')
def index():
    flash(" Welcome to Vatsal's site")
    return render_template('index.html')

@app.route('/audio_to_text/')
def audio_to_text():
    flash(" Press Start to start recording audio and press Stop to end recording audio")
    return render_template('audio_to_text.html')
# sentiment=""
# ctr=0
@app.route('/audio', methods=['POST'])
def audio():
    r = sr.Recognizer()
    with open('upload/audio.wav', 'wb') as f:
        f.write(request.data)
  
    with sr.AudioFile('upload/audio.wav') as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='en-IN', show_all=True)
        print(text)
        return_text = " Did you say : <br> "
        print(type(text))
        try:
            for num, texts in enumerate(text['alternative']):
                return_text += str(num+1) +") " + texts['transcript']  + " <br> "
            return_text+="<br> <br>" 
        except:
            return_text = " Sorry!!!! Voice not Detected "
        x=text['alternative'][0].values()
        print("x",str(x))
        
        # print("y",y)
    # Initialize the VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Define the text to be analyzed
    

    # Analyze sentiment
    scores = sid.polarity_scores(str(x))

    # Interpret sentiment scores
    if scores['compound'] > 0.05:
        sentiment = "Positive"
        ctr=1
    elif scores['compound'] < -0.05:
        sentiment = "Negative"
        ctr=1
    else:
        sentiment = "Neutral"
        ctr=1


    # Print sentiment scores and sentiment
    print("Sentiment Scores:", scores)
    print("Sentiment:", sentiment)
    
    sentence=return_text
    sentence+=" <h1> "+str(sentiment) +" </h1>"
    idx=sentence.rfind(" <br>")
    print(sentence[idx+4:])
    print(type(return_text))
        
    return str(sentence)

if __name__ == "__main__":
    app.run(debug=True)
