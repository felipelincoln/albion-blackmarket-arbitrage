import requests
from tkinter import *

client_version = 0.3
client_title = 'albion-black-market-comparison Client v' + str(client_version)

city_list = ['Lymhurst', 
			 'Bridgewatch',
			 'Fortsterling',
			 'Caerleon',
			 'Martlock',
			 'Thetford']
file_list = ['accessories.txt',
			 'armor1.txt',
			 'armor2.txt',
			 'armor3.txt',
			 'armor4.txt',
			 'armor5.txt',
			 'armor6.txt',
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

img_route = 'https://gameinfo.albiononline.com/api/gameinfo/items/'
data_route = 'https://www.albion-online-data.com/api/v2/stats/prices/'
tax = 0.06

def cmd_search():
	city = var_city.get() 
	item_file = 'items/' + var_file.get()
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
		
	full_list = sorted(offer_dict.items(), key=lambda x:(x[0], -x[1][1]+x[1][0]))
	profit_list = []
	
	for item in full_list:
		name = item[0]
		values_pair = item[1]
		profit = round(values_pair[1]*(1-tax) - values_pair[0])
	
		if profit > 0:
			profit_list.append([name, values_pair, profit])


	for widget in frame.winfo_children()[10:]:
		widget.destroy()
	frame.pack_forget()

	i = 0
	for item in profit_list[::-1]:
		name = item[0]
		item_id = item[0].split('#')[0]
		price = item[1][0]
		blackmarket = item[1][1]
		profit = item[2]

		img = PhotoImage(file='img_lowquality/'+item_id+'.png')
		label = Label(frame, image=img)
		label.image = img
		label.grid(row=3+i, column=0, sticky=W)
		Label(frame, text=name).grid(row=3+i, column=1, sticky=W)
		Label(frame, text=price, padx=15).grid(row=3+i, column=2, sticky=W)
		Label(frame, text=blackmarket, padx=15).grid(row=3+i, column=3, sticky=W)
		Label(frame, text=profit, padx=15).grid(row=3+i, column=4, sticky=W)
		i += 1

	gui.update()
	canvas.config(scrollregion=canvas.bbox('all'))

## LAYOUT

gui = Tk()
gui.title(client_title)
gui.geometry('800x500')


scrollbar = Scrollbar(gui)
canvas = Canvas(gui, bg='pink', yscrollcommand=scrollbar.set)
scrollbar.config(command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
frame = Frame(canvas)
canvas.pack(side=LEFT, fill=BOTH, expand=True)
canvas.create_window(0, 0, window=frame, anchor=NW)

var_city = StringVar(frame)
var_file = StringVar(frame)
var_city.set(city_list[0])
var_file.set(file_list[0])

Label(frame, text='Version 0.3', bg='turquoise').grid(row=0, column=0)

Label(frame, text='City').grid(row=1, column=0, sticky=W)
OptionMenu(frame, var_city, *city_list).grid(row=1, column=1, sticky=W)
Label(frame, text='Items', padx=15).grid(row=1, column=2, sticky=W)
OptionMenu(frame, var_file, *file_list).grid(row=1, column=3, sticky=W)
Button(frame, text='Search', command=cmd_search).grid(row=1, column=4, sticky=W)

Label(frame, text='Item#quality').grid(row=2, column=0, columnspan=2, sticky=W)
Label(frame, text='Price', padx=15).grid(row=2, column=2, sticky=W)
Label(frame, text='Black Market', padx=15).grid(row=2, column=3, sticky=W)
Label(frame, text='Profit', padx=15).grid(row=2, column=4, sticky=W)

gui.update()
canvas.config(scrollregion=canvas.bbox('all'))
gui.mainloop()
