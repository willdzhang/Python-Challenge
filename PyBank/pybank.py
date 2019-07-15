import os
import csv

bankcsv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', "budget_data.csv")

# Open and read csv
with open(bankcsv, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    print("Financial Analysis")
    print("----------------------------")

    #Loop for months, total, max, min
    pnlTotal = 0
    months = 0
    maxProfit = 0
    minProfit = 0
    maxMonth = 0
    minMonth = 0
    for row in csvreader:
        months += 1
        pnlTotal += int(row[1])
        if int(row[1]) > int(maxProfit):
            maxProfit = row[1]
            maxMonth = row[0]
        if int(row[1]) < int(minProfit):
            minProfit = row[1]
            minMonth = row[0]
    average = pnlTotal / months
    print(f'Total Months: {months}')
    print(f'Net Total: ${pnlTotal}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {maxMonth} (${maxProfit})')
    print(f'Greatest Decrease in Profits: {minMonth} (${minProfit})') 

    #write to text file
    file = open("budget_output.txt","w+") 
    file.write("Financial Analysis\n") 
    file.write("----------------------------\n") 
    file.write(f'Total Months: {months}\n') 
    file.write(f'Net Total: ${pnlTotal}\n') 
    file.write(f'Average Change: ${average}\n') 
    file.write(f'Greatest Increase in Profits: {maxMonth} (${maxProfit})\n')
    file.write(f'Greatest Decrease in Profits: {minMonth} (${minProfit})\n')
    file.close()