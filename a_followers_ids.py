#----------------------------------------------------------------------------------------------#
#                                       Created/Credited by                                    #
#                                Kibeom Alex Hong & Sol Peter Won                              #
#----------------------------------------------------------------------------------------------#

import tweepy
import time

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# replace your tokens / keys into the " "

#----------------------------------------------------------------------------------------------#

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name = "AVMaltese").pages(131):
#                                                           ^^^^^^^^^    
# screen_name is where the userid is placed at.
# pages(#) is how many pages the Tweepy iterate through.
# For example, if there are 650.4k followers, since IDs can be pulled 5000 at a time,
# there will be 131 pages, 650.4k / 5000 = 130.8

    ids.extend(page)
    if len(page) == 5000 : time.sleep(65)
    
    # time.sleep(seconds) is at 65 seconds because there can be 15 requests per 15-min-window,
    # 60 seconds would work since 15/15 = 1 minute, but we gave extra 5 seconds for secure flow.

    print len(ids)
    
    # this will print out the length of how many ids are retrived. 

#----------------------------------------------------------------------------------------------#

files = open("scifri_followers_ids.txt","w")
#             ^^^^^^^^^^^^^^^^^^^^^^^^

# this is the name of the text file that will be developed on the
# same folder of where the file is stored at.

# You can select the name of your choice.



for item in ids:
  files.write("%s\n" % item)
files.close()

#----------------------------------------------------------------------------------------------#

# When all IDs are successfully pulled, you will have a text file created.




# Go To --> "parse_100.py"




#----------------------------------------------------------------------------------------------#
