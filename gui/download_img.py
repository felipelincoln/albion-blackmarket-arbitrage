import requests
from PIL import Image

file_list = [
			#'accessories.txt',
			# 'armor1.txt',
			# 'armor2.txt',
			# 'armor3.txt',
			# 'armor4.txt',
			# 'armor5.txt',
			# 'armor6.txt',
			 'magic1.txt',
			 'magic2.txt',
			 'magic3.txt',
			 'magic4.txt',
			 'melee1.txt',
			 'melee2.txt',
			 'melee3.txt',
			 'melee4.txt',
			 'melee5.txt',
			 'off-hand1.txt',
			 'off-hand2.txt',
			 'ranged1.txt',
			 'ranged2.txt']

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
