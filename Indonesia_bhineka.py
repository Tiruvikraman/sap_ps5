from selenium import webdriver
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('headless')  # Run Chrome in headless mode, i.e., without a GUI
driver = webdriver.Chrome(options=options)

try:
    # Load the page
    driver.get('https://www.bhinneka.com/jual?cari=i+phone+15&order=')
    html = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all <span> elements containing the price
    price_spans = soup.find_all('span', class_='oe_currency_value')

    # Extract and print the price from each <span> element
    for price_span in price_spans:
        price = price_span.text.strip()
        print('Price:', price)
    
except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the WebDriver
    driver.quit()
