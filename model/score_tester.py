import ml_metrics as metrics
file = open("predictions.txt")
numarray = []
while 1:
	line = file.readline()
	if not line:
		break
	numarray.append(int(float(line)))
file = open("answers.txt")
answerarray = []
while 1:
	line = file.readline()
	if not line:
		break
	answerarray.append(int(float(line)))
##print len(numarray)
##print len(answerarray)
solutionarray = []
for x in range(0, len(numarray)):
	if numarray[x] == answerarray[x]:
		solutionarray.append(1)
	else:
		solutionarray.append(0)
onecounter = solutionarray.count(1)
print "QWK_Score: " + str(metrics.quadratic_weighted_kappa(answerarray,numarray))
