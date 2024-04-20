from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
def get_indonesia_price(product_name):
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # Run Chrome in headless mode, i.e., without a GUI
    driver = webdriver.Chrome(options=options)

    url=f'https://www.bhinneka.com/jual?cari={product_name}'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find('span', class_='oe_currency_value').get_text()
    return[price]
