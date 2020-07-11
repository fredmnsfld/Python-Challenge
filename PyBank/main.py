import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Global Variables dates(months),PLSum(Profit/loss sum), PL1(Profit/loss month 1), PL2 (Profit/loss month 2), PLdif (difference in profit/loss from PL1 & PL2)
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

# Caculates number of months
    first_row = next(csvreader)
    PL1 = int(first_row[1])
    dates = dates + 1

# Interage through each row of the data after the header
    for row in csvreader:
        dates = dates + 1
        PLSum = PLSum + int(row[1])
        PL2 = int(row[1])
        PLdif = PL2-PL1
        print(PLdif)
        #print(PLSum)

# print output to screen
print(f"----------------------\n")
print((f"Total Months: {dates}\n"))
print((f"Total: {PLSum}\n"))
print((f"Average Change: {PLdif}\n"))

# Write to file
f = open("PyBank.txt", "w")
f.write(f"----------------------\n")
f.write((f"Total Months: {dates}\n"))
f.write((f"Total: {PLSum}\n"))
f.write((f"Average Change: {PLdif}\n"))
f.close()    


