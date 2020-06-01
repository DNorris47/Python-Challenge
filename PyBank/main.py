import os 
import csv

'''
Your task is to create a Python script that analyzes the records to calculate each of the following:

DONE-The total number of months included in the dataset
DONE-The net total amount of "Profit/Losses" over the entire period
DONE-The average of the changes in "Profit/Losses" over the entire period
DONE-The greatest increase in profits (date and amount) over the entire period
DONE-The greatest decrease in losses (date and amount) over the entire period

As an example, your analysis should look similar to the one below:

Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)

In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''

# READ THE SOURCE FILE

file_path = os.path.join('Resources','budget_data.csv')

# create empty lists to hold our data
month_list = []
profit_and_loss = []

i = 0
with open(file_path) as budget_data: 
    reader = csv.reader(budget_data)
    for row in reader:
        #print(row)
        #skip the first, header row
        if i > 0:
            month_list.append(row[0])
            profit_and_loss.append(int(row[1])) # force python to treat the data as numbers instead of strings
        i = i + 1

# Create a variable to contain the output.
# It will be printed to the output and saved
# to a file
final_text = ""
final_text += "Total Months : " + str(len(month_list))

# Use str(number) to force python to treat a number as a string, so you can CONCATENATE (add) it to another string
final_text += "\nTotal : $" + str(sum(profit_and_loss))

# Need to create list of p&l changes between periods
#change in P&L = endvalue - startvalue
pl_changes_list = []
for i in range(1,len(profit_and_loss)):
    end_value = profit_and_loss[i]
    start_value = profit_and_loss[i-1]
    change = end_value - start_value
    pl_changes_list.append(change)

#average = sum of the P&L changes / number of months(entries)
sum_of_changes = sum(pl_changes_list)
number_of_entries = len(pl_changes_list)
average_change = round(sum_of_changes / number_of_entries,2)

final_text += ("\nAverage Change : $" + str(average_change))

# Need to create list of p&l changes between periods

# Greatest increase month and amount
Largest_Increase=max(pl_changes_list)
# Find the index of this Value: use list.index(element)
idx = pl_changes_list.index(Largest_Increase)
# need to add 1 to idx, because pl_changes_list starts on the second element from the source list
idx = idx + 1

final_text += ("\nGreatest Increase in Profits : {} (${})".format(month_list [idx], Largest_Increase))

Greatest_Decrease=min(pl_changes_list)
idx = pl_changes_list.index(Greatest_Decrease)
idx = idx + 1

final_text += ("\nGreatest Decrease in Profits : {} (${})".format (month_list [idx] ,Greatest_Decrease))

print(final_text)

file_path = os.path.join('analysis','results.txt')
#print(file_path)
with open(file_path,'w') as fp:
    fp.write(final_text)
