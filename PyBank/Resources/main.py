
# Allows path creation across operating system
import os
import csv


total_months = 0
total_profit = 0
average_change = 0
greatest_increase = 0
max_row = ""
greatest_decrease = 0
min_row = ""

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter="-")

    for row in csvreader:
        if row[0] == "Jan" or row[0] == "Feb" or row[0] == "Mar" or row[0] == "Apr" or row[0] == "May" or row[0] == "Jun" or row[0] == "Jul" or row[0] == "Aug" or row[0] == "Sep" or row[0] == "Oct" or row[0] == "Nov" or row[0] == "Dec":

            total_months = total_months + 1



with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    date=csv_header.index("Date")
    profit_losses=csv_header.index("Profit/Losses")

    print(f"CSV Header: {csv_header}")
 

    for row in csvreader:
        total_profit = total_profit + float(row[1])


        
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        if float(row[1]) > greatest_increase:
            greatest_increase = float(row[1])
            max_row = row
        elif float(row[1]) < greatest_decrease:
            greatest_decrease = float(row[1])
            min_row = row


average_change = total_profit / total_months


print("")
print("Financial Analysis")
print("----------------------------------------------")
print("")
print(f"Total Number of Months: {total_months}")
print(f"Net Total Amount: {total_profit}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profit is: {max_row}")
print(f"Greatest Decrease in Profit is: {min_row}")