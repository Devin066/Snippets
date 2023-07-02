import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

def analyze_text(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove punctuation and stopwords
    stopwords_set = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in stopwords_set]

    # Count word frequency
    word_freq = Counter(words)

    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Perform sentiment analysis
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = [sia.polarity_scores(sentence) for sentence in sentences]
    overall_sentiment = sum(score['compound'] for score in sentiment_scores) / len(sentiment_scores)

    return {
        'word_frequency': dict(word_freq),
        'sentence_count': len(sentences),
        'word_count': len(words),
        'overall_sentiment': overall_sentiment,
        'sentiment_scores': sentiment_scores
    }

# Example usage
text = """
The quick brown fox jumps over the lazy dog. The dog, however, doesn't seem to care. 
The cat is also unimpressed. This is just a sample text for demonstration purposes.
"""

analysis_result = analyze_text(text)
print("Word frequency:", analysis_result['word_frequency'])
print("Sentence count:", analysis_result['sentence_count'])
print("Word count:", analysis_result['word_count'])
print("Overall sentiment:", analysis_result['overall_sentiment'])
print("Sentiment scores:", analysis_result['sentiment_scores'])
