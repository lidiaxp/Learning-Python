#encoding: utf-8
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

# conect to REST API
twitter_rest = Twitter(auth = oauth)
##### END AUTHENTICATION #####

# get most recent your twett
gean_twett = twitter_rest.statuses.user_timeline(screen_name = "YOUR_SCREEN_NAME", count = 1)
# save them to a file
with open('your-most-recent-twett.txt', 'w') as g:
    for tweet in gean_twett:
        g.write(json.dumps(tweet, indent = 4, sort_keys = True))
        g.write('\n')

# get most recent Gean's twett (JSON response manipulation)
gean_twett = twitter_rest.statuses.user_timeline(screen_name = "YOUR_SCREEN_NAME", count = 1)
# save them to a file
with open('your-most-recent-twett-JSON-response-manipulated.txt', 'w') as h:
    for tweet in gean_twett:
        h.write(json.dumps(tweet['text'], indent = 4, sort_keys = True, ensure_ascii = False).encode("utf-8"))
        h.write('\n')

# get five most recents Gean's favorites
gean_favorites_list = twitter_rest.favorites.list(screen_name = "YOUR_SCREEN_NAME", count = 5)
# save them to a file
with open('your-favorites-list.txt', 'w') as i:
    for fv in gean_favorites_list:
        i.write(json.dumps(fv, indent = 4, sort_keys = True))
        i.write('\n')

# get five most recent Gean's mentions
gean_metions = twitter_rest.statuses.mentions_timeline(screen_name = "YOUR_SCREEN_NAME", count = 5)
# save them to a file
with open('your_metions-list.txt', 'w') as j:
    for mt in gean_metions:
        j.write(json.dumps(mt, indent = 4, sort_keys = True))
        j.write('\n')

# get five Gean's followers
gean_followers = twitter_rest.followers.list(screen_name = "YOUR_SCREEN_NAME", count = 5)
#print json.dumps(gean_followers, indent = 4)
# save them to a file
with open('your-followers.txt', 'w') as k:
    for fl in gean_followers['users']:
        k.write(json.dumps(fl, indent = 4, sort_keys = True))
        k.write('\n')
