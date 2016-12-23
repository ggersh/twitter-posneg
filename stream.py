from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import time
from TweetClean import *
from nltk.corpus import wordnet
import nltk



ckey = 'XXXXX'
csecret = 'XXXXXX'
atoken = 'XXXXXXXX'
asecret = 'XXXXXXXXX'

class listener(StreamListener):

    def __init__(self):
        self.tweets = []

    def on_data(self,data):



            tweet = data.split(',"text":"')[1].split('","source')[0]


            sentence = clean(tweet)


            a = ', '.join(str(x) for x in sentence)



            saveFile = open('newTwitDB.csv','a')
            saveFile.write(a)
            saveFile.write('\n')
            saveFile.close()
            return True



    def on_error(self,status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track = ["hate"])
