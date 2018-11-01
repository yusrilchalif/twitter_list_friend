import tweepy

#consumer & access token key
consumer_key        = 'HIDg3TUD64usi0HCzulWRf8O0'
consumer_secret_key = 'qj8s3uznzhI8IUJmrbHsoFaV995VmUlWr5o4xgWNKNoKV6wzhh'
access_token        = '919474569261367297-x46bWTtlMGqTaGpvJ3zbXNhGVI1bs2F'
access_token_secret = '79QR2p1tNKA2yaW0av1jfv8p78KM4vkA3pjLSKh6x3t5b'

#OAuth with keys and tokens
auth = tweepy.OAuthHandler(HIDg3TUD64usi0HCzulWRf8O0, qj8s3uznzhI8IUJmrbHsoFaV995VmUlWr5o4xgWNKNoKV6wzhh)
auth.set_access_token(919474569261367297-x46bWTtlMGqTaGpvJ3zbXNhGVI1bs2F, 79QR2p1tNKA2yaW0av1jfv8p78KM4vkA3pjLSKh6x3t5b)

#interface with authentication
api = tweepy.API(auth)

#get all followers user
friends = api.friends_ids()
