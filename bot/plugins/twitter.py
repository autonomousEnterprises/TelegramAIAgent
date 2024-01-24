# from .plugin import Plugin
import tweepy

# Replace these with your own keys
access_token = 'SZ6lg4i2GJpXWMFC7TaDAFUSE'
access_token_secret = 'Qc77SyhlaR3Dr1dsWV9zD61Z44al6nWwRbArS2nGIDmHp6Za2u'

# Authenticate to Twitter
auth = tweepy.OAuth2AppHandler(access_token, access_token_secret)
api = tweepy.API(auth)
# Create API object
api = tweepy.API(auth)

# Fetch user's tweets
tweets = api.user_timeline(screen_name='username', count=2)

for tweet in tweets:
    print(tweet.text)
