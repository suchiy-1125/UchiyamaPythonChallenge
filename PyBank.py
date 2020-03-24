import os
import csv

#open original data csv
file = os.path.join("Resources","budget_data.csv")

#set variable
total_month = 0
total_profit = 0
greatest_inc = 0
greatest_inc_month = ""
greatest_dec = 0
greatest_dec_month = ""

prev_pl = 0
changes = []

#reading csv file
with open(file)as data:
    csvreader = csv.reader(data, delimiter = ",")
    header = next(csvreader)

    #for each row date is in 1st column and rofit is in second column
    for row in csvreader:
        date = row[0]
        pl = int(row[1])
        #total profit is adding all the profit
        total_profit = total_profit + pl
        #total month is adding all the months
        total_month = total_month + 1

        #change is profit before the previous profit
        change = pl - prev_pl
        if total_month != 1:
            changes.append(change)
        #for each row if the new calculated change is bigger than the previous changes calculated, then it's counted as greatest increase
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_month = date
        #for each row if the new calculated change is smaller than the previous changes calculated, then it's counted as greatest decrease    
        elif change <greatest_dec:
            greatest_dec = change
            greatest_dec_month = date
        prev_pl = pl
        
#calculation       
avg_change = int(round(sum(changes)/len(changes),2))
#monthly_avg_profit = int(round(total_profit/total_month,0))

#printout
analysis = f"""
Total Profit: ${total_profit}
Total months: {total_month}
Monthly Average Change: ${avg_change}
Greatest Increase: {greatest_inc_month}, ${greatest_inc}
Greatest Decrease: {greatest_dec_month}, ${greatest_dec}"""

print(analysis)

output_file = "output.txt"
with open(output_file, "w") as doc:
    doc.write(analysis)