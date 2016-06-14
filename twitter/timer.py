from datetime import datetime
from threading import Timer
from twitter_api import get_home_tweets


def run_daily():
    """

    :return: run a function daily for 30 days
    """

    x = datetime.today()

    for day in range(30):
        y = x.replace(day=x.day + day, hour=x.hour, minute=x.minute, second=x.second, microsecond=x.microsecond)
        delta_t = y-x
        secs = delta_t.seconds+1
        t = Timer(secs, get_home_tweets)
        t.start()


def run_hourly():
    """

    :return: run a function hourly
    """

    x = datetime.today()

    for hour in range(24):
        y = x.replace(day=x.day, hour=x.hour + hour, minute=x.minute, second=x.second, microsecond=x.microsecond)
        delta_t = y-x
        secs = delta_t.seconds+1
        t = Timer(secs, get_home_tweets)
        t.start()
