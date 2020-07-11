import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

# Global Variables dates(months),PLSum(Profit/loss sum), PL1(Profit/loss month 1), PL2 (Profit/loss month 2), PLdif (difference in profit/loss from PL1 & PL2)
Vid = 0
#PLSum = 0
#PL1 = 0
#PL2 = 0
#PLdif = 0



# Open and read csv
with open(election_data_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

# Read the header row first
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

# Caculates number of months
    first_row = next(csvreader)
    #PL1 = int(first_row[1])
    Vid = Vid + 1

# Interage through each row of the data after the header
    for row in csvreader:
        Vid = Vid + 1
        #PLSum = PLSum + int(row[1])
        #PL2 = int(row[1])
        #PLdif = PL2-PL1
        #print(PLdif)
        ##print(PLSum)

# Print to screen
print("------------------------")
print(f"Total Votes: {Vid}")
print("------------------------")
       
# Write to file
f = open("PyElect.txt", "w")
f.write(f"----------------------\n")
f.write((f"Total Votes: {Vid}\n"))
f.write(f"----------------------\n")
#f.write((f"Total: {PLSum}\n"))
#f.write((f"Average Change: {PLdif}\n"))
f.close()    