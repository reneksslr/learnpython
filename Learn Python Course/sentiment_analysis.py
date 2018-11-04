import tweepy
from textblob import TextBlob
import csv

key = 'mELedUe0QY6DREixjNFOawZCo'
secret = 'HPx3QdVFyxKOimsAw3VeqiJxUZz6bY56OEcwRlg1rrswNDBI5l'

token = '956184427104751616-4v8zkShcYZRDY2KEWUu9k2rjtcWhObE'
token_secret = 'LG321fr61xsLjcwUbARe5s0aRzIYB4ry4HDfhsgaO9CLP'

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)

api = tweepy.API(auth)

with open('test.csv','w', encoding='utf-8') as csvfile:
    fieldnames = ['Sentiment','Tweet']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    tweets = api.search('bundesliga')
    writer.writeheader()
    for tweet in tweets:
        writer.writerow({'Sentiment': TextBlob(tweet.text).sentiment,'Tweet': tweet.text})
