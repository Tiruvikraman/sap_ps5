from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_thailand_price(product_name):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.powerbuy.co.th/en/search/iphone%2015')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find('div',class_='text-redPrice font-bold text-sm leading-3 w-full flex').get_text()

    return[price]