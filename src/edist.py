import math as sqrt
def edist(X,Y):
	return sqrt(sum( (xi - yi)**2 for xi, yi in zip(x, y)))

 