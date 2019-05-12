    
# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# Set variables
total_votes = 0
candidate = ""
candidate_list = []
vote_list = []
percent_list = []
winner = ""

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # move to second row, start loop after header 
    csv_header = next(csvreader)
    
    # Begin Loop in second row
    for row in csvreader:
        # total votes
        total_votes += 1
        
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_list.append(1)
        else:
            vote_list[candidate_list.index(row[2])] += 1

# Calculate percent of vote            
percent_list = [(100/total_votes) * i for i in vote_list]

# Find the winner
winner = candidate_list[vote_list.index(max(vote_list))]

# Print to terminal      
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for i in candidate_list:
    print(i + ": " + str(format(percent_list[candidate_list.index(i)], '.3f')) 
        + "% (" + str(vote_list[candidate_list.index(i)]) + ")")
    
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Write to text
f = open("analysis.txt", "w")

f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("-------------------------\n")

for i in candidate_list:
    f.write(i + ": " + str(format(percent_list[candidate_list.index(i)], '.3f')) 
        + "% (" + str(vote_list[candidate_list.index(i)]) + ")\n")
    
f.write("-------------------------\n")
f.write("Winner: " + winner + "\n")
f.write("-------------------------\n")

f.close()
