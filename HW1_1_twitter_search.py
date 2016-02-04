from pattern.web import Twitter

t = Twitter()
i = None
for j in range(3):
    for tweet in t.search('SuperBowl', start=i, count=100):
        print tweet.id
        print tweet.name
        print tweet.text
        print tweet.coordinates
        print
