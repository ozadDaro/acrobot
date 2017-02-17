import numpy as np

def GetReward(x) : 

	y_acrobot= []

	theta1 = x[0]
	theta2 = x[1]
	y_acrobot.append(0)
	y_acrobot.append(y_acrobot[0] - np.cos(theta1))
	y_acrobot.append(y_acrobot[1] - np.cos(theta2))  

	goal = y_acrobot[0] + 1.0 

	r = -1
	f = False

	if( y_acrobot[2] >= goal):
		r = 100 
		f = True


	return r,f
	
	
