from app_types.main import PostNewVoteProps
from database.main import firebase
from urllib.error import HTTPError
from configurations.tweepy import twitter_api
from controllers.helpers.main import clear_text, pre_processamento

async def post_vote_new(vote_data: PostNewVoteProps):
  try:
    db = firebase.database()

    item_to_save = {
      "id": vote_data.id,
      "tweet_text": pre_processamento(vote_data.tweet_text),
      "sentiment": vote_data.sentiment
    }

    print(item_to_save)
    return item_to_save

  except HTTPError as error:
    return { "status": 400, "message": "Houve um erro ao salvar a votação." }

async def get_by_keyword(keyword: str):
  amount = 5
  query_results = twitter_api.search_tweets(q=keyword, count=amount, lang="pt-br", tweet_mode="extended")

  tweets = []
  if len(query_results) > 0:
    for tweet in query_results:
      tweet_details = twitter_api.get_status(tweet.id, tweet_mode="extended")

      full_text = tweet.full_text

      if tweet_details is not None:
        if tweet_details.retweeted is True:
            full_text = tweet_details.retweeted_status.full_text
        else:
            full_text = tweet_details.full_text
      tweet_item = {
          "id": tweet.id,
          "url":
          f"http://twitter.com/{tweet.user.screen_name}/status/{tweet.id}",
          "keyword": keyword,
          "text": clear_text(full_text)
      }

      tweets.append(tweet_item)

  return {
      "keyword": keyword,
      "amount": len(tweets),
      "results": tweets
  }

async def get_tweets_pre():
  try:
    db = firebase.database()
    pre_tweets = db.child("pre_tweets").get()

    response = []
    for tweet in pre_tweets.each():
      response.append(tweet.val())

    return { "status": 200, "amount": len(response), "pre_tweets": response }

  except HTTPError as error:
    return { "status": 400, "message": "Houve um erro ao obter os tweets." }

async def populate(keyword: str):
  try:
    db = firebase.database()

    amount = 5
    query_results = twitter_api.search_tweets(q=keyword, count=amount, lang="pt-br", tweet_mode="extended")

    if len(query_results) > 0:
      for tweet in query_results:
        tweet_details = twitter_api.get_status(tweet.id, tweet_mode="extended")

        full_text = tweet.full_text

        if tweet_details is not None:
          if tweet_details.retweeted is True:
              full_text = tweet_details.retweeted_status.full_text
          else:
              full_text = tweet_details.full_text

        tweet_item = {
            "id": tweet.id,
            "url":
            f"http://twitter.com/{tweet.user.screen_name}/status/{tweet.id}",
            "keyword": keyword,
            "text": clear_text(full_text)
        }

        db.child("pre_tweets").push(tweet_item)

      return { "status": 200, "message": "Banco de dados populado com  sucesso" }
  except HTTPError as error:
    return { "status": 400, "message": "Houve um erro ao popular o banco de dados." }