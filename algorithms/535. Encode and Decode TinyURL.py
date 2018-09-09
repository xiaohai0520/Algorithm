from random import choice
class Codec:

    def __init__(self):
        self.TinyToLong = {}
        self.LongToTiny = {}
        self.rand_scope = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.LongToTiny:
            return self.LongToTiny[longUrl]
        Url_main = longUrl.split('/')[-1]
        res = ''
        for c in Url_main:
            res += choice(self.rand_scope)
        shortUrl = 'http://tinyurl.com/' + res
        self.LongToTiny[longUrl] = shortUrl
        self.TinyToLong[shortUrl] = longUrl
        return shortUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.TinyToLong[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
