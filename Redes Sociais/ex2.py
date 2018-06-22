from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
try:
    import json
except ImportError:
    import simplejson as json
import csv
import time
from dateutil.parser import parse
import pandas

'''
access_token = "298221198-0ncIxf4UXOaOj7GTKe24sffxCcRwfcwveIwJMGWH"
access_secret = "klSYxSRqPQzIhP721DBuvtH1nTY93K4vZ4B3cHHwYIQsF"
consumer_key = "JJ6I0QWQEtbY2qcVJPHkd6p7n"
consumer_secret = "jzq41XHKGwMArIZ3ATAhjj4sky4yJXVRACKNxaa4O4IKJzZ1UA"

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

twitter_rest = Twitter(auth = oauth)

ufpa_tweets = twitter_rest.statuses.user_timeline(screen_name = "Samsung", count = 150)
'''

'''
with open('exercicio2.csv', 'w') as s_t:
	row = []
	writer = csv.writer(s_t, delimiter= ',')
	writer.writerow(['id', 'texto', 'retweet_count'])
	for tweet in ufpa_tweets:
		row.append(unicode(tweet['id']).encode("utf-8"))
		row.append(tweet['text'].replace('\n', ' ').replace('\r', '').encode("utf-8"))
		row.append(unicode(tweet['retweet_count']).encode("utf-8"))
		writer.writerow(row)
		row = []
'''

def retweeters(id_status, twitter_rest):
	retweets = twitter_rest.statuses.retweets._id(_id = id_status)
	mais_follow = []
	ids = []
	names = []
	screen_names = []
	for retweet in retweets:
		mais_follow.append(int(retweet['user']['followers_count']))
		ids.append(retweet['id'])
		names.append(retweet['user']['name'])
		screen_names.append(retweet['user']['screen_name'])

	max_follow = max(mais_follow)

	for c in xrange(len(mais_follow)):
		if max_follow == mais_follow[c]:
			lugar_maior_follow = c

	print ''.join(["id: ", str(ids[lugar_maior_follow]), 
		" - name: ", names[lugar_maior_follow], 
		" - screen_name: ", str(screen_names[lugar_maior_follow])])

def main():
	access_token = "298221198-0ncIxf4UXOaOj7GTKe24sffxCcRwfcwveIwJMGWH"
	access_secret = "klSYxSRqPQzIhP721DBuvtH1nTY93K4vZ4B3cHHwYIQsF"
	consumer_key = "JJ6I0QWQEtbY2qcVJPHkd6p7n"
	consumer_secret = "jzq41XHKGwMArIZ3ATAhjj4sky4yJXVRACKNxaa4O4IKJzZ1UA"
	oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)
	twitter_rest = Twitter(auth = oauth)
	id_status = max_retweetes()
	retweeters("849850390770106368", twitter_rest)

def max_retweetes():
	df = pandas.read_csv('exercicio2.csv')
	return str(df.loc[df['retweet_count'].idxmax()]['id'])

if __name__ == '__main__':
	main()

'''
def create_csv():
	with open('exercicio2.csv', 'w') as s_t:
		row = []
		writer = csv.writer(s_t, delimiter= ',')
		writer.writerow(['id', 'texto', 'retweet_count'])
		for tweet in ufpa_tweets:
			row.append(unicode(tweet['id']).encode("utf-8"))
			row.append(tweet['text'].replace('\n', ' ').replace('\r', '').encode("utf-8"))
			row.append(unicode(tweet['retweet_count']).encode("utf-8"))
			writer.writerow(row)
			row = []

def quem_rt(mais_id):
	retweets = twitter_rest.statuses.retweets_id(_id = mais_id)
	for retweet in retweets:
		print str(retweet['followers_count'])

def id_m_rt():
	df = pandas.read_csv('exercicio2.csv')
	id_mais = str(df.loc[df['retweet_count'].idxmax()]['id'])
	return int(id_mais)

def main():
	access_token = "298221198-0ncIxf4UXOaOj7GTKe24sffxCcRwfcwveIwJMGWH"
	access_secret = "klSYxSRqPQzIhP721DBuvtH1nTY93K4vZ4B3cHHwYIQsF"
	consumer_key = "JJ6I0QWQEtbY2qcVJPHkd6p7n"
	consumer_secret = "jzq41XHKGwMArIZ3ATAhjj4sky4yJXVRACKNxaa4O4IKJzZ1UA"
	oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)
	create_csv()
	twitter_rest = Twitter(auth = oauth)
	quem_rt(id_m_rt())

if __name__ == '__main__':
	main()
'''