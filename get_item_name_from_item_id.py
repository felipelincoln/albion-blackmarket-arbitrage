import requests
from PIL import Image

from datainfo import file_list

print('id_to_name = {')
for filename in file_list:
    item_file = 'items/'+filename
    items = open(item_file, 'r').read().split()

    for name in items:
        url = f'https://gameinfo.albiononline.com/api/gameinfo/items/{name}/data'
        with requests.get(url) as response:
            if response.status_code == 200:
                value = response.json()['localizedNames']['EN-US']
                print(f'    "{name}": "{value}",')

print('}')
