import random 
from GetBestAction import GetBestAction
import numpy as np

def e_greedy_selection(Q, s,epsilon):

	actions = Q.shape[1];
	print actions
	
	if (random.random()>epsilon) :
		a = GetBestAction(Q,s)   
	else:
	
		a = np.random.randint(low=0,high=actions);
	return a
