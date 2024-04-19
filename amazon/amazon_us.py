from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

url = 'https://www.amazon.com/s?k=boat+headphones&ref=cs_503_search'

driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

div_g = soup.find("a", target="_blank")
print(div_g)
while   div_g:
    driver.refresh()
    updated_url = driver.current_url
    print(updated_url)
    url = updated_url

    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    div_g = soup.find("div", id="g")
    if div_g==None:
        break    
deliver_to_link = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "nav-global-location-popover-link"))
)
deliver_to_link.click()

postcode_input1 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "GLUXZipUpdateInput"))
)

postcode_input1.clear()
postcode_input1.send_keys("10001")


apply_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "GLUXZipUpdate"))
)
apply_button.click()

print("Postcode applied successfully.")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-price-whole")))

html_after_apply = driver.page_source

soup = BeautifulSoup(html_after_apply, 'html.parser')


updated_url = driver.current_url
print(updated_url)
url = updated_url

driver.get(url)

html = driver.page_source

symbol = soup.find('div', class_='puisg-col puisg-col-4-of-12 puisg-col-4-of-16 puisg-col-4-of-20 puisg-col-4-of-24')
symbol = symbol.find('span', class_='a-offscreen')

if symbol:
    print('Price:', symbol.get_text())
else:
    print('Price not found')
