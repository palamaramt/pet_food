import csv
import sys


def appendToCSV(fields,pricesDict,species,today,filename):
    # Determine which csv to print to
    #if species == "dog":
    #    # name of csv
    #    filename = "csvs/dogFoodPriceRecords.csv"
    #else:
    #    print("Choose a species! Cat will be added later.")
 
    with open(filename, 'a+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        #writer.writeheader()
        writer.writerows(pricesDict)
