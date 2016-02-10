import sys
import tweepy
import codecs
from time import clock
import my_keys

# import time
# from tweepy import Stream
# from tweepy import OAuthHandler
# from tweepy.streaming import StreamListener
# import os

CONSUMER_KEY = my_keys.CONSUMER_KEY
CONSUMER_SECRET = my_keys.CONSUMER_SECRET
ACCESS_KEY = my_keys.ACCESS_KEY
ACCESS_SECRET = my_keys.ACCESS_SECRET
 

auth1 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth1.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth1)

# class MyStreamListener(tweepy.StreamListener):
#     def on_status(self, status):
#         print(status.text)
#     def on_error(self, status_code):
#         if status_code == 420:
#             return False

            
# myStreamListener = MyStreamListener()
# print(type(myStreamListener))
# myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

# print(myStream.filter(track=['#nycdh','#dh']))

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet = status.text
        user = status.author
        userid = status.author.id
        time = status.created_at
        source = status.source
        tweetid = status.id

        if not ('RT @' in tweet) :	

            print("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"" % (tweet,user,userid,time,source))

StreamListener = StreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=StreamListener)
            
myStream.filter(track=['python'])
