#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

# Import Modules
import os
import csv

# CSV Path
csvpath = os.path.join("..", "PyBank","Resources", "budget_data.csv")

# Variables - Integer/String
total_months = 0
prev_profit_loss = 0
total_profit_loss = 0
month_change = 0
average_month_change = 0
total_month_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

# CSV Open
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the Header and start at second row
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        # total number of months
        total_months += 1
        
        # total net profit/loss
        total_profit_loss += int(row[1])
        
        # calculate the monthly change in profit/loss
        if total_months > 1:
            month_change = int(row[1]) - prev_profit_loss
            
        # total monthly change
        total_month_change += month_change
        
        # set profit/loss value for previous month
        prev_profit_loss = int(row[1])
        
        # greatest increase in profits
        if month_change > greatest_increase:
            greatest_increase = month_change
            greatest_increase_month = row[0]
        
        # calculate greatest decrease in losses
        if month_change < greatest_decrease:
            greatest_decrease = month_change
            greatest_decrease_month = row[0]

# calculate average change between months        
average_month_change = total_month_change / (total_months - 1)

# Print the analysis to terminal
print("Financial Analysis")
print("----------------------------")        
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(format(average_month_change, '.2f')))
print("Greatest Increase in Profits: " + greatest_increase_month 
      + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month 
      + " ($" + str(greatest_decrease) + ")")

# Write to text file
f = open("analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")        
f.write("Total Months: " + str(total_months) + "\n")
f.write("Total: $" + str(total_profit_loss) + "\n")
f.write("Average Change: $" + str(format(average_month_change, '.2f')) + "\n")
f.write("Greatest Increase in Profits: " + greatest_increase_month 
      + " ($" + str(greatest_increase) + ")\n")
f.write("Greatest Decrease in Profits: " + greatest_decrease_month 
      + " ($" + str(greatest_decrease) + ")\n")
f.close()