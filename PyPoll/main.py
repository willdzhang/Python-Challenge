import os
import csv

pollcsv = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')

# Open and read csv
with open(pollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    print("Election Results")
    print("--------------------")

    #candidate votes (Khan, Correy, Li, O'Tooley)
    voteTotal = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    for row in csvreader:
        voteTotal += 1
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1

    khanPercent = (khan / voteTotal) * 100
    correyPercent = (correy / voteTotal) * 100
    liPercent = (li / voteTotal) * 100
    otooleyPercent = (otooley / voteTotal) * 100
    
    print(f'Total votes: {voteTotal}')
    print("--------------------")
    print(f'Khan: {round(khanPercent, 3)}% {khan}')
    print(f'Correy: {round(correyPercent,3)}% {correy}')
    print(f'Li: {round(liPercent,3)}% {li}')
    print(f'O\'Tooley: {round(otooleyPercent,3)}% {otooley}')
    print("--------------------")
    
    if khan > correy and khan > li and khan > otooley:
        winner = "Khan"
    elif correy > khan and correy > li and correy > otooley:
        winner = "Correy"
    elif li > correy and li > khan and li > otooley:
        winner = "Li"
    else:
        winner = "O'Tooley"
    print(f'Winner: {winner}')
    print("--------------------")

    #write to text file
    file = open("polldata.txt","w+")
    file.write(f'Total votes: {voteTotal}\n') 
    file.write("--------------------\n") 
    file.write(f'Khan: {round(khanPercent, 3)}% {khan}\n') 
    file.write(f'Correy: {round(correyPercent,3)}% {correy}\n') 
    file.write(f'Li: {round(liPercent,3)}% {li}\n') 
    file.write(f'O\'Tooley: {round(otooleyPercent,3)}% {otooley}\n')
    file.write("--------------------\n")
    file.write(f'Winner: {winner}\n')
    file.write("--------------------")
    file.close()