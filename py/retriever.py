# python3 py/retriever.py items/<file> <city1, [city2, ...]>
import requests
import sys

api = 'https://www.albion-online-data.com/api/v2/stats/prices/'
tag = '?locations='

items = open(sys.argv[1], 'r').read().replace('\n', ',')[:-1]

response_caerleon = requests.get(api + items + tag + 'caerleon').json()
response_blackmarket = requests.get(api + items + tag + 'blackmarket').json()
val = {}

for each in response_caerleon:
	if each['sell_price_min']:
		val[each['item_id'] + '#' + str(each['quality'])] = [each['sell_price_min'], 0]

for each in response_blackmarket:
	k = each['item_id'] + '#' + str(each['quality'])
	if k in val.keys(): 
		val[k][1] = each['buy_price_max']

#print(sorted(val.items(), key=lambda x: -x[1][1]+x[1][0]))


for each in sorted(val.items(), key=lambda x: -x[1][1]+x[1][0]):
	if each[1][1] > each[1][0]:
		print(each[0], each[1])
