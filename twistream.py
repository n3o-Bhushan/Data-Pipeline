#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt

access_token = "842328502229598208-Xiv3DnlPD4oTC7mXXQk8JQmlxgrqS1e"
access_token_secret = "BnFd9gePFUxCkydqJfjnBS9jTpmBvCLHEBPeVwprLq2hJ"
consumer_key = "rmOUn4KvriYHVZAKqjOvKYUhs"
consumer_secret = "GB8YTREn8ojujP8a3pj4Ep9Bsu0vOWXSiMu7fGIWyw5GUGX2BL"

class StdOutListener(StreamListener):

    def on_data(self, data):
        # with open('stream.txt', 'a') as the_file:
        #  the_file.write(data)
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)


    #This line filter Twitter Streams to capture data by the keywords: 'Prague'
    stream.filter(track=['Prague'])


    data = 'stream.txt'

    tweets_data = []
    tweets_file = open(data, "r")
    for line in tweets_file:
      try:
           tweet = json.loads(line)
           tweets_data.append(tweet)
           print tweets_data
      except:
            continue


