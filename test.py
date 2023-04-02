from flask import Flask, request
from googleapiclient.discovery import build
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/sentiment', methods=['GET'])
def analyze_sentiment():
    video_id = request.args.get('video_id')

    # Get YouTube video comments
    youtube = build('youtube', 'v3', developerKey="AIzaSyCtgINjW_z1Yr9WIsecxBzn-BkKE9RmDf0")
    comments = []
    results = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText'
    ).execute()
    print("result - {results}")
    for item in results['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    # Perform sentiment analysis
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = []
    for comment in comments:
        sentiment_scores.append(sia.polarity_scores(comment))

    return {'sentiment_scores': sentiment_scores}

if __name__ == '__main__':
    app.run()
