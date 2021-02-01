# Import Dependencies
import os
import csv
import sys

# Identify filepath to import csv file to calculate election results
filepath = os.path.join("Resources","Election_Data.csv")

# Create new lists by column as per the headings on csv file
voter_ID = []
county = []
candidate = []

# Open csv to read, seperate items by splitting with a comma, and delete the heading row to get the vote counts accurately
with open (filepath, 'r', encoding = 'utf-8') as pypoll_data:
    csvreader = csv.reader(pypoll_data, delimiter =",")
    header = next(csvreader, None)

    # Put info from csv file in list
    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

"""Ensure that the CSV information has been inserted to the empty lists
    print(voter_ID)
    print(county)
    print(candidate)
    break
"""
# Get the total number of votes
total_vote = (len(voter_ID))

# Need to determine the # of candidates by printing the unique list to run the for loop below
candidate_list = list(set((candidate)))

#create empty list for the store values for the number of votes received and winning % for each candidate
candidate_vote_count =[]
candidate_percentage = []

# Insert values for vote counts for each candidate and winning % in a for loop
# For Loop will go through all the rows of counting the items candidate list
for x in candidate_list:
        candidate_vote_count.append((candidate.count(x)))
        candidate_percentage.append((candidate.count(x))/(total_vote)*100)

# Find the winner of the election.  This s the person with the most votes with the below function
winner = max(set(candidate), key = candidate.count)

# Output Terminal
# For Loop needed to printout for candidate results, automate the process of listing each item one by one
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_vote}")
print("-----------------------------------")
for index in range(len(candidate_list)):
	print(f"{candidate_list[index]}:  {round(candidate_percentage[index],3)}00% ({candidate_vote_count[index]})")
print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")

# Output for Text File
stdoutOrigin=sys.stdout 
sys.stdout = open("Election_Results.txt", "w")

print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_vote}")
print("-----------------------------------")
for index in range(len(candidate_list)):
	print(f"{candidate_list[index]}:  {round(candidate_percentage[index],3)}00% ({candidate_vote_count[index]})")
print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")
sys.stdout.close()
sys.stdout=stdoutOrigin
