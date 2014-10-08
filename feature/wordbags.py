import re
import numpy
import array

def wordbag(SET, linenum):
	file = open("../output/training_" + str(SET) + "_w.txt")
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
print len(wordbag(2, 9))