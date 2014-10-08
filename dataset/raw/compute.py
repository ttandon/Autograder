##this was an experimental file meant to count the number of lines in the public leaderboard. not important/used in model.

file = open("public_leaderboard_solution.tsv")
linecount = 0
while 1:
	line = file.readline()
	if not line:
		break
	linecount = linecount + 1
print linecount
