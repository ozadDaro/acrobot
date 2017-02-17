# -*- coding: utf-8 -*-
from BuildQTable import * 
from BuildStateList import * 
from BuildActionList import * 
from Episode import *
import matplotlib.pyplot as plt

def AcrobotDemo(maxepisodes) : 

	maxsteps    = 1000;              #nombre maximal dtapes par épisode
	statelist   = BuildStateList();  #Liste d'états
	actionlist  = BuildActionList(); #Liste d'actions

	nstates     = len(statelist);
	nactions    = len(actionlist);
	Q           = BuildQTable(nstates,nactions);  # Qtable

	alpha       = 0.5;    # learning rate
	gamma       = 1.0;    # discount factor
	epsilon     = 0.01;   # 
	grafica     = True;  # indique si on fait appel à l'inteface graphique

	xpoints=[];
	ypoints=[];

	for i in range(maxepisodes) : 
		
		total_reward,steps,Q  = Episode( maxsteps, Q , alpha, gamma,epsilon,statelist,actionlist,grafica );
		print 'Espisode: ',int2str(i),'  Steps:',int2str(steps),'  Reward:',num2str(total_reward),' epsilon: ',num2str(epsilon)   
		
		#On décroit epsilon
		epsilon = epsilon * 0.99;
		
		xpoints[i]=i;
		ypoints[i]=steps;
		#graph de la learning curve
		fig = plt.figure()
		ax1 = fig.add_subplot(221)   
		ax1.plot(xpoints,ypoints)      
		ax.set_title('Episode: '+str(i)+' epsilon: '+str(epsilon))
		
		if (i>1000) : 
			grafica=True

