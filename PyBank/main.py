print("Hello from PyBank")

import os
import csv

# Path to resources folder and CSV
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Open CSV File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

print (csvreader)

# Read Header
csv_header = next(csvreader)

# Assign Variables
TotalMonths = 0
NetProfitLoss = 0
AvgChange = 0
GreatestIncrease = 0
GreatestDecrease = 0 
Previous = 0
Current = 0
Counter = 0
