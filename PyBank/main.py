#   The total number of months included in the dataset
#   The net total amount of "Profit/Losses" over the entire period
#   The average of the changes in "Profit/Losses" over the entire period
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in losses (date and amount) over the entire period
#   Print the analysis to the terminal and export a text file with the results


# Import OS and CSV
import os
import csv

# Define what Is looked for am looking for
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# add path
budget_data_csv_path = os.path.join("Resource" ,"budget_data.csv")

#   read csv
with open(budget_data_csv_path, newline="") as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    print(f"Header: {csv_header}")
    #This prints -->> Header: Date, Profit/Losses
             
    # Read through each row of data after the header
    for row in csv_reader:

        # Count of months
        count_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
           
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # add each month to the months[]
            months.append(row[0])

            # add each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Loop the profit_loss per month
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes  
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes  
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes 
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


#   Export a text file with the results
budget_file = os.path.join("analysis", "budget_data.txt")
with open(budget_file, "w") as export:

    export.write("Financial Analysis\n")
    export.write("----------------------------\n")
    export.write(f"Total Months:  {count_months}\n")
    export.write(f"Total:  ${net_profit_loss}\n")
    export.write(f"Average Change:  ${average_profit_loss}\n")
    export.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    export.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")

    #hwt3