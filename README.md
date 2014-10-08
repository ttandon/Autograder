Autograder
==========

A random forests based autograding system (based on LT-Autograder, Luis Tandalla's winning entry in the SAS kaggle competition)

Simply run runner.py to begin the entire process. The classifier will be trained in the datasets provided in dataset/raw. The provided test data from Kaggle will then be applied to generate a QWK (Quadratic Weighted Kappa) inter-rater agreement to determine the accuracy of the model. Score predictions are outputted into /model, and a QWK prediction is printed out at the end. 
