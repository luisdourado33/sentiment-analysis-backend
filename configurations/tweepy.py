from dotenv import dotenv_values
import tweepy


config = dotenv_values(".env")

consumer_key = config['CONSUMER_KEY']
consumer_secret = config['CONSUMER_SECRET']

access_token = config['ACCESS_TOKEN']
access_token_secret = config['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(auth, wait_on_rate_limit=True)