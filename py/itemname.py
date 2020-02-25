#python3 py/itemname.py urls/<file>
import requests
import sys

api = 'https://api.hackertarget.com/pagelinks/?q='
urls = open(sys.argv[1], 'r').read().split()
items = []

print(urls)


for url in urls:
    response = requests.get(api+url)
    it = [x[42:] for x in response.text.split() if 'https://www.albiononline2d.com/en/item/id/' in x]
    items += it

for item in items:
    print(item)
