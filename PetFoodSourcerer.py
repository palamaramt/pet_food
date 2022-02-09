# import specific libraries
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from datetime import date
# import libraries
import time
import re
import csv
import sys
# get custom functions
from appendToCSV import appendToCSV
from priceFinder import priceFinder
from checkCSV import checkCSV

# get today's date
today = date.today().strftime("%m/%d/%y")
# make empty dictionary for completed date
pricesList= []
# looking for cat or dog food?
species = "dog"

# Check if prices have been checked already
filename = "csvs/dogFoodPriceRecords.csv"
checkCSV(filename,today)

# get only numbers
numbers = re.compile(r'\d+(?:\.\d+)?')

# list of website: petco, petsmart
websites = {
    'Petco': ['https://www.petco.com/shop/en/petcostore/product/blue-buffalo-chicken-and-brown-rice-adult-dog-food','div.PriceRowContainer-sc-1wlo6zv-1.fPOcHS'],
    'PetSmart': ['https://www.petsmart.com/dog/food/dry-food/blue-buffalo-life-protection-formula-adult-dry-dog-food---chicken-and-brown-rice-41846.html?cgid=100246','span.product-price-discount']
    }

# change path to match your directory structure for the geckodriver
gecko_path = "/Users/Marissa/AppData/Local/Programs/Python/Python39/geckodriver.exe"
service = Service(executable_path=gecko_path)

# iterate through the websites dictionary and find the prices listed on the websites
for name,data in websites.items():
    # dictionary with empty values
    myDict = {"Name": [], "Price": [], "Date": []}
    # get website url
    website = data[0]
    # get what specifically you are looking for in the website
    css = data[1]
    # use priceFinder.py to find the price
    price = priceFinder(service,website,name,css)
    # strip any words and only get numbers for the prices
    price = numbers.findall(price)
    # put name of website, the price, and the date into dictionary
    myDict["Name"] = name
    myDict["Price"] = price[0]
    myDict["Date"] = today
    # append the dictionary to the list of prices
    pricesList.append(myDict)

# call appendToCSV.py to append data to end of csv
appendToCSV(pricesList,species,today,filename)
