from selenium import webdriver
from bs4 import BeautifulSoup

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('headless')  # Run Chrome in headless mode, i.e., without a GUI
driver = webdriver.Chrome(options=options)

try:
    # Load the page
    driver.get('https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=hp+victus+gaming+laptop&_sacat=0')

    # Get the page source after JavaScript execution
    html = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <li> elements
    items = soup.find_all('li', class_='s-item')
    price=[]
    # Extract prices for each item
    for item in items:
        price_element = item.find('span', class_='ITALIC')
        status = item.find('span',class_='SECONDARY_INFO').text.strip()
        if price_element and status!='Pre-owned':
            a = price_element.text.strip()
            price.append(a)
            break

        else:
            pass
    for j in price:
        print(j)        
except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the WebDriver
    driver.quit()
