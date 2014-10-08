import sys
sys.path.append('feature')
from preProcessData import start_process
start_process()
from rf2 import feature_runner
feature_runner()
sys.path.remove('feature')
sys.path.append('model')
from estimateaccuracy import predict_score
predict_score()
