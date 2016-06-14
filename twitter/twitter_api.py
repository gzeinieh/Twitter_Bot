import tweepy
import csv
import time
from datetime import datetime
import sqlite3
from twitter_auth import T

api = T.api


def limit_handled(cursor):
    """

    :param cursor:
    :return:
    """
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


def follow_all_followers():
    """

    :return: follow all of auth's user followers
    """
    i = 0
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()
        i +=1
    return i


def friends_names():
    """
    :return: a list of auth user's friends' names

    """

    friends = []

    for friend in tweepy.Cursor(api.friends).items():
        friends.append(friend.screen_name)

    return friends


def get_home_tweets():
    """

    :return: csv with the last 200 tweets on the auth's home
    and send last 200 tweet to database
    """

    home_tweets = tweepy.Cursor(api.home_timeline).items(200)
    out_tweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in home_tweets]

    conn = sqlite3.connect('tweets.db')
    c = conn.cursor()
    # connect to database

    for tweet in out_tweets:
        c.execute("INSERT INTO home_tweets VALUES (?,?,?)",
                  (tweet[0], tweet[1], tweet[2]))

        conn.commit()
    # send tweets to database


    with open("data/" + str(datetime.today()) + "_home_tweets.csv", 'wt') as f:
        writer = csv.writer(f)
        writer.writerows(out_tweets)

    pass
    # send tweets to csv file

    return out_tweets


def get_all_tweets_one_user(screen_name):
    """

    :param screen_name:
    :return: csv with all tweets of a specified user

    get_all_tweets_one_user('gianluigibuffon')
    """

    all_tweets = tweepy.Cursor(api.user_timeline, screen_name=screen_name).items()

    out_tweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in all_tweets]

    with open("data/" + screen_name + "_tweets.csv", 'wt') as f:
        writer = csv.writer(f)
        writer.writerows(out_tweets)

    pass

    return out_tweets


def retweet(id_string):

    api.retweet(id_string)
    return
