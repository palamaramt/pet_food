from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time


website = 'https://www.petco.com/shop/en/petcostore/product/blue-buffalo-chicken-and-brown-rice-adult-dog-food'

gecko_path = "/Users/Marissa/AppData/Local/Programs/Python/Python39/geckodriver.exe"
service = Service(executable_path=gecko_path)
browser = webdriver.Firefox(service = service)
browser.get(website)

price = browser.find_element(By.CSS_SELECTOR, 'div.PriceRowContainer-sc-1wlo6zv-1.fPOcHS')
#price = browser.find_element_by_css_selector('div.PriceRowContainer-sc-1wlo6zv-1.fPOcHS')
print("Petco Price: " + price.text)

time.sleep(3)
browser.close()
browser.quit()