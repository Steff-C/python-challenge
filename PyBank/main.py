import os
import csv

# Path to resources folder and CSV
budgetfile_path = os.path.join("Resources", "budget_data.csv")
#   print(budgetfile_path)

# Open CSV File and read header
with open(budgetfile_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Read Header
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

# Assign Variables    
    TotalMonths =0
    TotalProfitLoss =0
    AvgDifference =0
    GreatestIncrease =0
    GreatestIncreaseMonth = ""
    GreatestDecrease = 0 
    GreatestDecreaseMonth = ""
    PreviousTotal =0
    CurrentTotal =0
    Counter =0
    i =0
    
    for row in csvreader:
        i += 1
        TotalMonths = TotalMonths+1
        if i == 1:
            PreviousTotal = int(row[1])
            TotalProfitLoss = int(row[1])
            Counter = Counter+1
        else:
        
              
# Calculate Greatest Increase       
            if GreatestIncrease < (int(row[1]) - PreviousTotal):
                GreatestIncrease= (int(row[1]) - PreviousTotal)
                GreatestIncreaseMonth = row[0]
        
# Calculate Greatest Decrease
            if GreatestDecrease > (int(row[1]) - PreviousTotal):
                GreatestDecrease= (int(row[1]) -PreviousTotal)
                GreatestDecreaseMonth = row[0]

            AvgDifference += int(row[1])-PreviousTotal
            TotalProfitLoss += int(row[1])
            Counter = Counter + 1
            PreviousTotal= int(row[1])

Counter = Counter - 1        

# Calculate Average Net Change
AverageChange = AvgDifference/(Counter)



    
 # Print  Answers to Terminal  
print(f"Financial Analysis")
print(f"----------------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${TotalProfitLoss}")
print(f"Average Change: ${AverageChange:.2f}")
print(f"Greatest Increase in Profits: {GreatestIncreaseMonth} (${GreatestIncrease}) ") 
print(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} (${GreatestDecrease})")

# Export Answers to Text File
Text_File_Export = os.path.join("analysis", "budget_analysis.txt")
with open(Text_File_Export, 'w', newline='') as csvfile:
    print(f"Financial Analysis",file=csvfile)
    print(f"----------------------------------",file=csvfile)
    print(f"Total Months: {TotalMonths}",file=csvfile)
    print(f"Total: ${TotalProfitLoss} ",file=csvfile)
    print(f"Average Change: ${AverageChange:.2f}",file=csvfile)
    print(f"Greatest Increase in Profits: {GreatestIncreaseMonth} $({GreatestIncrease})",file=csvfile) 
    print(f"Greatest Decrease in Profits: {GreatestDecreaseMonth} $({GreatestDecrease})",file=csvfile)
