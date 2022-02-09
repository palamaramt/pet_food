from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

def price_finder(service,website,name,css):
    browser = webdriver.Firefox(service = service)
    browser.get(website)

    price = browser.find_element(By.CSS_SELECTOR, css)
    #price = browser.find_element_by_css_selector('div.PriceRowContainer-sc-1wlo6zv-1.fPOcHS')
    print(name + " Price: " + price.text)

    time.sleep(3)
    browser.close()
    return price