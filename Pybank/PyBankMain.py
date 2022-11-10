## TASK: Analyze the financial records of the company. 

#------Import CVS file
import os
import csv

budget_data_path = os.path.join("PyBank","Resources","budget_data.csv")

#------Read CSV file
with open(budget_data_path,"r") as budget_data:

    csvreader = csv.reader(budget_data, delimiter=',')
    #print(csvreader)

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)

#------Organizing the Data

    
#1. Calculate the total number of months included in the dataset
#need count the months
# date = [csvreader[0]]
# months = dict(date)



# print(f"Months {string.count(date)}")


#2. Calculate the net total amount of "Profit/Losses" over the entire period
#need sum everything at column"Profit/Losses"

    def print_results (results):
        months = str(results[0])
        values = int(results[1])
        total_months = (sum(values))
        print(f"months {total_months}")
    



#3. Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
# need subtract the new month with the previous (with the whole period) and calculate the average from these differences



#4. Calculate the greatest increase in profits (date and amount) over the entire period
# need subtract the new month with the previous (with the whole period) and get the max



#5. Calculate the greatest decrease in profits (date and amount) over the entire period
# need subtract the new month with the previous (with the whole period) and get the min



#6. Print the analysis to the terminal and export a text file with the results