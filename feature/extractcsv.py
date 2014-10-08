##this file opens the solutions to the public leaderboard and extracts just the scores into a separate file called answers.txt.
##which is then used in the estimateaccuracy.py to estimate the accuracy of the model.

import csv

scorearray = []	
cr = csv.reader(open("../dataset/raw/public_leaderboard_solution.csv","rb"))
linecounter = 0
for row in cr:
	if linecounter != 0 :
		if row[1] != "3" and row[1] != "4":      
			scorearray.append(row[3])
	linecounter = linecounter + 1
ofile ="answers.txt"
filew = open(ofile, "w")
for score in scorearray:
	filew.write(str(score) + " \n")