#----------------------------------------------------------------------------------------------#
#                                       Created/Credited by                                    #
#                                Kibeom Alex Hong & Sol Peter Won                              #
#----------------------------------------------------------------------------------------------#

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import time
import json


access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

# replace your tokens / keys into the " "


#----------------------------------------------------------------------------------------------#

auth = OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
auth.set_access_token(access_token, access_token_secret)


ids = open("ids_smithsonian.txt","r")

#            ^^^^^^^^^^^^^^^^^^

# "all_ids_by_100.txt" from "parse_100.py" goes in here, you may change the name of the file 

#----------------------------------------------------------------------------------------------#

content = ids.readlines()
print "--------------------------------"
print "Collecting Twitter User Data"
print "--------------------------------"
print "  "
print "100 users per # of trial."
print "  "
print "62 seconds rest every 12 trials."
print "  "
print "--------------------------------"
print "  Number of trials: " + str(len(content))
print "--------------------------------"
print "  "

#----------------------------------------------------------------------------------------------#


description_file = open("a_description.txt","w")
statuses_count_file = open("b_statuses_count.txt","w")
followers_count_file = open("c_followers_count.txt","w")
favourites_count_file = open("d_favourites_count.txt","w")
friends_count_file = open("e_friends_count.txt","w")
url_file = open("f_url.txt","w")
name_file = open("g_name.txt","w")
created_at_file = open("h_created_at.txt","w")
protected_file = open("i_protected.txt","w")
verified_file = open("j_verified.txt","w")
screen_name_file = open("k_screen_name.txt","w")
location_file = open("l_location.txt","w")
lang_file = open("m_lang.txt","w")
id_file = open("n_id.txt","w")
listed_count_file = open("o_listed_count.txt","w")
follow_request_sent_file = open("p_follow_request_sent.txt","w")
profile_image_url_file = open("q_profile_image_url.txt","w")

# creates the text file of the name you choose

#----------------------------------------------------------------------------------------------#

num = 0
print "# of trials:  "
for i in range(len(content)):
    num += 1
    # content is the input that takes 100 IDs per trial.
    
    print str(i+1)
    
    for user in api.lookup_users(user_ids=[content[i]]):
        
        description_file.write((json.dumps(user.description).strip()).replace('"','') + '\n')
        statuses_count_file.write((json.dumps(user.statuses_count).strip()).replace('"','') + '\n')
        followers_count_file.write((json.dumps(user.followers_count).strip()).replace('"','') + '\n')
        favourites_count_file.write((json.dumps(user.favourites_count).strip()).replace('"','') + '\n')
        friends_count_file.write((json.dumps(user.friends_count).strip()).replace('"','') + '\n')
        url_file.write((json.dumps(user.url).strip()).replace('"','') + '\n')
        name_file.write((json.dumps(user.name).strip()).replace('"','') + '\n')

        created_at_file.write(str(user.created_at) + '\n')
        
        protected_file.write((json.dumps(user.protected).strip()).replace('"','') + '\n')
        verified_file.write((json.dumps(user.verified).strip()).replace('"','') + '\n')
        screen_name_file.write((json.dumps(user.screen_name).strip()).replace('"','') + '\n')
        location_file.write((json.dumps(user.location).strip()).replace('"','') + '\n')
        lang_file.write((json.dumps(user.lang).strip()).replace('"','') + '\n')
        id_file.write((json.dumps(user.id).strip()).replace('"','') + '\n')
        listed_count_file.write((json.dumps(user.listed_count).strip()).replace('"','') + '\n')
        follow_request_sent_file.write((json.dumps(user.follow_request_sent).strip()).replace('"','') + '\n')
        profile_image_url_file.write((json.dumps(user.profile_image_url).strip()).replace('"','') + '\n')

      

        if num == 12:
            
            print "Wait 62 seconds."
            time.sleep(62)
            
            # Added extra 2 seconds for secure flow.

            num = 0


#----------------------------------------------------------------------------------------------#

description_file.close()
statuses_count_file.close()
followers_count_file.close()
favourites_count_file.close()
friends_count_file.close()
url_file.close()
name_file.close()
created_at_file.close()
protected_file.close()
verified_file.close()
screen_name_file.close()
location_file.close()
lang_file.close()
id_file.close()
listed_count_file.close()
follow_request_sent_file.close()
profile_image_url_file.close()

# file close

print "Done"

#----------------------------------------------------------------------------------------------#



# Open each file created, ctrl+a to select all. copy and paste each to the designated column in Microsoft Excel.




