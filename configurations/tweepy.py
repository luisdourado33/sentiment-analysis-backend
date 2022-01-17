import tweepy

consumer_key = "3iCmhmWKnj92SW2GtDZuykwFN"
consumer_secret = "Nfnn2fEtXN3rcUm6ehZ5Et37CJMPTlK953inlbak1hQJYl3bts"

access_token = "1131345642-5AQCy4nfpQdAlsGIihHEU2GKlpAcz6eg3RkLMoq"
access_token_secret = "naOB9jokowrMK2ofK48TQoopzytbjAcGOkD0LfgkDZOLC"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(auth, wait_on_rate_limit=True)