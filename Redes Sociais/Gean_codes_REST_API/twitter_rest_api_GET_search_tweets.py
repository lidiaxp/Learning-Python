# -*- coding: UTF-8 -*-
##### BEGIN IMPORT #####

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
try:
    import json
except ImportError:
    import simplejson as json
import csv

##### END IMPORT #####

##### BEGIN AUTHENTICATION #####

access_token = "INSERT_YOUR_ACCESS_TOKEN_HERE"
access_secret = "INSERT_YOUR_ACCESS_SECRET_HERE"
consumer_key = "INSERT_YOUR_CONSUMER_KEY_HERE"
consumer_secret = "INSERT_YOUR_CONSUMER_SECRET_HERE"

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

# conect to REST API
twitter_rest = Twitter(auth = oauth)

##### END AUTHENTICATION #####

# get a number of tweets searched by a query
searched_tweets = twitter_rest.search.tweets(q = 'YOUR_QUERY', count = 100)
# save them to a .txt file
with open('searched-tweets.txt', 'w') as s_t:
	s_t.write(json.dumps(searched_tweets, indent = 4, sort_keys = True))
	s_t.write('\n')

# get a number of tweets searched by a query (JSON response manipulation)
searched_tweets = twitter_rest.search.tweets(q = 'YOUR_QUERY', count = 100)
# save them to a .txt file
with open('searched-tweets-JSON-response-manipulated.txt', 'w') as s_t:
	for tweet in searched_tweets['statuses']:
		s_t.write(tweet['user']['screen_name'] + '\n')
		s_t.write(json.dumps(tweet['text'].replace('\n', ' ').replace('\r', ''), indent = 4, sort_keys = True, ensure_ascii = False).encode("utf-8"))
		s_t.write('\n\n')

# making a simple database in a .csv file
# fields: NAME, SCREEN_NAME, TEXT
searched_tweets = twitter_rest.search.tweets(q = 'YOUR_QUERY', count = 100)
# save them to a .csv file
with open('searched-tweets-database.csv', 'w') as s_t:
	row = []
	writer = csv.writer(s_t, delimiter= ',')
	for tweet in searched_tweets['statuses']:
		row.append(unicode(tweet['user']['name']).encode("utf-8"))
		row.append(unicode(tweet['user']['screen_name']).encode("utf-8"))
		row.append(tweet['text'].replace('\n', ' ').replace('\r', '').encode("utf-8"))
		writer.writerow(row)
		row = []
