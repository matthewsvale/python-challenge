import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    ballot = csv_header.index("Ballot ID")
    county = csv_header.index("County")
    candidate = csv_header.index("Candidate")

    print(f"CSV Header: {csv_header}")