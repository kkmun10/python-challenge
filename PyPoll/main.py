import os
import csv	

poll = os.path.join("resources", "election_data.csv")

#make variables
votes = 0
candidate_list = []
candidate = " "
stockham_total = 0
diana_total = 0
doane_total = 0
winner_total = 0
winner = " "

#open file
with open(poll) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	header = next(csv_reader)
	
	for row in csv_reader:
		#count all votes
		votes = votes + 1
		
		#make list of candidate names
		candidate = row[2]
		if candidate not in candidate_list:
			candidate_list.append(candidate)

		#count how many votes each candiate has
		if (candidate == "Charles Casper Stockham"):
			stockham_total += 1
			#check if they have the most votes
			if winner_total < stockham_total:
				winner_total = stockham_total
				winner = candidate
		#check for new candidate
		elif (candidate == "Diana DeGette"):
			diana_total += 1
			if winner_total < diana_total:
				winner_total = diana_total
				winner = candidate
		#check for new candidate
		elif (candidate == "Raymon Anthony Doane"):
			doane_total += 1
			if winner_total < doane_total:
				winner_total = doane_total
				winner = candidate
		

#find percentage for each candidate
stockham_percent = round(stockham_total / votes * 100, 3)
diana_percent = round(diana_total / votes * 100, 3)
doane_percent = round(doane_total / votes * 100, 3)
       
#print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: ", (votes))
print("-------------------------")
print(f"{(candidate_list[0])}:  {stockham_percent}% ({(stockham_total)})")
print(f"{(candidate_list[1])}:  {diana_percent}% ({(diana_total)})")
print(f"{(candidate_list[2])}:  {doane_percent}% ({(doane_total)})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#create an output

output_file = os.path.join("analysis", "pypoll_analysis.csv")
with open(output_file,"w") as datafile:
	datafile.write("Election Results")
	datafile.write("\n")
	datafile.write("-------------------------")
	datafile.write("\n")
	datafile.write(f"Total Votes: {votes}")
	datafile.write("\n")
	datafile.write("-------------------------")
	datafile.write("\n")
	datafile.write(f"{(candidate_list[0])}:  {stockham_percent}% ({(stockham_total)})")
	datafile.write("\n")
	datafile.write(f"{(candidate_list[1])}:  {diana_percent}% ({(diana_total)})")
	datafile.write("\n")
	datafile.write(f"{(candidate_list[2])}:  {doane_percent}% ({(doane_total)})")
	datafile.write("\n")
	datafile.write("-------------------------")
	datafile.write("\n")
	datafile.write(f"Winner: {winner}")
	datafile.write("\n")
	datafile.write("-------------------------")





	
		


