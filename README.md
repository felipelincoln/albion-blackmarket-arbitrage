#albion-blackmarket-comparison
Compares prices from Caerleon market to the Black Market

Download this repository, `cd` into it and type:

``
python3 py/retriever.py items/<file>
``

chosing the file you want from the following:

``
accessories.txt      gathering_gear2.txt  melee3.txt
armor1.txt           gathering_gear3.txt  melee4.txt
armor2.txt           magic1.txt           melee5.txt
armor3.txt           magic2.txt           off-hand1.txt
armor4.txt           magic3.txt           off-hand2.txt
armor5.txt           magic4.txt           ranged1.txt
armor6.txt           melee1.txt           ranged2.txt
gathering_gear1.txt  melee2.txt
``

the result will be in the following format:

``
ITEM_NAME	[CAERLEON_SELL_PRICE, BLACKMARKET_BUY_PRICE]
``

We are using the API from www.albion-online-data.com.
