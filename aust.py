from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_aust_price(product_name):
    driver = webdriver.Chrome()
    product_name = product_name.replace(' ', '+')
    url = f'https://www.amazon.com.au/s?k={product_name}'
    driver.get(url)

    deliver_to_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link"))
    )

    deliver_to_link.click()

    postcode_input1 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "GLUXPostalCodeWithCity_PostalCodeInput"))
    )

    postcode_input1.clear()
    postcode_input1.send_keys("2001")

    select_city_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@id='GLUXPostalCodeWithCity_CityValue']"))
    )
    select_city_button.click()

    sydney_option = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//select[@id='GLUXPostalCodeWithCity_DropdownList']//option[@value='SYDNEY']"))
    )

    sydney_option.click()
    select_city_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'GLUXPostalCodeWithCity_DropdownList_0'))
    )
    select_city_button.click()

    apply_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "GLUXPostalCodeWithCity_ApplyButtonLabel"))
    )
    driver.execute_script("arguments[0].click();", apply_button)

    print("Postcode applied successfully.")

    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-price-whole")))
    html_after_apply = driver.page_source

    soup = BeautifulSoup(html_after_apply, 'html.parser')

    updated_url = driver.current_url
    print(updated_url)
    url = updated_url

    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    symbol = soup.find('span', class_='a-price-symbol').get_text()
    price_text = soup.find('span', class_='a-price-whole').get_text().strip(',').replace('\u202f', '')

    price_text = price_text.replace(',', '').replace('.', '')

    price = int(price_text)

    return [symbol, price]