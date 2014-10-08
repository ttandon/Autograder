##this was the original rf model file, and it generates one rf model for the entire training data. it was replaced by rf2.py, and is not used
##in the final model.

# Import the random forest package
from sklearn.ensemble import RandomForestClassifier
import re
import numpy
import array

def wordbag(SET, linenum, doctype, filetype):
	file = open("../output/" +doctype+ "_" + str(SET) + "_"+filetype+".txt")
	# Read in the file once and build a list of line offsets
	line_offset = []
	offset = 0
	for line in file:
	    line_offset.append(offset)
	    offset += len(line)
	file.seek(0)

	# Now, to skip to line n (with the first line being line 0), just do
	file.seek(line_offset[linenum])
	bag = file.readline()
	mylist = bag.split(" ")
	mylist.pop(0)
	freq = []
	for pair in mylist:
		freq.append(int(float(pair.split(":")[1])))
	return freq

train_data = [] ##full array
train = [] ##no scores
for x in range(1, 11):
	print x
	 ##each row of data in format [score, wordcount, sentencecount, averagesentsize]
	file = open("../output/training_" + str(x) + ".txt")
	linecount = 0
	while 1:
		line = file.readline()
		if not line:
			break
		new = []
		new2 = []
		line = line.replace("  ", " ", 1)
		score = float(re.search("s1:(\d+)", line).group(1))
		feat1 = float(re.search(" 1:(\d+)", line).group(1))
		feat2 = float(re.search(" 2:(\d+)", line).group(1))
		feat3 = float(re.search(" 3:(\d+)", line).group(1))
		feat4 = float(re.search(" 4:(\d+)", line).group(1))

		##array with score
		new.append(score)
		new.append(feat1)
		new.append(feat2)
		new.append(feat3)
		freq = wordbag(x, linecount, "training", "w")
		for b in xrange(0, 300):
			new.append(freq[b])
		bfreq = wordbag(x, linecount, "training", "b")
		for b in xrange(0, 100):
			new.append(bfreq[b])
		##new.append(freq)
		##for array without score
		new2.append(feat1)
		new2.append(feat2)
		new2.append(feat3)
		for b in xrange(0, 300):
			new2.append(freq[b])
		##new2.append(freq)
		for b in xrange(0, 100):
			new2.append(bfreq[b])

		train_data.append(new)
		train.append(new2)
		linecount = linecount + 1
##numpy.array(train_data)

test_data = [] ##full array
for x in range(1, 11):
	 ##each row of data in format [score, wordcount, sentencecount, averagesentsize]
	file = open("../output/test_" + str(x) + ".txt")
	linecount = 0
	while 1:
		line = file.readline()
		if not line:
			break
		new = []
		feat1 = float(re.search(" 1:(\d+)", line).group(1))
		feat2 = float(re.search(" 2:(\d+)", line).group(1))
		feat3 = float(re.search(" 3:(\d+)", line).group(1))
		feat4 = float(re.search(" 4:(\d+)", line).group(1))
		new.append(feat1)
		new.append(feat2)
		new.append(feat3)
		freq = wordbag(x, linecount, "test", "w")
		for b in xrange(0, 300):
			new.append(freq[b])
		bfreq = wordbag(x, linecount, "test", "b")
		for b in xrange(0, 100):
			new.append(bfreq[b])
		##new.append(freq)
		test_data.append(new)
		linecount = linecount+1
##numpy.array(test_data)	    

# Create the random forest object which will include all the parameters
# for the fit
Forest = RandomForestClassifier(n_estimators = 200)
# Fit the training data to the training output and create the decision
# trees
score_array = []
for row in train_data:
	for item in row:
		score_array.append(item)
		break
Forest = Forest.fit(train, score_array)

# Take the same decision trees and run on the test data
predictions = Forest.predict(test_data)
ofile ="predictions.txt"
filew = open(ofile, "w")
for prediction in predictions:
	filew.write(str(int(round(prediction))) + "\n")
	


