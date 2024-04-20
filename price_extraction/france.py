from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def get_france_price(product_name):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    
    product_name = product_name.replace(' ', '+')
    url = f'https://amazon.fr/s?k={product_name}'

    driver.get(url)

    deliver_to_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link"))
    )
    deliver_to_link.click()

    postcode_input1 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "GLUXZipUpdateInput"))
    )

    postcode_input1.clear()
    postcode_input1.send_keys("75001")

    apply_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "GLUXZipUpdate"))
    )
    apply_button.click()

    print("Postcode applied successfully.")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-price-whole")))

    html_after_apply = driver.page_source

    soup = BeautifulSoup(html_after_apply, 'html.parser')

    updated_url = driver.current_url
    url = updated_url

    driver.get(url)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find('div', class_='a-row a-size-base a-color-base')
    price = price.find('span', class_='a-offscreen')

    return [price]
