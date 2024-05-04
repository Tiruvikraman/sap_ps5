from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def get_canada_price(product_name):
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
    url = f'https://www.amazon.ca/s?k={product_name}'

    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    div_h = soup.find("div", id="h")
    captcha = soup.find('form', action='/errors/validateCaptcha')

    while div_h or captcha:
        driver.refresh()
        updated_url = driver.current_url
        url = updated_url

        driver.get(url)
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')
        captcha = soup.find('form', action='/errors/validateCaptcha')

        div_h = soup.find("div", id="h")
        if (div_h == None) and (captcha == None):
            break

    deliver_to_link = WebDriverWait(driver,0).until(
        EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link"))
    )
    deliver_to_link.click()

    postcode_input1 = WebDriverWait(driver,2).until(
        EC.presence_of_element_located((By.ID, "GLUXZipUpdateInput_0"))
    )
    postcode_input2 = WebDriverWait(driver,2).until(
        EC.presence_of_element_located((By.ID, "GLUXZipUpdateInput_1"))
    )

    postcode_input1.clear()
    postcode_input1.send_keys("T0A")
    postcode_input2.clear()
    postcode_input2.send_keys("0A0")

    apply_button = WebDriverWait(driver,0).until(
        EC.element_to_be_clickable((By.ID, "GLUXZipUpdate"))
    )
    apply_button.click()

    print("Postcode applied successfully.")

    WebDriverWait(driver,0).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-price-whole")))

    html_after_apply = driver.page_source

 
    soup = BeautifulSoup(html_after_apply, 'html.parser')

    updated_url = driver.current_url
    url = updated_url

    driver.get(url)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find('div', class_='a-row a-size-base a-color-base')
    price = price.find('span', class_='a-offscreen').get_text()

    return [price]
