import copy
def UpdateSARSA(s, a, r, sp, ap, tab , alpha, gamma ):
	
	Q = copy.copy(tab)
	Q[int(s)][int(a)] =  Q[int(s)][int(a)] + alpha * ( r + gamma*Q[int(sp)][int(ap)] - Q[int(s)][int(a)])
	return Q
