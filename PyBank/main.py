import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

dates = 0
PLSum = 0
PL1 = 0
PL2 = 0
PLdif = 0


# Open and read csv
with open(budget_data_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

# Read the header row first
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    first_row = next(csvreader)
    PL1 = int(first_row[1])
    dates = dates + 1

# Read through each row of the data after the header
    for row in csvreader:
        dates = dates + 1
        PLSum = PLSum + int(row[1])
        PL2 = int(row[1])
        PLchange = PL1-PL2
        print(PLchange)
        break
print(f"{dates}")
       

f = open("PyBank.txt", "w")
f.write((f"{dates}"))
f.close()    
# The total number of months included in the dataset
# Create dictionary to hold data "Months" and "Profit/loss"
#data = {}
#data = dict()
#data = {"date": "Profit/Loss"}
#print(f{})

# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

