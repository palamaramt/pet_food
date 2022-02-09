from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

from price_finder import price_finder

# list of website: petco, petsmart
websites = {
    'Petco': ['https://www.petco.com/shop/en/petcostore/product/blue-buffalo-chicken-and-brown-rice-adult-dog-food','div.PriceRowContainer-sc-1wlo6zv-1.fPOcHS'],
    'PetSmart': ['https://www.petsmart.com/dog/food/dry-food/blue-buffalo-life-protection-formula-adult-dry-dog-food---chicken-and-brown-rice-41846.html?cgid=100246','span.product-price-discount']
    }

gecko_path = "/Users/Marissa/AppData/Local/Programs/Python/Python39/geckodriver.exe"
service = Service(executable_path=gecko_path)

for name,data in websites.items():
    website = data[0]
    css = data[1]
    price_finder(service,website,name,css)