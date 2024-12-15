import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Define the text to be analyzed
text = "i am going to shoot him"

# Analyze sentiment
scores = sid.polarity_scores(text)

# Interpret sentiment scores
if scores['compound'] > 0.05:
    sentiment = "Positive"
elif scores['compound'] < -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Print sentiment scores and sentiment
print("Sentiment Scores:", scores)
print("Sentiment:", sentiment)