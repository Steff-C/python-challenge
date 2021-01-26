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
    # print(f"CSV Header: {csv_header}")
        
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
        PPC = (DistinctV/Count)*100
        PercentageVotes.append(PPC)


    WinningNumVotes = max(NumVotes)
    Winner = UniqueCandidates[NumVotes.index(WinningNumVotes)]    

  
# Print  Answers to Terminal  (Copied what I used from PyBank and adjusted as needed)
print(f"Election Results")
print(f"----------------------------------")
print(f"Total Votes: {Count}")
print(f"----------------------------------")
print(f"{UniqueCandidates[0]}: {PercentageVotes[0]:.3f}% ({NumVotes[0]})")
print(f"{UniqueCandidates[1]}: {PercentageVotes[1]:.3f}% ({NumVotes[1]})")
print(f"{UniqueCandidates[2]}: {PercentageVotes[2]:.3f}% ({NumVotes[2]})")
print(f"{UniqueCandidates[3]}: {PercentageVotes[3]:.3f}% ({NumVotes[3]})")
print(f"----------------------------------")
print(f"Winner: {Winner}")
print(f"----------------------------------")

# Export Answers to Text File (Copied what I used from PyBank and adjusted as needed)
Text_File_Export = os.path.join("analysis", "election_data.txt")
with open(Text_File_Export, 'w', newline='') as csvfile:
    print(f"Election Results",file=csvfile)
    print(f"----------------------------------",file=csvfile)
    print(f"Total Votes: {Count}",file=csvfile)
    print(f"----------------------------------",file=csvfile)
    print(f"{UniqueCandidates[0]}: {PercentageVotes[0]:.3f}% ({NumVotes[0]})",file=csvfile)
    print(f"{UniqueCandidates[1]}: {PercentageVotes[1]:.3f}% ({NumVotes[1]})",file=csvfile)
    print(f"{UniqueCandidates[2]}: {PercentageVotes[2]:.3f}% ({NumVotes[2]})",file=csvfile)
    print(f"{UniqueCandidates[3]}: {PercentageVotes[3]:.3f}% ({NumVotes[3]})",file=csvfile)
    print(f"----------------------------------",file=csvfile)
    print(f"Winner: {Winner}",file=csvfile)
    print(f"----------------------------------",file=csvfile)
    