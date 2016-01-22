from pattern.web import Crawler
from pattern.web import download
from pattern.web import plaintext

class Wally(Crawler):
    def visit(self, link, source=None):
        print 'visited:', repr(link.url), 'from:', link.referrer
        print plaintext(download(link.url))

    def fail(self, link):
        print 'failed:', repr(link.url)

p = Wally(links=['http://www.cnbc.com/'], delay=1)
while not p.done:
    p.crawl(method=2, cached=False, throttle=1)
