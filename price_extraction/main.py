from france import get_france_price
from germany import get_germany_price
from japan import get_japan_price
from singapore import get_singapore_price
from uk import get_uk_price
from aust import get_aust_price
from usa import get_usa_price
from canada import get_canada_price
from indonesia import get_indonesia_price
from thailand import get_thailand_price

product_name = input("Enter product name: ")

france_price = get_france_price(product_name)
usa_price = get_usa_price(product_name)

germany_price = get_germany_price(product_name)

japan_price = get_japan_price(product_name)

singapore_price = get_singapore_price(product_name)

uk_price = get_uk_price(product_name)

aust_price = get_aust_price(product_name)


canada_price = get_canada_price(product_name)

indonesia_price = get_indonesia_price(product_name)

thai_price = get_thailand_price(product_name)
print(uk_price,usa_price,germany_price,thai_price,canada_price,aust_price,indonesia_price,japan_price,france_price,singapore_price)