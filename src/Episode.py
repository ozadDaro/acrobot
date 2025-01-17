
from DiscretizeState import DiscretizeState
from e_greedy_selection import e_greedy_selection
from AcrobotPlot import AcrobotPlot
from UpdateSARSA import UpdateSARSA
from GetReward import GetReward
from DoAction import *

def Episode( maxsteps, Q , alpha, gamma,epsilon,statelist,actionlist,grafic,fig ) :

	print "Episode"

	x            = [0, 0, 0, 0]
	steps        = 0
	total_reward = 0


	s   = DiscretizeState(x,statelist)
	a   = e_greedy_selection(Q,s,epsilon)


	for i in range(maxsteps )   :
	        
		action = actionlist[int(a)]  

		xp  = DoAction( action , x )  

		r,f   = GetReward(xp)
		total_reward = total_reward + r

		sp  = DiscretizeState(xp,statelist)

		ap = e_greedy_selection(Q,sp,epsilon)


		Q = UpdateSARSA( s, a, r, sp, ap, Q , alpha, gamma )


		s = sp
		a = ap
		x = xp


		steps=steps+1


		if (grafic==True):           
			AcrobotPlot(x,action,steps,fig)

		if (f==True):
			break
     
	AcrobotPlot(x,action,steps,fig)
	return total_reward,steps,Q
