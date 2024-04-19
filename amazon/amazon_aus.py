from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

url = 'https://www.amazon.com.au/s?k=iphone+15&ref=cs_503_search'

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

# Wait for the page to reload or update after applying the postcode
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-price-whole")))

# Get the page source after JavaScript execution
html_after_apply = driver.page_source

# Save the HTML page after applying the postcode
with open("amazon_page_after_apply.html", "w", encoding="utf-8") as f:
    f.write(html_after_apply)


# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_after_apply, 'html.parser')

# Find the price element using BeautifulSoup

updated_url = driver.current_url
print(updated_url)
url = updated_url

# Open the Amazon page in the browser
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
symbol = soup.find('span', class_='a-price-symbol')
price = soup.find('span', class_='a-price-whole')

if price:
    print('Price:', symbol.get_text(), price.get_text())
else:
    print('Price not found')
