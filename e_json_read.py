#----------------------------------------------------------------------------------------------#
#                                       Created/Credited by                                    #
#                                Kibeom Alex Hong & Sol Peter Won                              #
#----------------------------------------------------------------------------------------------#


import json


lst = []

#-----------------------------------------------------------------------

# OPEN JSON file
json_data=open("live_tweets_recorded.txt", "r")
#               ^^^^^^^^^^^^^^^^^^^^^^^^

#-----------------------------------------------------------------------

for line in json_data:
    try:
        tweet = json.loads(line)
        lst.append(tweet)
    except:
        continue


created_at = open("created_at.txt","w")
ids = open("tweet_ids.txt","w")
text = open("text.txt","w")
retweeted = open("retweeted.txt","w")

id_str = open("id_str.txt","w")
name = open("name.txt","w")
location = open("location.txt","w")
profile_img_url = open("profile_img_url.txt","w")
user_created_at = open("user_created_at.txt","w")
verified = open("verified.txt","w")
protected = open("protected.txt","w")
favourites_count = open("favourites_count.txt","w")
followers_count = open("followers_count.txt","w")
friends_count = open("friends_count.txt","w")
statuses_count = open("statuses_count.txt","w")
screen_name = open("screen_name.txt","w")
lang = open("lang.txt","w")

#-----------------------------------------------------------------------
for i in lst:
    created_at.write((json.dumps(i["created_at"]).strip()).replace('"','') + "\n")                   
    ids.write((json.dumps(i["id"]).strip()).replace('"','') + "\n")
    text.write((json.dumps(i["text"]).strip()).replace('"','') + "\n")
    retweeted.write((json.dumps(i["retweeted"]).strip()).replace('"','') + "\n")

    

    id_str.write((json.dumps(i["user"]["id_str"]).strip()).replace('"','') + "\n")
    name.write((json.dumps(i["user"]["name"]).strip()).replace('"','') + "\n")
    location.write((json.dumps(i["user"]["location"]).strip()).replace('"','') + "\n")
    profile_img_url.write((json.dumps(i["user"]["profile_image_url"]).strip()).replace('"','') + "\n")
    user_created_at.write((json.dumps(i["user"]["created_at"]).strip()).replace('"','') + "\n")
    verified.write((json.dumps(i["user"]["verified"]).strip()).replace('"','') + "\n")
    protected.write((json.dumps(i["user"]["protected"]).strip()).replace('"','') + "\n")
    favourites_count.write((json.dumps(i["user"]["favourites_count"]).strip()).replace('"','') + "\n")
    followers_count.write((json.dumps(i["user"]["followers_count"]).strip()).replace('"','') + "\n")
    friends_count.write((json.dumps(i["user"]["friends_count"]).strip()).replace('"','') + "\n")
    statuses_count.write((json.dumps(i["user"]["statuses_count"]).strip()).replace('"','') + "\n")
    screen_name.write((json.dumps(i["user"]["screen_name"]).strip()).replace('"','') + "\n")
    lang.write((json.dumps(i["user"]["lang"]).strip()).replace('"','') + "\n")

    

created_at.close()
ids.close()
text.close()
retweeted.close()

id_str.close()
name.close()
location.close()
profile_img_url.close()
user_created_at.close()
verified.close()
protected.close()
favourites_count.close()
followers_count.close()
friends_count.close()
statuses_count.close()
screen_name.close()
lang.close()




print "Done"




#-----------------------------------------------------------------------
