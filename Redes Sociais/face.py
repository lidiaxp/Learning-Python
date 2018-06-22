# -*- coding: utf-8 -*-
##### BEGIN IMPORT #####
import facebook
try:
    import json
except ImportError:
    import simplejson as json
##### END IMPORT #####

##### BEGIN AUTHENTICATION #####
#acess_token = "INSERT_YOUR_ACCESS_TOKEN_HERE"
acess_token = "EAANmn2Sjbw8BAA0CZBlYfp6VzQ3hgd8KIbVTVYbP6UTBuDwW97JvqNoZBaUSw19gK6y8IB8GUMm1OBucSdonv8nZC1JAkCBvM09zfxW8eM7tHUMAWZCnU7SudNsNdFLlZAsL7v9ImQ39ZADGtUBu6RbTJo59oeHrwZD"
# conect to Graph API
graph = facebook.GraphAPI(access_token = acess_token, version='2.7')
##### END AUTHENTICATION #####

# Para obter suas informações básicas
info_default = graph.get_object("me")
# ou infos = graph.get_object(id = 'INSERT_YOUR_FACEBOOK_ID_HERE') http://findmyfbid.com/
with open('gean-info-default.txt', 'w') as g:
	g.write(json.dumps(info_default, ensure_ascii = False, indent = 4, sort_keys = True).encode("utf-8"))
	g.write('\n')
'''
# Para obter outras informações, adiciona-se o campo fields.
# Ver lista completa de fields em Graph API Explores
infos = graph.get_object("182614806880", fields = 'id,name,posts')
with open('gean-infos.txt', 'w') as h:

	h.write(json.dumps(infos, ensure_ascii = False, indent = 4, sort_keys = True).encode("utf-8"))
	h.write('\n')
'''
# Para obter outras informações, adiciona-se o campo fields.
# Ver lista completa de fields em Graph API Explores
infos = graph.get_object("182614806880_10154326847821881", fields = 'id,likes.summary(TRUE)')
with open('tes.txt', 'w') as i:
	a = json.dumps(infos, ensure_ascii = False, indent = 4, sort_keys = True).encode("utf-8")
	b = json.loads(a)
	print b["likes"]["summary"]["total_count"]
	i.write(json.dumps(infos, ensure_ascii = False, indent = 4, sort_keys = True).encode("utf-8"))
	i.write('\n')

# id,name,posts{message,story,comments{from,message}}
