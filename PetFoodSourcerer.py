from selenium import webdriver
import time


website = 'https://www.petco.com/shop/en/petcostore/product/blue-buffalo-chicken-and-brown-rice-adult-dog-food'

browser = webdriver.Firefox(executable_path="/Users/Marissa/AppData/Local/Programs/Python/Python39/geckodriver.exe")
browser.get(website)

price = browser.find_element_by_css_selector('div.PriceRowContainer-sc-1wlo6zv-1.fPOcHS')
print("Price: " + price.text)

time.sleep(3)
browser.close()
