import sqlite3
conn = sqlite3.connect('tweets.db')


c = conn.cursor()

# Create table
c.execute('''CREATE TABLE home_tweets
             (id integer, date numeric, tweet text)''')

c.execute('''CREATE TABLE streaming_tweets
    (id text, user text, date numeric, date_str text,tweet text, filter text)''')

# Save and close
conn.commit()

conn.close()
