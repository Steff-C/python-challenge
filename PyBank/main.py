import os
import csv

# Path to resources folder and CSV
budgetfile_path = os.path.join("Resources", "budget_data.csv")
print(budgetfile_path)

# Open CSV File and read header
with open(budgetfile_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Assign Variables
    TotalMonths = 0
    NetProfitLoss = 0
    AvgChange = 0
    GreatestIncrease = 0
    GreatestDecrease = 0 
    Previous = 0
    Current = 0
    Counter = 0

    for row in csvreader:
        Counter = Counter+1
        month = row [0]
        profitloss = int(row[1])
        TotalMonths = TotalMonths+1
        NetProfitLoss = NetProfitLoss + profitloss

