import os
import csv

#Variables, lists and dictionary to be used throughout the code
total_votes = 0
candidate_name = []
candidate_votes = []
vote_number1 = 0
vote_number2 = 0
vote_number3 = 0
percentage1 = 0
percentage2 = 0
percentage3 = 0
number_of_candidates = 0
candidate1_results = []
candidate2_results = []
candidate3_results = []
outcome = {}
winner = ""

#Creates path to the csv file
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#Opens file and sets the headers of the data
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    ballot = csv_header.index("Ballot ID")
    county = csv_header.index("County")
    candidate = csv_header.index("Candidate")

    #Wanted to see what the Headers were
    print(f"CSV Header: {csv_header}")


    #Loops through each row and column of the csv file to search for unique names
    #Places each unique name in a list through the append function
    for row in csvreader:
        if row[2] not in candidate_name:
            candidate_name.append(row[2])

    #Shows how many unique candidates there are        
    number_of_candidates = len(candidate_name)
    print(f"There are {number_of_candidates} candidates")


#Opens csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skips the first row because they were the Headers
    next(csvreader)

    #Loops through each row after the Header row to to count the total number of votes placed
    for row in csvreader:
        if row != "":
            total_votes = total_votes + 1
            #Adds the name of each candidate who was voted for
            candidate_votes.append(row[2])
        
#Counts the votes for each candidate and assigns it to a variable
vote_number1 = candidate_votes.count(candidate_name[0])
vote_number2 = candidate_votes.count(candidate_name[1])
vote_number3 = candidate_votes.count(candidate_name[2])

#Used to find the percentage of votes each candidate received 
percentage1 = (vote_number1 / total_votes) * 100
percentage2 = (vote_number2 / total_votes) * 100
percentage3 = (vote_number3 / total_votes) * 100

#Creates a list for each candidate to show their vote percentage and the vote total
candidate1_results = [percentage1, vote_number1]
candidate2_results = [percentage2, vote_number2]
candidate3_results = [percentage3, vote_number3]


#Creates a dictionary with the lists for each candidate name
outcome = {"Charles Casper Stockham": candidate1_results,
           "Diana DeGette": candidate2_results,
           "Raymon Anthony Doane": candidate3_results
           }          

#If statements used to find who received the most votes
#Uses the and conditional statement to show that their vote total must be the highest
if vote_number1 > vote_number2 and vote_number1 > vote_number3:
    winner = candidate_name[0]
elif vote_number2 > vote_number1 and vote_number2 > vote_number3:
    winner = candidate_name[1]
elif vote_number3 > vote_number1 and vote_number3 > vote_number2:
    winner = candidate_name[2]


#Prints out the analysis based ont he CSV
print(candidate_name)

print("")
print("Election Results")
print("-----------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------------------")
print("Candidate Name : [Percentage of Votes (%), Total Number of Votes]")
print("")
print(candidate_name[0],f': {outcome["Charles Casper Stockham"]}')
print("")
print(candidate_name[1],f': {outcome["Diana DeGette"]}')
print("")
print(candidate_name[2],f': {outcome["Raymon Anthony Doane"]}')
print("-----------------------------------------------------")
print(f'Winner : {winner}')
print("-----------------------------------------------------")

#Used to create a new path towards the Analysis folder
output_path = os.path.join("..", "Analysis", "PyPoll_Results.txt")

#Creates a Text datafile
with open(output_path, 'w') as datafile:
    writer = csv.writer(datafile, delimiter=',')

    #Writes the analysis of the csv data as a text file
    writer.writerow(["Election Results"])
    writer.writerow(["-----------------------------------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["-----------------------------------------------------"])
    writer.writerow(["Candidate Name : Percentage of Votes (%), Total Number of Votes"])
    writer.writerow([candidate_name[0],f': {outcome["Charles Casper Stockham"]}'])
    writer.writerow([candidate_name[1],f': {outcome["Diana DeGette"]}'])
    writer.writerow([candidate_name[2],f': {outcome["Raymon Anthony Doane"]}'])
    writer.writerow(["-----------------------------------------------------"])
    writer.writerow([f'Winner : {winner}'])
    writer.writerow(["-----------------------------------------------------"])