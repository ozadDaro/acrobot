
import numpy as np
from numpy.matlib import repmat
from edist import edist
def DiscretizeState(x, statelist):

	x = repmat(x,statelist.size,1)
	s = min(edist(statelist,x))
	return s