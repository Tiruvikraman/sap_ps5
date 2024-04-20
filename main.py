from france import get_france_price
from germany import get_germany_price
from japan import get_japan_price
from singapore import get_singapore_price
from uk import get_uk_price
from aust import get_aust_price
from usa import get_usa_price

product_name = "iphone 15 pro"

price_info = get_france_price(product_name)
print(price_info)

price_info = get_germany_price(product_name)
print(price_info)

price_info = get_japan_price(product_name)
print(price_info)

price_info = get_singapore_price(product_name)
print(price_info)

price_info = get_uk_price(product_name)
print(price_info)

price_info = get_aust_price(product_name)
print(price_info)

price_info = get_usa_price(product_name)
print(price_info)
