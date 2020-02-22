# albion-blackmarket-comparison
[![](https://img.shields.io/github/downloads/felipelincoln/albion-blackmarket-comparison/total)](https://github.com/felipelincoln/albion-blackmarket-comparison/releases)

Compares cities market prices to the black market in Albion Online.

![](https://raw.githubusercontent.com/felipelincoln/albion-blackmarket-comparison/master/screenshot.png)

## Legal issues
Since it is mainly the presentation of the data obtained from a legal API, [albion-online-data](https://www.albion-online-data.com/), this can't be ilegal.

## Installing

Download the [latest release](https://github.com/felipelincoln/albion-blackmarket-comparison/releases) and unzip it.

## Running

Once you are in the blackmarket-comparison folder, run:
``
python3 py/retriever.py items/<file> <city>
``

chosing the file you want from the following:

```
accessories.txt  armor4.txt  magic2.txt  melee2.txt  off-hand1.txt
armor1.txt       armor5.txt  magic3.txt  melee3.txt  off-hand2.txt
armor2.txt       armor6.txt  magic4.txt  melee4.txt  ranged1.txt
armor3.txt       magic1.txt  melee1.txt  melee5.txt  ranged2.txt
```

the result will be in the following format:

``
ITEM_ID#ITEM_QUALITY	[CITY_SELL_PRICE, BLACKMARKET_BUY_PRICE] PROFIT_VALUE_WITH_6%_TAX
``

If you are not sure what items is T8_HEAD_CLOTH_SET3@3#2, use the official API to take a look:
https://gameinfo.albiononline.com/api/gameinfo/items/T8_HEAD_CLOTH_SET3@3

**Importante note**: the use of this python code won't give you up to date prices.

## Real-time prices
In order to get market prices updated you have to first download the [albiondata-client](https://github.com/BroderickHyman/albiondata-client/releases) and keep it running. Then visit the market, the items in the current market tab will be automaticaly updated to the API.

Have fun and good tradings! :moneybag:  
And if you have any questions you can call me ingame, my nickname is Etiopia.
