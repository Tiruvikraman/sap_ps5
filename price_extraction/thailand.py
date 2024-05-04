from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_thailand_price(product_name):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--disable-images")
    chrome_options = webdriver.ChromeOptions()
    # this will disable image loading
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    # or alternatively we can set direct preference:
    chrome_options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2}
    )
    options.add_argument('window-size=1200x600')
    options.add_argument('--disable-web-security')  # Disable web security
    options.add_argument('--disable-cookie-encryption')

    driver = webdriver.Chrome(options=options)
    product_name = product_name.replace(' ', '%20')
    driver.get(f'https://www.powerbuy.co.th/en/search/{product_name}')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find('div',class_='text-redPrice font-bold text-sm leading-3 w-full flex').get_text()

    return[price]
