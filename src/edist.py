from math import sqrt
import numpy as np
def edist(X,Y):
	return np.sqrt(np.sum( (xi - yi)**2 for xi, yi in zip(X, Y)))


 