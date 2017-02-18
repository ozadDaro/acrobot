
import numpy as np
from numpy.matlib import repmat
from edist import edist
import sklearn
from sklearn.metrics import pairwise_distances_argmin_min
def DiscretizeState(x, statelist):

	

	
	#x = repmat(x,statelist.shape[0],1)
	#print "size x"
	#print x
	#print x.shape
	#s = min(edist(statelist,x))
	
	s = sklearn.metrics.pairwise_distances_argmin_min( x,statelist, axis=1, metric='euclidean')
	
	s = s[0][0] 
	

	return s