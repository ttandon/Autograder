##this file creates rf models specifically for each SET. a bug was found in sets 3/4, so they were not included.
##its based on rfmodel.py, and replaced rfmodel.py in use in the system.

# Import the random forest package
from sklearn.ensemble import RandomForestClassifier
import re
import numpy
import array

def wordbag(SET, linenum, doctype, filetype):
	file = open("output/" +doctype+ "_" + str(SET) + "_"+filetype+".txt")
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
def feature_runner():
	train_data = [] ##full array
	train = [] ##no scores
	forestarray = [] ##array of random forests. 1 for each set
	##for each set
	for x in range(1, 11):
		if x == 3 or x == 4:
			continue
		print x
		file = open("output/training_" + str(x) + ".txt")
		linecount = 0
		while 1:
			line = file.readline()
			if not line:
				break
			##print line
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
			for f in freq:
				new.append(freq[f])
			bfreq = wordbag(x, linecount, "training", "b")
			for f in bfreq:
				new.append(bfreq[f])

			##new.append(freq)
			##for array without score
			new2.append(feat1)
			new2.append(feat2)
			new2.append(feat3)
			for f in freq:
				new2.append(f)
			for f in bfreq:
				new2.append(f)

			train_data.append(new)
			train.append(new2)
			linecount = linecount + 1
			score_array = []
		for row in train_data:
			for item in row:
				score_array.append(item)
				break
		Forest = RandomForestClassifier(n_estimators = 200)
		Forest = Forest.fit(train, score_array)
		forestarray.append(Forest)
		train = []
		train_data = []
	##numpy.array(train_data)
	finalpredictions = []
	first = []
	second = []
	test_data = [] ##full array
	id_array = []
	for x in range(1, 11):
		 ##each row of data in format [score, wordcount, sentencecount, averagesentsize]
		if x == 3 or x == 4:
			continue
		file = open("output/test_" + str(x) + ".txt")
		linecount = 0
		print x
		while 1:
			line = file.readline()
			if not line:
				break
			new = []
			id_array.append(line.split(" ")[0]) 
			feat1 = float(re.search(" 1:(\d+)", line).group(1))
			feat2 = float(re.search(" 2:(\d+)", line).group(1))
			feat3 = float(re.search(" 3:(\d+)", line).group(1))
			##feat4 = float(re.search(" 4:(\d+)", line).group(1))
			new.append(feat1)
			new.append(feat2)
			new.append(feat3)
			freq = wordbag(x, linecount, "test", "w")
			for f in freq:
				new.append(f)
			bfreq = wordbag(x, linecount, "test", "b")
			for f in bfreq:
				new.append(f)
			test_data.append(new)
			linecount = linecount+1
		predictions = []
		if x<5:
			predictions = forestarray[x-1].predict(test_data)
		elif x>2:
			predictions = forestarray[x-3].predict(test_data)
		##print str(len(predictions)) + "prediction length"
		print len(predictions)
		for prediction in predictions:
			finalpredictions.append(prediction)

		test_data = []
	# ofile ="predictions2.txt"
	# filew = open(ofile, "w")
	# for p in finalpredictions:
	# 	filew.write(str(int(round(p))) + "\n")

	##final ouput
	ofile = "model/predictions.csv"
	filek = open(ofile, "w")
	counter = 0
	filek.write("id,prediction")
	for i in id_array:
		filek.write(i + "," + str(int(round(finalpredictions[counter]))) + "\n")
		counter = counter + 1
	ofile = "model/predictions.txt"
	filetxt = open(ofile, "w")
	counter_txt = 0
	for i in id_array:
		filetxt.write(str(int(round(finalpredictions[counter_txt]))) + "\n")
		counter_txt = counter_txt + 1

	##old junk

	##numpy.array(test_data)	    

	# Create the random forest object which will include all the parameters
	# for the fit
	##Forest = RandomForestClassifier(n_estimators = 200)
	# Fit the training data to the training output and create the decision
	# trees
	##score_array = []
	##for row in train_data:
		##for item in row:
			##score_array.append(item)
			##break
	##Forest = Forest.fit(train, score_array)

	# Take the same decision trees and run on the test data
	##predictions = Forest.predict(test_data)

		


