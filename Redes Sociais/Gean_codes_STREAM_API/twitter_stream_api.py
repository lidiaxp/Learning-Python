# -*- coding: utf-8 -*-
##### BEGIN IMPORT #####
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
try:
    import json
except ImportError:
    import simplejson as json
##### END IMPORT #####

##### BEGIN AUTHENTICATION #####
access_token = "INSERT_YOUR_ACCESS_TOKEN_HERE"
access_secret = "INSERT_YOUR_ACCESS_SECRET_HERE"
consumer_key = "INSERT_YOUR_CONSUMER_KEY_HERE"
consumer_secret = "INSERT_YOUR_CONSUMER_SECRET_HERE"

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

# conect to STREAM API
twitter_stream = TwitterStream(auth = oauth)
##### END AUTHENTICATION #####

# get some random tweets and save them to a file
# https://dev.twitter.com/streaming/reference/get/statuses/sample
tweet = twitter_stream.statuses.sample()
with open('public-tweets.txt', 'w') as a:
    for tw in tweet:
        a.write(json.dumps(tw, indent = 4, sort_keys = True))
        a.write('\n')


# get tweets containing "YOUR_QUERY" and save them to a file
# https://dev.twitter.com/streaming/reference/post/statuses/filter
tweets = twitter_stream.statuses.filter(track = "YOUR_QUERY")
with open('tweets-search.txt', 'w') as b:
    for tws in tweets:
        b.write(json.dumps(tws, indent = 4, sort_keys = True))
        b.write('\n')


# get tweets containing "YOUR_QUERY" and save them to a file (JSON response manipulation)
# https://dev.twitter.com/streaming/reference/post/statuses/filter
tweet = twitter_stream.statuses.filter(track = "YOUR_QUERY")
with open('tweets-search-JSON response manipulated.txt', 'w') as c:
    for tws in tweet:
        c.write(str('@' + tws['user']['screen_name'] + '\n'))
        c.write(str(tws['text'].encode("utf-8") + '\n\n'))
