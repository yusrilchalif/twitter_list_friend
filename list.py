#using pyhton 2.7
import time
import tweepy           

#consumer & access token key
consumer_key        = ''
consumer_secret_key = ''
access_token        = ''
access_token_secret = ''

#OAuth with keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

#interface with authentication
#get followers with user FakhriyRN
api = tweepy.API(auth)
ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name = "FakhriyRN").pages():
        ids.extend(page)
        time.sleep(60)
print ("followers"), len(ids)

