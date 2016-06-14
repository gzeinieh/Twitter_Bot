from tweepy import Stream
from tweepy.streaming import StreamListener
import sqlite3
import time
from datetime import datetime
import json
from twitter_auth import T

auth = T.auth


conn = sqlite3.connect('tweets.db')
c = conn.cursor()



class Listener(StreamListener):

    def __init__(self, filter_by, time_limit):
        """

        :param filter_by: the word to search for
        :param time_limit: the duration of the streaming
        """
        super().__init__()
        self.filter_by = filter_by
        self.time_limit = time_limit * 60
        self.start_time = time.time()

    def on_data(self, data):
        """

        :param data: data from twitter api
        :return: process data and save it to database
        """
        if (time.time() - self.start_time) < self.time_limit:
            all_data = json.loads(data)

            tweet = all_data["text"]

            username = all_data["user"]["screen_name"]

            ID = all_data["id_str"]

            dt = datetime.today()

            time_stamp = int(time.mktime(dt.timetuple())*1000)

            c.execute("INSERT INTO streaming_tweets VALUES (?,?,?,?,?,?)",
                      (ID, username, time_stamp, str(datetime.today()), tweet, self.filter_by))

            conn.commit()

            print((username, tweet))

            return True
        else:
            conn.commit()
            conn.close()
            return False

    def on_error(self, status):
        """

        :param status: error
        :return: deal with twitter 420 api error (420: when making many wrong streaming api requests)
        """
        if status == 420:
            print(status)
            return False


twitterStream = Stream(auth, Listener(filter_by="#Buffon", time_limit=1))
twitterStream.filter(track=["#Buffon"])
# twitterStream.filter(track=["azzurri"], async = True) # will run on a new thread
