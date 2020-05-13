import requests
from tkinter import *
from PIL import ImageTk, Image
from datainfo import (
    city_list, file_list, client_version, client_title, quality_list
)
from id_to_name import id_to_name
import time
from datetime import datetime

def timeDiff(date):
    format = '%Y-%m-%dT%H:%M:%S%z'
    timestampFromDate = int(datetime.strptime(date + "+0000", format).timestamp())
    currentTimestamp = time.time()
    timeDiff = currentTimestamp - timestampFromDate
    return '%.2f' % (timeDiff / 60 / 60)


data_route = 'https://www.albion-online-data.com/api/v2/stats/prices/'
tax = 0.06


def human_readable_value(value):
    if 1e3 <= value < 1e6:
        return str(round(value/1e3)) + ' k'
    elif 1e6 <= value:
        return str(round(value/1e6, 1)) + ' m'
    else:
        return str(value)

def cmd_search():
    city = var_city.get() 
    item_file = 'items/' + var_file.get()
    item_query = open(item_file, 'r').read().replace('\n', ',')[:-1]
    if not item_query:
        return
    
    response_city = requests.get(data_route + item_query + '?locations=' + city).json()
    response_blackmarket = requests.get(data_route + item_query + '?locations=blackmarket').json()
    
    offer_dict = {}
    for entry in response_city:
        item = entry['item_id']
        value = entry['sell_price_min']
        quality = entry['quality']
        name = item + "#" + str(quality)
        cityDiff = timeDiff(entry['sell_price_min_date'])
    
        if value:
            offer_dict[name] = [value, 0, cityDiff, 0]

    for entry in response_blackmarket:
        item = entry['item_id']
        value = entry['buy_price_max']
        qualities = [x for x in range(entry['quality'], 6)]
        items_to_purchase = [item+"#"+str(x) for x in qualities]
        city_values = []
        bmDiff = timeDiff(entry['buy_price_max_date'])
    
        for item_key in items_to_purchase:
            if item_key in offer_dict.keys():
                item_city_value = offer_dict[item_key][0]
                city_values.append(item_city_value)
    
        if len(city_values) > 0:
            cityDiff = -1
            if items_to_purchase[0] in offer_dict.keys():
                item = offer_dict[items_to_purchase[0]]
                cityDiff = item[2]
            offer_dict[items_to_purchase[0]] = [min(city_values), value, cityDiff, bmDiff]
        
    full_list = sorted(offer_dict.items(), key=lambda x:(x[0], -x[1][1]+x[1][0]))
    profit_list = []
    
    for item in full_list:
        name = item[0]
        values_pair = item[1]
        profit = round(values_pair[1]*(1-tax) - values_pair[0])
        cityDiff = values_pair[2]
        bmDiff = values_pair[3]
    
        if profit > 5000:
            profit_list.append([name, values_pair, profit, cityDiff, bmDiff])


    for widget in frame.winfo_children()[10:]:
        widget.destroy()
    frame.pack_forget()

    i = 0
    profit_list = sorted(profit_list, key=lambda x:x[2])
    for item in profit_list[::-1]:
        _id, _quality = item[0].split('#')

        enchant = item[0][-1] if "@" in item[0] else '0'
        tier = _id[1]
        quality = quality_list[int(_quality) -1]
        if _id in id_to_name.keys():
            translated_name = id_to_name[_id]
        else:
            tier = ''
            enchant = ''
            translated_name = _id
            

        name = f'{tier}.{enchant} {translated_name}, {quality}'

        item_id = item[0].split('#')[0]
        price = human_readable_value(item[1][0])
        blackmarket = human_readable_value(item[1][1])
        profit = human_readable_value(item[2])
        cityDiff = item[3]
        bmDiff = item[4]

        img = ImageTk.PhotoImage(Image.open('img/'+item_id+'.png'))
        label = Label(frame, image=img)
        label.image = img
        label.grid(row=3+i, column=0, sticky=W)
        Label(frame, text=name).grid(row=3+i, column=1, sticky=W)
        Label(frame, text=price, padx=15).grid(row=3+i, column=2, sticky=W)
        Label(frame, text=blackmarket, padx=15).grid(row=3+i, column=3, sticky=W)
        Label(frame, text=profit, padx=15).grid(row=3+i, column=4, sticky=W)
        Label(frame, text=str(cityDiff) + 'h', padx=15).grid(row=3+i, column=5, sticky=W)
        Label(frame, text=str(bmDiff) + 'h', padx=15).grid(row=3+i, column=6, sticky=W)
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

Label(frame, text='Version '+str(client_version), bg='turquoise').grid(row=0, column=0)

Label(frame, text='City').grid(row=1, column=0, sticky=W)
OptionMenu(frame, var_city, *city_list).grid(row=1, column=1, sticky=W)
Label(frame, text='Items', padx=15).grid(row=1, column=2, sticky=W)
OptionMenu(frame, var_file, *file_list).grid(row=1, column=3, sticky=W)
Button(frame, text='Search', command=cmd_search).grid(row=1, column=4, sticky=W)

Label(frame, text='Item').grid(row=2, column=0, columnspan=2, sticky=W)
Label(frame, text='Price', padx=15).grid(row=2, column=2, sticky=W)
Label(frame, text='Black Market', padx=15).grid(row=2, column=3, sticky=W)
Label(frame, text='Profit', padx=15).grid(row=2, column=4, sticky=W)
Label(frame, text='City Diff', padx=15).grid(row=2, column=5, sticky=W)
Label(frame, text='BM Diff', padx=15).grid(row=2, column=6, sticky=W)

gui.update()
canvas.config(scrollregion=canvas.bbox('all'))
gui.mainloop()
