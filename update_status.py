import  time, sys
from twitter.twitter_auth import T

api = T.api

argfile = str(sys.argv[1])

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:

    api.update_status(status=line)
    time.sleep(900)  # Tweet every 15 minutes

