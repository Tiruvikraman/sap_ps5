from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
def get_indonesia_price(product_name):
    
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
    url=f'https://www.bhinneka.com/jual?cari={product_name}'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find('span', class_='h6 mb-0').get_text().replace("\xa0",'')
    return price[:price.index('.000')].replace('.','')
