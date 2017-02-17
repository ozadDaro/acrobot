def GetBestAction(Q,s):
	print s
	return max(Q[int(s),:])