import numpy as np 
from matplotlib import pyplot as plt
import pylab

file = open("predictions.txt")
numarray = []
while 1:
	line = file.readline()
	if not line:
		break
	numarray.append(float(line))

x = range(len(numarray))
plt.scatter(x,numarray)

plt.savefig("figure.pdf")


