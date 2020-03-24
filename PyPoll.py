import os
import csv

file = os.path.join("Resources","election_data.csv")

total_votes = 0

#setting candidate and number of volutes as key and values in dictionary
vote_counter = {}

#reading csv file
with open(file) as data:
    csvreader = csv.reader(data,delimiter = ",")
    header = next(csvreader)
    # for each row in the data, if there's a new candidate then start from one and add as candidate comes up
    for row in csvreader:
        candidate = row[2]
        if candidate in vote_counter.keys():
            vote_counter[candidate] += 1
        else:
            vote_counter[candidate] = 1
    
        total_votes += 1

#print(vote_counter)    
winner = max(vote_counter, key = vote_counter.get)

Results = f"""
Election Reults
-------------------------
Total Votes: {total_votes}
-------------------------"""

for k, v in vote_counter.items():
    percentage = v / total_votes
    Results += k + ': ' + '{:.3%}'.format(percentage) + ', (' + str(v) +')\n'

Results += f"""-------------------------
Winner: {winner}
-------------------------"""
print(Results)

output_file = "PyPoll_output.txt"
with open(output_file, "w") as doc:
    doc.write(Results)