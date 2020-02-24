import requests

data_route = 'https://www.albion-online-data.com/api/v2/stats/prices/'
city = 'lymhurst'
tax = 0.06

item_file = '../items/armor1.txt'
item_query = open(item_file, 'r').read().replace('\n', ',')[:-1]

response_city = requests.get(data_route + item_query + '?locations=' + city).json()
response_blackmarket = requests.get(data_route + item_query + '?locations=blackmarket').json()

offer_dict = {}
for entry in response_city:
	item = entry['item_id']
	value = entry['sell_price_min']
	quality = entry['quality']
	name = item + "#" + str(quality)

	if value:
		offer_dict[name] = [value, 0]

for entry in response_blackmarket:
	item = entry['item_id']
	value = entry['buy_price_max']
	qualities = [x for x in range(entry['quality'], 6)]
	items_to_purchase = [item+"#"+str(x) for x in qualities]
	city_values = []

	for item_key in items_to_purchase:
		if item_key in offer_dict.keys():
			item_city_value = offer_dict[item_key][0]
			city_values.append(item_city_value)

	if len(city_values) > 0:
		offer_dict[items_to_purchase[0]] = [min(city_values), value]
	

for item in sorted(offer_dict.items(), key=lambda x:(x[0], -x[1][1]+x[1][0])):
	name = item[0]
	values_pair = item[1]
	profit = round(values_pair[1]*(1-tax) - values_pair[0])

	if profit > 0:
		print(name, values_pair, profit)
