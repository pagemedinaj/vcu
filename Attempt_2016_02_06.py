from pattern.web import Crawler
from pattern.web import download
from pattern.web import plaintext
from textblob import TextBlob

from pattern.web import Twitter

t = Twitter()
i = None
for j in range(4):
    for tweet in t.search('#SuperBowl', start=i, count=40):
       # print tweet.id
       # print tweet.name
        print tweet.text
       # print tweet.coordinates
        print
    blob = TextBlob(plaintext(tweet.text))
    for sentence in blob.sentences:
        print(sentence.sentiment.polarity)
        print blob.noun_phrases
        print blob.detect_language()
        print




#def fail(self, link):
 #       print 'failed:', repr(link.url)

#print blob.noun_phrases

#doc = {
#    'author': 'Timo Selvaraj',
#    'text': 'VCU is the best',
#    'tags': 'hello, world',
#    'timestamp: datetime.now'()
#    }
