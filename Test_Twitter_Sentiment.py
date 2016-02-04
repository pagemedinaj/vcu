from pattern.web import Crawler
from pattern.web import download
from pattern.web import plaintext
from textblob import TextBlob

from pattern.web import Twitter
t = Twitter()
i = None
for j in range(1):
    for tweet in t.search('#SuperBowl', start=i, count=40):
       # print tweet.id
       # print tweet.name
        print tweet.text
       # print tweet.coordinates
        print
    blob = TextBlob(plaintext(tweet.text))
    for sentence in blob.sentences:
            print(sentence.sentiment.polarity)

