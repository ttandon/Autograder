import enchant
import re
pretext = "The procedures I think they should have included inorder for me to replicate the experiment would be how different samples did they used for each? What tool did they use to determine the mass."

d = enchant.Dict("en_US")
wordList = re.sub("[^\w]", " ",  pretext).split()
errorcounter = 0
for word in wordList:
	if d.check(word) != True :
		print word
		errorcounter = errorcounter+1
print errorcounter