# -*- coding: utf-8 -*-
from BuildQTable import * 
from BuildStateList import * 
from BuildActionList import * 
from Episode import *
import matplotlib.pyplot as plt

def AcrobotDemo(maxepisodes) : 

	fig = plt.figure()
	ax1 = fig.add_subplot(211) 

	maxsteps    = 1000;              #nombre maximal dtapes par épisode
	statelist   = BuildStateList();  #Liste d'états
	actionlist  = BuildActionList(); #Liste d'actions

	nstates     = len(statelist);
	nactions    = len(actionlist);
	Q           = BuildQTable(nstates,nactions);  # Qtable

	alpha       = 0.5;    # learning rate
	gamma       = 1.0;    # discount factor
	epsilon     = 0.01;   # 
	grafica     = False;  # indique si on fait appel à l'inteface graphique

	xpoints=[];
	ypoints=[];

	for i in range(maxepisodes) : 
		
		total_reward,steps,Q  = Episode( maxsteps, Q , alpha, gamma,epsilon,statelist,actionlist,grafica, fig );
		print 'Espisode: ',str(i),'  Steps:',str(steps),'  Reward:',str(total_reward),' epsilon: ',str(epsilon)   
		
		#On décroit epsilon
		epsilon = epsilon * 0.99;
		
		xpoints.append(i);
		ypoints.append(steps);
		#graph de la learning curve
		
		  
		ax1.plot(xpoints,ypoints)      
		ax1.set_title('Episode: '+str(i)+' epsilon: '+str(epsilon))
		plt.pause(1)
		if (i>1000) : 
			grafica=True

