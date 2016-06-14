import tweepy
import csv
from twitter_auth import T

api = T.api


def get_all_tweets_one_user(screen_name):
    """

    :param screen_name:
    :return:

    #get_all_tweets_one_user('gianluigibuffon')
    #get_all_tweets_one_user('Pirlo_official')
    """
    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)


    # save the id of the oldest tweet less one
    if len(alltweets) > 0:
        oldest = int(alltweets[-1].id_str) - 1

    # keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:

            # all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

            # save most recent tweets
            alltweets.extend(new_tweets)

            # update the id of the oldest tweet less one
            oldest = int(alltweets[-1].id_str) - 1

    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]

    with open(screen_name + "_tweets.csv", 'wt') as f:
        writer = csv.writer(f)
        writer.writerows(outtweets)

    pass


    return alltweets
