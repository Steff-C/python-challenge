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
    TotalProfitLoss = 0
    Difference = 0
    GreatestIncrease = 0
    GreatestIncreaseMonth = ""
    GreatestDecrease = 0 
    GreatestDecreaseMonth = ""
    PreviousTotal = 0
    CurrentTotal = 0
    Counter = 0
    TotalAmount = 0

    for row in csvreader:
        Counter = Counter+1
        Month = row [0]
        profitloss = int(row[1])
        TotalMonths = TotalMonths+1
        TotalProfitLoss = TotalProfitLoss + profitloss
        PreviousAmount = int(row[1])
       
# Calculate Greatest Increase       
        if profitloss>GreatestIncrease:
            GreatestIncrease=profitloss
            GreatestIncreaseMonth=Month
        
# Calculate Greatest Decrease
        if profitloss<GreatestDecrease:
            GreatestDecrease=profitloss
            GreatestDecreaseMonth=Month
        if Counter>1:
            CurrentTotal=profitloss
            Difference=Difference+CurrentTotal-PreviousTotal
        PreviousTotal=profitloss

# Calculate Average Net Change
AverageChange = Difference/(TotalMonths-1)



    
 # Print  Answers to Terminal  
print(f"Financial Analysis")
print(f"----------------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${TotalProfitLoss} ")
print(f"Average Change: ")
print(f"Greatest Increase in Profits: ") 
print(f"Greatest Decrease in Profits: ")

# Export Answers to Text File
Text_File_Export = os.path.join("analysis", "budget_analysis.txt")
with open(Text_File_Export, 'w', newline='') as csvfile:
    print(f"Financial Analysis",file=csvfile)
    print(f"----------------------------------",file=csvfile)
    print(f"Total Months: {TotalMonths}",file=csvfile)
    print(f"Total: ${TotalProfitLoss} ",file=csvfile)
    print(f"Average Change: ",file=csvfile)
    print(f"Greatest Increase in Profits: ",file=csvfile) 
    print(f"Greatest Decrease in Profits: ",file=csvfile)
