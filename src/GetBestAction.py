import numpy as np

def GetBestAction(Q,s):
	print s
	print np.argmax(Q[int(s),:])
	return np.argmax(Q[int(s),:])