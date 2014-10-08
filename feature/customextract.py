##this was an experimental file to test a bug. not used/important for model.

import csv

scorearray = []	
cr = csv.reader(open("../dataset/raw/public_leaderboard_solution.csv","rb"))
linecounter = 0
for row in cr:
	if linecounter != 0:
		if row[1] != "3" and row[1] != "4":   
			scorearray.append(row)
	linecounter = linecounter + 1
ofile ="answers.txt"
filew = open(ofile, "w")
for score in scorearray:
	filew.write(str(score) + " \n")