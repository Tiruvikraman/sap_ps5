from selenium import webdriver
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('headless')  # Run Chrome in headless mode, i.e., without a GUI
driver = webdriver.Chrome(options=options)

try:
    # Load the page
    driver.get('https://www.powerbuy.co.th/search/i%20phone%2015')
    html = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the <div> element containing the price range
    #price_div = soup.find('div', class_='text-xs leading-3 line-through')

    price_spans = soup.find_all('div', class_='text-xs leading-3 line-through')

    # Extract and print the price from each <span> element
    for price_span in price_spans:
        price = price_span.text.strip()
        price = price.encode('utf-8').decode('unicode-escape')
        print('Price:', price)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the WebDriver
    driver.quit()
