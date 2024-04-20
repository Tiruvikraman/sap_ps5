
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')  # Run Chrome in headless mode, i.e., without a GUI
driver = webdriver.Chrome(options=options)
driver.get('https://www.bhinneka.com/jual?cari=iphone+14+pro&order=')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
price = soup.find('span',class_='oe_currency_value')
print('price',price.get_text())
