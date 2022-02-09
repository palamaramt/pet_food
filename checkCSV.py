import csv
import sys


def checkCSV(filename,today):
    # open the csv file
    with open(filename, 'r') as csvfile:
        # read the csv file
        csvfile = csv.reader(csvfile)
        # create empty variable for continuation
        cont = ""
        # go through all lines in the csv
        for lines in csvfile:
            # if today's date is found in the csv, create following options:
            if lines[-1] == today:
                # loop to force user to choose to continue or not
                while cont.lower() != "n" or "y":
                    print("You've already searched for prices today!")
                    cont = input("Would you like to continue? (Y/N): ")
                    # if user chooses to not continue, end program
                    if cont.lower() == "n":
                        sys.exit("Ending program.")
                    # if suer chooses to continue, exit function
                    elif cont.lower() == "y":
                        print("Continuing program.")
                        return
                    # if user makes invalid choice, tell them about it
                    else:
                        print("Please enter a valid answer.")