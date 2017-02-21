# -*- coding: utf-8 -*-
import numpy as np
from math import pi, cos, sin
import matplotlib.pyplot as plt
from sklearn.metrics import pairwise_distances_argmin_min











def CreerListeEtats() : 
	#BuildStateList retourn une liste d'etats à partir d'une matrice d'états


	pi = np.pi

	x1   = np.linspace(-pi/2,pi/2,5)
	x2   = np.linspace(-pi/2,pi/2,5)
	x3   = np.linspace(-pi/4,pi/4,3)
	x4   = np.linspace(-pi/4,pi/4,3)


	etats= np.zeros((x1.shape[0]*x2.shape[0]*x3.shape[0]*x4.shape[0], 4))
	index=0
	for i in range(x1.shape[0]) :     
		for j in range(x2.shape[0]) : 
			for k in range(x3.shape[0]) : 
				for l in range(x4.shape[0]) : 
					etats[index,0]=x1[i]
					etats[index,1]=x2[j]
					etats[index,2]=x3[k]
					etats[index,3]=x4[l]
					index=index+1
	return etats

def Discretisation(x, listeEtats):

	
	s = pairwise_distances_argmin_min( x,listeEtats, axis=1, metric='euclidean')
	
	s = s[0][0] 
	

	return s
	
def epsilon_greedy(Q, etat,epsilon):
	actions = Q.shape[1]	
	if (np.random.rand(1,1)[0]>epsilon) :
		return np.argmax(Q[int(etat),:])
		
	return np.random.randint(low=0,high=actions)

	
def Actionner(torque,x):
 	
	vitesseMax1 = 4*pi
	vitesseMax2 = 9*pi 
	m1        = 1
	m2        = 1 
	l1        = 1 
	l2        = 1 

	lc1       = 0.5
	lc2       = 0.5 

	I1        = 1
	I2        = 1 
	g         = 9.8 
	delta_t   = 0.05

	theta1        = x[0]
	theta2        = x[1]
	theta1_dot    = x[2]
	theta2_dot    = x[3]
	
	d1     = m1*lc1*lc1  + m2*(l1*l1  + lc2*lc2  + 2*l1*lc2 * cos(theta2)) + I1 + I2
	d2     = m2*(lc2*lc2+l1*lc2*cos(theta2)) + I2

	phi2   = m2*lc2*g*cos(theta1+theta2-pi/2)
	phi1   = -m2*l1*lc2*theta2_dot*sin(theta2)*(theta2_dot-2*theta1_dot)+(m1*lc1+m2*l1)*g*cos(theta1-(pi/2))+phi2

	accel2 = (torque+phi1*(d2/d1)-m2*l1*lc2*theta1_dot*theta1_dot*sin(theta2)-phi2)
	accel2 = accel2/(m2*lc2*lc2+I2-(d2*d2/d1))
	accel1 = -(d2*accel2+phi1)/d1


	for i in range(4):
		theta1_dot = theta1_dot + accel1*delta_t

		

		if(theta1_dot<-vitesseMax1):
			
			theta1_dot=-vitesseMax1

                 
		if(theta1_dot>vitesseMax1):
			theta1_dot=vitesseMax1
        
		theta1     =  theta1 + theta1_dot*delta_t
		theta2_dot =  theta2_dot + accel2*delta_t


		if(theta2_dot<-vitesseMax2):
        	
			theta2_dot=-vitesseMax2
			

		
		


		if(theta2_dot>vitesseMax2):
			theta2_dot=vitesseMax2

		theta2 = theta2 + theta2_dot*delta_t; 
		

	if(theta1<-pi):
		theta1 = -pi 
	
	if(theta1>pi):
		theta1 = pi 
	   
	if(theta2<-pi):
		theta2 = -pi 
	
	if(theta2>pi):
		theta2 = pi 
	

	xp = []
	xp.append(theta1)
	xp.append(theta2)
	xp.append(theta1_dot)
	xp.append(theta2_dot)
	return xp


	
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
	

def AcrobotPlot( x,a,etapes ,fig):

	#plt.clf()
	
	ax1 = fig.add_subplot(212) 
	ax1.clear()	
	#plt.subplot(212)
	theta1 = x[0]
	theta2 = x[1]
	
	x_acrobot = np.zeros(3)
	y_acrobot = np.zeros(3)
	
	x_acrobot[0] =0
	y_acrobot[0]=0

	x_acrobot[1] = x_acrobot[0] + sin(theta1) 
	y_acrobot[1] = y_acrobot[0] - cos(theta1)

	x_acrobot[2] = x_acrobot[1] + sin(theta2)
	y_acrobot[2] = y_acrobot[1] - cos(theta2) 

	ax1.plot(x_acrobot ,y_acrobot,'ok-',linewidth = 1,markersize=7,markerfacecolor=[.7, .7, .7])
 	
 	ax1.plot(x_acrobot[2],y_acrobot[2] ,'.r',markersize=20)

	ax1.set_title(  'Etape: '+str(etapes))

	ax1.axis([-2.1, 2.1, -2.1, 2.1])
	
	plt.show(block=False)
	plt.pause(0.001)
	

def nouvelEpisodeSarsa( nbEtapes, Q , alpha, gamma,epsilon,listeEtats,listeActions, lamb, e, afficherAcrobot,fig ) :


	x            = [0, 0, 0, 0]
	etapes       = 0
	rewardTotal = 0
	
	visites = [1]*len(listeEtats)


	etat   = Discretisation(x,listeEtats)
	a   = epsilon_greedy(Q,etat,epsilon)


	for i in range(nbEtapes )   :
	
		#alpha = 1.0/visites[a]
		visites[a]+=1
	        
		action = listeActions[int(a)]  

		xp  = Actionner( action , x )  

		r,f   = GetReward(xp)
		rewardTotal = rewardTotal+ r

		sp  = Discretisation(xp,listeEtats)

		ap = epsilon_greedy(Q,sp,epsilon)
		
		delta = r + gamma*Q[sp][ap]-Q[etat][a]
		
		e[etat][a]+=1
		
		for s in range(len(listeEtats)) : 
			for a in range(len(listeActions)) : 
				Q[s][a]+=alpha*delta*e[s][a]
				e[s][a]*=gamma*lamb



		etat = sp
		a = ap
		x = xp


		etapes=etapes+1


		if (afficherAcrobot==True):           
			AcrobotPlot(x,action,etapes,fig)

		if (f==True):
			break
     
	AcrobotPlot(x,action,etapes,fig)
	return rewardTotal,etapes,Q
	

def nouvelEpisodeQ( nbEtapes, Q , alpha, gamma,epsilon,listeEtats,listeActions, lamb, e, afficherAcrobot,fig ) :


	x            = [0, 0, 0, 0]
	etapes       = 0
	rewardTotal = 0
	
	visites = [1]*len(listeEtats)


	etat   = Discretisation(x,listeEtats)
	a   = epsilon_greedy(Q,etat,epsilon)


	for i in range(nbEtapes )   :
	
		#alpha = 1.0/visites[a]
		#visites[a]+=1
	        
		action = listeActions[int(a)]  

		xp  = Actionner( action , x )  

		r,f   = GetReward(xp)
		rewardTotal = rewardTotal+ r

		sp  = Discretisation(xp,listeEtats)

		#ap = epsilon_greedy(Q,sp,epsilon)
		ap = np.argmax(Q[sp,:])
		delta = r + gamma*Q[sp][ap]-Q[etat][a]
		
		e[etat][a]+=1
		
		for s in range(len(listeEtats)) : 
			for a in range(len(listeActions)) : 
				Q[s][a]+=alpha*delta*e[s][a]
				e[s][a]*=gamma*lamb



		etat = sp
		a = ap
		x = xp


		etapes=etapes+1


		if (afficherAcrobot==True):           
			AcrobotPlot(x,action,etapes,fig)

		if (f==True):
			break
     
	AcrobotPlot(x,action,etapes,fig)
	return rewardTotal,etapes,Q

	

def AcrobotDemo(nbEpisodes) : 

	
	
	fig = plt.figure()
	ax1 = fig.add_subplot(211) 

	nbEtapes   = 1000;              #nombre maximal dtapes par épisode
	listeEtats   = CreerListeEtats();  #Liste d'états
	listeActions  = [-1.0 , 0.0 , 1.0]; #Liste d'actions


	Q=np.zeros((len(listeEtats),len(listeActions)))
	e = np.zeros((len(listeEtats),len(listeActions)))

	alpha       = 0.5;    # learning rate
	gamma       = 1.0;    # discount factor
	epsilon     = 0.9;   # 
	lamb = 0.3
	afficherAcrobot     = False;  # indique si on fait appel à l'inteface graphique

	xpoints=[];
	ypoints=[];

	for i in range(nbEpisodes) : 
		total_reward,etapes,Q  = nouvelEpisodeSarsa( nbEtapes, Q , alpha, gamma,epsilon,listeEtats,listeActions,lamb, e, afficherAcrobot, fig )
		#total_reward,etapes,Q  = nouvelEpisode( nbEtapes, Q , alpha, gamma,epsilon,listeEtats,listeActions,afficherAcrobot, fig );
		print 'Espisode: ',str(i),'  Etapes:',str(etapes),'  Reward:',str(total_reward),' epsilon: ',str(epsilon)   
		
		#On décroit epsilon
		epsilon = epsilon * 0.95;

		xpoints.append(i);
		ypoints.append(etapes);
		#graph de la learning curve
		
		  
		ax1.plot(xpoints,ypoints)      
		ax1.set_title('Episode: '+str(i)+' epsilon: '+str(epsilon))
		plt.pause(0.0001)





AcrobotDemo(200);