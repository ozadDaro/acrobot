
import numpy as np
from edist import edist
def DiscretizeState(x, statelist):

	x = np.matlib.repmat(x,size(statelist,1),1)
	s = min(edist(statelist,x))
	return s