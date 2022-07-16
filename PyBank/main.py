
import os
import csv
csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    total_months = 0
    total_profitsorlosses = 0
    pl_value= 0
    period_changes=[]
    months = []

    for row in csvreader:
    
        total_months+= 1
        total_profitsorlosses += int(row[1])
        present_change = int(row[1]) - pl_value
        pl_value = int(row[1])
        if present_change != int(row[1]):
            period_changes.append(present_change)
        months.append(str(row[0]))
average_change = round(sum(period_changes)/len(period_changes),2)
max_value= max(period_changes)
max_index = period_changes.index(max_value)
month_max=months[max_index]
min_value= min(period_changes)
min_index = period_changes.index(min_value)
month_min=months[min_index]

printanalysis= (f'''Financial Analysis
----------------------------------------
Total Months: {total_months}
Total: ${total_profitsorlosses}
Average Change: ${average_change}
Greatest Increase in Profits:{month_max} (${max_value})
Greatest Decrease in Profits:{month_min} (${min_value})''')
print(printanalysis)

output_path = os.path.join("analysis", "analysis.txt")
with open(output_path, 'w') as textfile:
    textfile.write(printanalysis)




       
            

    

        


    
    



