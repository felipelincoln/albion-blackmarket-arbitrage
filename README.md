# albion-blackmarket-comparison
[![](https://img.shields.io/github/downloads/felipelincoln/albion-blackmarket-comparison/total)](https://github.com/felipelincoln/albion-blackmarket-comparison/releases)

Compares prices from city's market to the Black Market.  

**Important note**: the API's refresh rate isn't real time, so there may be some offer showed here that is currently finished. Always check before doing anything!

Download the [latest release](https://github.com/felipelincoln/albion-blackmarket-comparison/releases), unzip and run:

``
python3 py/retriever.py items/<file> <city>
``

chosing the file you want from the following:

```
accessories.txt      gathering_gear2.txt  melee3.txt
armor1.txt           gathering_gear3.txt  melee4.txt
armor2.txt           magic1.txt           melee5.txt
armor3.txt           magic2.txt           off-hand1.txt
armor4.txt           magic3.txt           off-hand2.txt
armor5.txt           magic4.txt           ranged1.txt
armor6.txt           melee1.txt           ranged2.txt
gathering_gear1.txt  melee2.txt
```

the result will be in the following format:

``
ITEM_NAME	[CITY_SELL_PRICE, BLACKMARKET_BUY_PRICE] PROFIT_VALUE_WITH_6%_TAX
``

We are using the API from www.albion-online-data.com.
