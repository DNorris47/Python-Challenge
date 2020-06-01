'''
In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

You will be given a set of poll data called election_data.csv. 
'''
import os
import csv

final_text = ""
final_text += ("Election Results\n-------------------------")

file_path = os.path.join ('Resources', "election_data.csv")
#create list
#print("\n-------------------------")
Candidate_List = []
Candidate_Vote ={}
i = 0
total_votes=0
Candidate_Percentage = {}


with open(file_path) as fp:
    my_reader = csv.reader(fp)
    for row in my_reader:
        #The first row of data is a header
        #Skip it
        if i == 0:
            i += 1
            continue
        
        Candidate_Name=row[2] 
        if Candidate_Name not in Candidate_List:
            Candidate_List.append(Candidate_Name)
            Candidate_Vote[Candidate_Name]=0
        Candidate_Vote[Candidate_Name]+=1

        total_votes +=1

final_text += ("\nTotal Votes: " + str(total_votes))
final_text += ("\n-------------------------")



for key in Candidate_Vote:
  final_text += ("\n{}: {:.3f}% ({})".format(key,(Candidate_Vote[key]/total_votes)* 100, Candidate_Vote[key]))

final_text += ("\n-------------------------")      

final_text += ("\nWinner: " + str(max(Candidate_Vote,key = Candidate_Vote.get)))
final_text += ("\n-------------------------") 

print(final_text)


file_path = os.path.join('analysis','results.txt')
#print(file_path)
with open(file_path,'w') as fp:
    fp.write(final_text)




'''
The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

*DONE-The total number of votes cast
*DONE-A complete list of candidates who received votes
*The percentage of votes each candidate won
*DONE-The total number of votes each candidate won
*DONE-The winner of the election based on popular vote.

As an example, your analysis should look similar to the one below:

Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------

In addition, your final script should both print the analysis to the terminal and export a text file with the results.


Write one script for each dataset provided. Run your script separately to make sure that the code works for its respective dataset.


'''

