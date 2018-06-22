import facebook
import csv
try:
    import json
except ImportError:
    import simplejson as json

import sys

acess_token = "EAANmn2Sjbw8BAA0CZBlYfp6VzQ3hgd8KIbVTVYbP6UTBuDwW97JvqNoZBaUSw19gK6y8IB8GUMm1OBucSdonv8nZC1JAkCBvM09zfxW8eM7tHUMAWZCnU7SudNsNdFLlZAsL7v9ImQ39ZADGtUBu6RbTJo59oeHrwZD"

graph = facebook.GraphAPI(access_token = acess_token, version='2.7')

infos = graph.get_object("PortaliMasters", fields = 'posts')


with open('ex3.csv', 'w') as i:
	row = []
	writer = csv.writer(i, delimiter= ',')
	writer.writerow(['created_time', 'likes', 'shares'])
	for post in infos['posts']:

		print post.keys()

		sys.exit()

		#row.append(str(unicode(post['created_time']).encode("utf-8")))
		row.append(str(unicode(post['likes']['summary']['total_count']).encode("utf-8")))
		row.append(str(unicode(post['shares']['count']).encode("utf-8")))
		row.append(tweet['message'].replace('\n', ' ').replace('\r', '').encode("utf-8"))
		writer.writerow(row)
		row = []