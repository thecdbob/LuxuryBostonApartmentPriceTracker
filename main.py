from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://500oceanavenue.com/floorplans/s2-f/')
print(driver.page_source)
driver.quit()

# b_price in each floor plan is where the price is

# use selenium to scape a website for apartment prices
# the website is https://jmaldencenter.com/floor-plans/
# use selenium to scrape the website for the price of each apartment
# save the prices to a list
# print the list of prices
# print the average price of all the apartments

#store dates as either epoch time or a string
#store data as json