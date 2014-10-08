import sys
sys.path.append('pythonScripts')

from pr1 import process1
from pr2 import process2
from pr3 import process3

nameTrainingOut1 = 'dataset/raw/train_rel_2_2.tsv'
nameTrainingOut2 = 'train_rel_2_3.tsv'
nameTestIn = 'dataset/raw/test.tsv'
nameTestOut1 = 'AdditionalFiles/test_2.tsv'
nameTestOut2 = 'AdditionalFiles/test_3.tsv'


##removed to optimize processing time:
##process1( nameTestIn, nameTestOut1, test = True)  #correcting mispelled words SPELL CORRECTOR loaded on test file
##print 'Stemming'
##process2( nameTrainingOut1, nameTrainingOut2 ) #PORTER STEMMER algorithm loaded on training file
##process2( nameTestIn, nameTestOut2 ) #run on test (output from spell corrector)

def start_process():
	print 'Calculating Features'
	for SET in range(1,11):
	 process3( SET, True, nameTrainingOut1, nameTestIn)
