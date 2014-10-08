import numpy as np 
from matplotlib import pyplot as plt

file = open("answers.txt")
numarray = []
while 1:
	line = file.readline()
	if not line:
		break
	numarray.append(float(line))
grapharray = [0, 1, 2, 3]
graphx = []
zerocount = 0
onecount = 0
twocount = 0
threecount = 0
for num in numarray:
	if num == 0:
		zerocount = zerocount + 1
	if num == 1:
		onecount = onecount + 1
	if num == 2:
		twocount = twocount + 1
	if num == 3:
		threecount = threecount + 1

grapharray.append(zerocount)
grapharray.append(onecount)
grapharray.append(twocount)
grapharray.append(threecount)
fig = plt.figure()

width = .35
ind = np.arange(len(grapharray))
plt.bar(ind, grapharray)
plt.xticks(ind + width / 2, graphx)

fig.autofmt_xdate()

plt.savefig("figurecorrect.pdf")


