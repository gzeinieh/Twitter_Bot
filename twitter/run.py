from markov_python.cc_markov import MarkovChain
import sqlite3



mk = MarkovChain()


conn = sqlite3.connect('tweets.db')
c = conn.cursor()
c.execute("SELECT COUNT(DISTINCT tweet) from home_tweets")
num_rows = c.fetchone()[0]
c.execute("SELECT DISTINCT tweet from home_tweets")
tweets = c.fetchmany(num_rows)


for tweet in tweets:
    mk.add_string(list(tweet)[0])

all_status = []

for i in range(int(num_rows/50)):
    all_status.append(" ".join(mk.generate_text(20)))

with open("data/update_status.txt", 'wt') as f:
    for status in all_status:
        f.write(status)
        f.write("\n")

pass





