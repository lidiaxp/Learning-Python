# -*- coding: UTF-8 -*-
##### BEGIN IMPORT #####

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
try:
    import json
except ImportError:
    import simplejson as json
import csv
import time
from dateutil.parser import parse

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

# get a number of tweets of @UFPA_Oficial
ufpa_tweets = twitter_rest.statuses.user_timeline(screen_name = "UFPA_Oficial", count = 150)
# save them to a .txt file
with open('ufpa-tweets.txt', 'w') as ufpa_t:
	ufpa_t.write(json.dumps(ufpa_tweets, indent = 4, sort_keys = True))
	ufpa_t.write('\n')

# get a number of tweets of @UFPA_Oficial (JSON response manipulation)
ufpa_tweets = twitter_rest.statuses.user_timeline(screen_name = "UFPA_Oficial", count = 150)
# save them to a .txt file
with open('ufpa-tweets-JSON-response-manipulated.txt', 'w') as s_t:
	for tweet in ufpa_tweets:
		s_t.write(json.dumps(tweet['text'].replace('\n', ' ').replace('\r', ''), indent = 4, sort_keys = True, ensure_ascii = False).encode("utf-8"))
		s_t.write('\n')

# making a simple database in a .csv file
# fields: CREATED_AT, FAVORIRE_COUNT, RETWEET_COUNT, TEXT
ufpa_tweets = twitter_rest.statuses.user_timeline(screen_name = "UFPA_Oficial", count = 150)
# save them to a .csv file
with open('ufpa-tweets-database.csv', 'w') as s_t:
	row = []
	writer = csv.writer(s_t, delimiter= ',')
	for tweet in ufpa_tweets:
		row.append(unicode(tweet['created_at']).encode("utf-8"))
		row.append(unicode(tweet['favorite_count']).encode("utf-8"))
		row.append(unicode(tweet['retweet_count']).encode("utf-8"))
		row.append(tweet['text'].replace('\n', ' ').replace('\r', '').encode("utf-8"))
		writer.writerow(row)
		row = []

##### statistical analysis #####
with open('ufpa-tweets-database.csv', 'r') as s_t:
    day_list = []
    fav_list = []
    retweet_list = []
    reader = csv.reader(s_t, delimiter = ',')
    for [created_at,favorite_count,retweet_count,text] in reader:
        createdAt = parse(created_at, ignoretz = True)
        # print createdAt
        date = '%s' % (createdAt)
        day_format = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        day = time.strftime("%d", day_format)
        day_list.append(day)

        fav = int(favorite_count)
        fav_list.append(fav)
        # print fav

        retweet = int(retweet_count)
        retweet_list.append(retweet)
        # print retweet

    day_list.reverse()
    fav_list.reverse()
    retweet_list.reverse()
    # print day_list
    # print fav_list
    # print retweet_list

    new_day_list = []
    number_of_tweets = []
    new_fav_list = []
    new_retweet_list = []
    sum_fav = 0
    sum_retweet = 0
    day_now = day_list[0]

    for dia in day_list:
        if dia not in new_day_list:
            new_day_list.append(dia)
            number_of_tweets.append(day_list.count(dia))

    for i,dia in enumerate(day_list):
        fav = fav_list[i]
        retweet = retweet_list[i]
        if (day_list.count(dia) == 1):
            sum_fav = fav
            sum_retweet = retweet
            new_fav_list.append(sum_fav)
            new_retweet_list.append(sum_retweet)
            day_now = day_list[i+1]
        elif (dia == day_now):
            sum_fav = sum_fav + fav
            sum_retweet = sum_retweet + retweet
            if i == (len(day_list) - 1):
                new_fav_list.append(sum_fav)
                new_retweet_list.append(sum_retweet)
        else:
            new_fav_list.append(sum_fav)
            new_retweet_list.append(sum_retweet)
            day_now = dia
            sum_fav = fav
            sum_retweet = retweet

    print new_day_list
    print len(new_day_list)
    print number_of_tweets
    print len(number_of_tweets)
    print new_fav_list
    print len(new_fav_list)
    print new_retweet_list
    print len(new_retweet_list)

    # STEM CHART
    '''
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.array(new_day_list).astype(np.int)
    y = number_of_tweets
    markerline, stemlines, baseline = plt.stem(x, y, '-.')
    plt.setp(baseline, 'color', 'r', 'linewidth', 2)
    plt.xticks(x)
    plt.grid(True)
    plt.show()
    '''

    # STEP CHART
    '''
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.array(new_day_list).astype(np.int)
    y = number_of_tweets
    plt.step(x, y, label='pre (default)')
    plt.xticks(x)
    plt.legend()
    plt.grid(True)
    plt.show()
    '''

    import matplotlib.pyplot as plt
    import numpy as np
    x = np.array(new_day_list).astype(np.int)
    y1 = number_of_tweets
    y2 = new_fav_list
    plt.figure(1)
    plt.subplot(211)
    plt.plot(x, y1)
    plt.xticks(x)
    plt.grid(True)
    plt.ylabel('Number of tweets')
    plt.xlabel('Dias')
    plt.subplot(212)
    plt.plot(x, y2, color = 'r')
    plt.xticks(x)
    plt.grid(True)
    plt.ylabel('Number of favorites')
    plt.xlabel('Dias')
    plt.show()
