import time 
import tweepy

#consumer & access token key
consumer_key        = 'HIDg3TUD64usi0HCzulWRf8O0'
consumer_secret_key = 'qj8s3uznzhI8IUJmrbHsoFaV995VmUlWr5o4xgWNKNoKV6wzhh'
access_token        = '919474569261367297-x46bWTtlMGqTaGpvJ3zbXNhGVI1bs2F'
access_token_secret = '79QR2p1tNKA2yaW0av1jfv8p78KM4vkA3pjLSKh6x3t5b'

#variable untuk menyimpan user followers
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
    #print user.screen_name
    print user.followers_count
