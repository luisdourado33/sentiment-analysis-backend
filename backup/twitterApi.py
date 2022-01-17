from twitter.config import twitter_api
import tweepy as tw


def search():
    amount = 100
    query_results = twitter_api.search_tweets(q="bolsonaro",
                                              count=amount,
                                              lang="pt-br",
                                              tweet_mode="extended")

    tweets = []
    count = 0

    if len(query_results) > 0:
        for tweet in query_results:
            full_status = twitter_api.get_status(tweet.id,
                                                 tweet_mode="extended")
            tweet_text = tweet.full_text

            if full_status is not None:
                if full_status.retweeted is True:
                    tweet_text = full_status.retweeted_status.full_text
                else:
                    tweet_text = full_status.full_text

            tweets.append({
                "id": count,
                "url":
                f"twitter.com/{tweet.user.screen_name}/status/{tweet.id}",
                "text": tweet_text
            })
            count = count + 1

    return {"amount": count, "results": tweets}
