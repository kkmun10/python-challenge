import os
import csv	

budget_data = os.path.join("resources", "budget_data.csv")

#make lists to store 
pnl = []
month_list = []
monthly_changes = []

with open(budget_data) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	header = next(csv_reader)
	
	#assign row to each list
	for row in csv_reader:
		month_list.append(row[0])
		pnl.append(int(row[1]))

	for i in range(len(pnl)-1):
		monthly_changes.append(pnl[i+1]-pnl[i])

#find max and min of profit and loss

max_increase = max(monthly_changes)
min_decrease = min(monthly_changes)

#find the month name of profit of and loss

month_increase = monthly_changes.index(max(monthly_changes))+1
month_decrease = monthly_changes.index(min(monthly_changes))+1	


#print values 

print("Financial Analysis")
print("------------------------")
print(f"Total Months: ", len(month_list))
print(f"Total: $", sum(pnl))
print(f"Average Change: {sum(monthly_changes)/len(monthly_changes)}")
print(f"Greatest Increase in Profits: {month_list[month_increase]} (${str(max_increase)})")
print(f"Greatest Decrease in Profits: {month_list[month_decrease]} (${str(min_decrease)})")

#create an output

output_file = os.path.join("analysis", "pybank_analysis.csv")
with open(output_file,"w") as datafile:
	datafile.write("Financial Analysis")
	datafile.write("\n")
	datafile.write("------------------------")
	datafile.write("\n")
	datafile.write(f"Total Months: {len(month_list)}")
	datafile.write("\n")
	datafile.write(f"Total: ${sum(pnl)}")
	datafile.write("\n")
	datafile.write(f"Average Change: {sum(monthly_changes)/len(monthly_changes)}")
	datafile.write("\n")
	datafile.write(f"Greatest Increase in Profits: {month_list[month_increase]} (${str(max_increase)})")
	datafile.write("\n")
	datafile.write(f"Greatest Decrease in Profits: {month_list[month_decrease]} (${str(min_decrease)})")




#end