from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

url = 'https://www.amazon.ca/s?k=boat+headphones&ref=cs_503_search'

driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

div_h = soup.find("div", id="h")
captcha=soup.find('form',action='/errors/validateCaptcha')

while   div_h or captcha:
    driver.refresh()
    updated_url = driver.current_url
    url = updated_url

    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    captcha=soup.find('form',action='/errors/validateCaptcha')


    div_h = soup.find("div", id="h")
    if (div_h==None) and (captcha==None):
        break  

deliver_to_link = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link"))
)
deliver_to_link.click()

postcode_input1 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "GLUXZipUpdateInput_0"))
)
postcode_input2 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "GLUXZipUpdateInput_1"))
)

postcode_input1.clear()
postcode_input1.send_keys("T0A")
postcode_input2.clear()
postcode_input2.send_keys("0A0")

apply_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "GLUXZipUpdate"))
)
apply_button.click()

print("Postcode applied successfully.")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-price-whole")))

html_after_apply = driver.page_source

with open("amazon_page_after_apply.html", "w", encoding="utf-8") as f:
    f.write(html_after_apply)


soup = BeautifulSoup(html_after_apply, 'html.parser')


updated_url = driver.current_url
print(updated_url)
url = updated_url

driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
price = soup.find('div', class_='a-section a-spacing-none a-spacing-top-small s-price-instructions-style')
price = price.find('span', class_='a-offscreen')

if price:
    print('Price:', price.get_text())
else:
    print('Price not found')
