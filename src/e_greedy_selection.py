import random 
from GetBestAction import GetBestAction

def e_greedy_selection(Q, s,epsilon):

	actions = size(Q,2);
	
	if (random.random()>epsilon) :
		a = GetBestAction(Q,s)   
	else:
	
		a = random.randint(1,1,actions)+1;
	return a
