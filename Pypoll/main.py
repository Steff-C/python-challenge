import os
import csv

# Path to resources folder and CSV
ElectionData_path = os.path.join("Resources", "election_data.csv")
#   print(ElectionData_path)

# Need to know 
# * The total number of votes cast - sum of votes
# * A complete list of candidates who received votes - unique names needed
# * The percentage of votes each candidate won - total # of votes per candidate divided by total votes casted (sum from 1st line above)
# * The total number of votes each candidate won - part one of previus line - total # of votes per candidate
# * The winner of the election based on popular vote. - unique candidate with the highest vote count

# Open CSV File and read header
with open(ElectionData_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# Read Header    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
        
# Assign Variables and List
Count = 0
Candidates = []
UniqueCandidates = []
NumVotes = []
PercentageVotes = []

for row in csvreader:
    Count = Count + 1 
    Candidates.append(row[2])
for Distinct in set(Candidates):
    UniqueCandidates.append(Distinct)
    DistinctV = Candidates.count(Distinct)
    NumVotes.append(DistinctV)
    PPC = (DistinctV/count)*100
    PercentageVotes.append(PPC)

print (count)
        
  
   


