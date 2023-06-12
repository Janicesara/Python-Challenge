#Importing modules required
import os
import csv

#seting up  path
csv_path=os.path.join('resources','budget_data.csv')

#reading csv file
with open(csv_path) as csvfile:
       #csv reader  delimiter
    csv_reader=csv.reader(csvfile,delimiter=",")

    #header
    csv_header=next(csv_reader)

    #Empty list
    date=[]
    profits=[]
    profit_change=[]

    #looping
    for row in csv_reader:
        #total number of months is calculated by date column and length
    
        date.append(row[0])
        daterange=len(date)

        #profit to list
        profits.append(int(row[1]))

    # average change
    for i in range(len(profits)-1):
        profit_change.append(profits[i+1]-profits[i])

        average=round(sum(profit_change)/len(profit_change),2)

    # max and min 
    increase=max(profit_change)
    decrease=min(profit_change)

    #index to find month
    max_month=profit_change.index(max(profit_change))+1
    min_month=profit_change.index(min(profit_change))+1
   
#printing Financial Analysis
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {daterange}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {date[max_month]} ${increase}")
print(f"Greatest Decrease in Profits: {date[min_month]} ${decrease}")
        
#text file summary written
txtpath=os.path.join('pybank.txt')
with open(txtpath,"w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------------\n")
    txtfile.write(f"Total Months: {daterange}\n")
    txtfile.write(f"Total: ${sum(profits)}\n")
    txtfile.write(f"Average Change: ${average}\n")
    txtfile.write(f"Greatest Increase in Profits: {date[max_month]} $({increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {date[min_month]} $({decrease})\n")
    