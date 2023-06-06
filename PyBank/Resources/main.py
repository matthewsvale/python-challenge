
# Allows path creation across operating system
import os
import csv

#Variables to be used throughout the code
total_months = 0
total_profit = 0
average_change = 0
greatest_increase = 0
max_row = ""
greatest_decrease = 0
min_row = ""

#Creates a path towards the Resrouces and csv needed 
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Opens csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    #Initially uses "-" as a delimiter, to seprate the month and the year for later use
    csvreader = csv.reader(csvfile, delimiter="-")

    #Loops through each row, but specifically the first column that only holds the months
    for row in csvreader:
        if row[0] == "Jan" or row[0] == "Feb" or row[0] == "Mar" or row[0] == "Apr" or row[0] == "May" or row[0] == "Jun" or row[0] == "Jul" or row[0] == "Aug" or row[0] == "Sep" or row[0] == "Oct" or row[0] == "Nov" or row[0] == "Dec":

            total_months = total_months + 1


#Opens the csv file again, but uses "," as the delimiter
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Finds the headers of the data set
    csv_header = next(csvreader)
    date=csv_header.index("Date")
    profit_losses=csv_header.index("Profit/Losses")

    print(f"CSV Header: {csv_header}")
 
    #Loops through each row of the data, using the float function to add all of the profit changes into total_profit
    for row in csvreader:
        total_profit = total_profit + float(row[1])


#Opens csv file        
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skips the first row in order to avoid the headers
    next(csvreader)

    #Loops through each row, utilizing the If statements to find the maximum and minimum numbers
    #Also stores the row where the maximum and minimum values are for later use
    for row in csvreader:
        if float(row[1]) > greatest_increase:
            greatest_increase = float(row[1])
            max_row = row
        elif float(row[1]) < greatest_decrease:
            greatest_decrease = float(row[1])
            min_row = row

#Calculates the average change based on the total profit and the amount of months
average_change = total_profit / total_months

#Print out the analysis based on the code
print("")
print("Financial Analysis")
print("----------------------------------------------")
print("")
print(f"Total Number of Months: {total_months}")
print(f"Net Total Amount: {total_profit}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profit is: {max_row}")
print(f"Greatest Decrease in Profit is: {min_row}")


#Opens a new path to the Analysis folder for the PyBank
output_path = os.path.join("..", "Analysis", "PyBank_Results.txt")

#Looks to create the text file for the folder
with open(output_path, 'w') as datafile:
    writer = csv.writer(datafile, delimiter=',')

    #Writes the analysis onto the text file
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-----------------------------------------------------"])
    writer.writerow([f"Total Number of Months: {total_months}"])
    writer.writerow([f"Net Total Amount: {total_profit}"])
    writer.writerow([f"Average Change: {average_change}"])
    writer.writerow([f"Greatest Increase in Profit is: {max_row}"])
    writer.writerow([f"Greatest Decrease in Profit is: {min_row}"])