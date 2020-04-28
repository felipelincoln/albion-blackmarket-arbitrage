import requests
from PIL import Image

from datainfo import file_list

for item in file_list:
    item_file = '../items/'+item
    items = open(item_file, 'r').read().split()

    for name in items:
        print('downloading', name)
        url = 'https://gameinfo.albiononline.com/api/gameinfo/items/'
        response = requests.get(url+name, stream=True)
        if response.status_code == 200:
            img = Image.open(response.raw)
            img = img.resize((50, 50))
            img.save('img_lowquality/'+name+'.png')
