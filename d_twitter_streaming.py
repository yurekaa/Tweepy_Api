#----------------------------------------------------------------------------------------------#
#                                       Created/Credited by                                    #
#                                        Kibeom Alex Hong                                      #
#----------------------------------------------------------------------------------------------#


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# Your tokens / keys

#-----------------------------------------------------------------------

# Save JSON file to the text file
tweets = open("live_tweets_recorded.txt","w")

#-----------------------------------------------------------------------

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        tweets.write(data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords


#-----------------------------------------------------------------------
    
    stream.filter(track=['cephalopodweek'])
    #                     ^^^^^^^^^^^^^^
    #                      Hashtag

tweets.close()






#-----------------------------------------------------------------------
