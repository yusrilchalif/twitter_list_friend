import time 
import tweepy

#consumer & access token key
consumer_key        = ''
consumer_secret_key = ''
access_token        = ''
access_token_secret = ''

akunVar = raw_input("Account name: ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

users = tweepy.Cursor(api.followers, screen_name = akunVar).items()

#program akan berhenti ketika telah menampilkan setiap 300 akun untuk 15 menit
while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break
    print '@' + user.screen_name
