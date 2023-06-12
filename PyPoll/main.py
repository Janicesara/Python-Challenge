# Importing the modules required
import os
import csv

#seting up  path
csv_path=os.path.join('Resources','election_data.csv')

#variables
total_votes_required=0
candidate_votes_count={}

#reading csv file
with open(csv_path,'r') as csvfile:

    #csv reader  delimiter
    csv_reader=csv.reader(csvfile,delimiter=',')

    #header
    csv_header=next(csv_reader)

    #looping
    for row in csv_reader:
        
        #total votes required
        total_votes_required+=1

        # candidates, candidate votes in dic
        if row[2] not in candidate_votes_count:
            candidate_votes_count[row[2]]=1
        else:
            candidate_votes_count[row[2]]+=1

#printing the total vote results
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_votes_required}")
print("------------------------")

#candidate name, percentage of votes, vote count
for candidate,votes in candidate_votes_count.items():
        print(candidate+": "+"{:.3%}".format(votes/total_votes_required)+"  ("+str(votes)+")")

# winner by popular vote
winner=max(candidate_votes_count,key=candidate_votes_count.get)
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")


#text file summary written
txtpath=os.path.join('pypoll.txt')
txtfile=open(txtpath,'w')
txtfile.write("Election Results\n")
txtfile.write("------------------------\n")
txtfile.write(f"Total Votes: {total_votes_required}\n")
txtfile.write("------------------------\n")

for candidate,votes in candidate_votes_count.items():
        txtfile.write(candidate+": "+"{:.3%}".format(votes/total_votes_required)+"  ("+str(votes)+")\n")
        
txtfile.write("------------------------\n")
txtfile.write(f"Winner: {winner}\n")
txtfile.write("------------------------")

txtfile.close()