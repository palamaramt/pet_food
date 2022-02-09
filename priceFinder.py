from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

def priceFinder(service,website,name,css):
    browser = webdriver.Firefox(service = service)
    browser.get(website)

    price = browser.find_element(By.CSS_SELECTOR, css).text

    time.sleep(3)
    browser.close()
    return price