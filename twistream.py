#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "842328502229598208-Xiv3DnlPD4oTC7mXXQk8JQmlxgrqS1e"
access_token_secret = "BnFd9gePFUxCkydqJfjnBS9jTpmBvCLHEBPeVwprLq2hJ"
consumer_key = "rmOUn4KvriYHVZAKqjOvKYUhs"
consumer_secret = "GB8YTREn8ojujP8a3pj4Ep9Bsu0vOWXSiMu7fGIWyw5GUGX2BL"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['reykjavik'])
