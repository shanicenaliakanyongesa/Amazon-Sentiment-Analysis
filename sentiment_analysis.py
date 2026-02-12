import pandas
from textblob import TextBlob
import matplotlib.pyplot as plt

data = pandas.read_csv('amazon.csv')

# Clean data: remove rows with missing reviewText
data = data.dropna(subset=['reviewText'])

# Compute sentiment polarity for each reviewText
data['polarity'] = data['reviewText'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Add sentiment classification
def classify_sentiment(polarity):
    if polarity > 0.1:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'

data['sentiment'] = data['polarity'].apply(classify_sentiment)

# Analyze: compare sentiment with overall ratings
sentiment_rating = data.groupby('sentiment')['overall'].mean()
print("Average rating by sentiment:")
print(sentiment_rating)

# Visualize: bar chart of sentiment distribution
sentiment_counts = data['sentiment'].value_counts()
sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.savefig('sentiment_distribution.png')
plt.show()

print('Sentiment analysis completed. Bar chart saved as sentiment_distribution.png.')
