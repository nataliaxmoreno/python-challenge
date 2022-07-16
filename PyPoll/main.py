
import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    total_votes = 0
    candidates= []
   
    for row in csvreader:  
        total_votes+= 1
        candidates.append(row[2])
def winnerfinder(candidates):
    return max(set(candidates), key = candidates.count)
 
candidates_counts=[candidates.count(candidate) for candidate in set(candidates)]
percentage= [round((element*100)/total_votes,3) for element in candidates_counts]
results= list(zip(set(candidates),percentage, candidates_counts))

printingresults=(f'''Election Results
----------------------------------------
Total Votes: {total_votes}
----------------------------------------
{results[0][0]}: {results[0][1]}% ({results[0][2]}) 
{results[1][0]}: {results[1][1]}% ({results[1][2]}) 
{results[2][0]}: {results[2][1]}% ({results[2][2]}) 
----------------------------------------
Winner:{winnerfinder(candidates)}
----------------------------------------''')
print(printingresults)

output_path = os.path.join("analysis", "analysis.txt")
with open(output_path, 'w') as textfile:
    textfile.write(printingresults)