from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
try:
    import json
except ImportError:
    import simplejson as json
import csv
import time
from dateutil.parser import parse
import pandas

access_token = "298221198-0ncIxf4UXOaOj7GTKe24sffxCcRwfcwveIwJMGWH"
access_secret = "klSYxSRqPQzIhP721DBuvtH1nTY93K4vZ4B3cHHwYIQsF"
consumer_key = "JJ6I0QWQEtbY2qcVJPHkd6p7n"
consumer_secret = "jzq41XHKGwMArIZ3ATAhjj4sky4yJXVRACKNxaa4O4IKJzZ1UA"

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

twitter_rest = Twitter(auth = oauth)

ufpa_tweets = twitter_rest.statuses.user_timeline(screen_name = "Samsung", count = 150)

#dataFrame
df = pandas.read_csv('exercicio1.csv')
print ''.join([str(df.loc[df['retweet_count'].idxmax()]['id']),
 " eh o id com mais retweet, com: ",
 str(df['retweet_count'].max()),
  " tweets."])

with open('exercicio1.csv', 'w') as s_t:
	row = []
	mais_rt = []
	id_mais_rt = []
	writer = csv.writer(s_t, delimiter= ',')
	writer.writerow(['id', 'texto', 'retweet_count'])
	for tweet in ufpa_tweets:
		mais_rt.append(int(unicode(tweet['retweet_count']).encode("utf-8")))
		id_mais_rt.append(unicode(tweet['id']).encode("utf-8"))
		row.append(unicode(tweet['id']).encode("utf-8"))
		row.append(tweet['text'].replace('\n', ' ').replace('\r', '').encode("utf-8"))
		row.append(unicode(tweet['retweet_count']).encode("utf-8"))
		writer.writerow(row)
		row = []

	maior_rt = max(mais_rt)

	for c in xrange(len(mais_rt)):
		if maior_rt == mais_rt[c]:
			lugar_maior_rt = c

	print id_mais_rt[lugar_maior_rt] + " eh o id com mais retweet, com: " + str(maior_rt) + " tweets."
