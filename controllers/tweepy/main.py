from configurations.tweepy import twitter_api

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

      tweets.append({
          "id": tweet.id,
          "url":
          f"http://twitter.com/{tweet.user.screen_name}/status/{tweet.id}",
          "text": full_text
      })

  return {
      "keyword": keyword,
      "amount": len(tweets),
      "results": tweets
  }
