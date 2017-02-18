from math import cos, sin
import matplotlib.pyplot as plt

import numpy as np

def AcrobotPlot( x,a,steps ,fig):

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

	ax1.set_title(  'Step: '+str(steps))

	ax1.axis([-2.1, 2.1, -2.1, 2.1])
	
	plt.show(block=False)
	plt.pause(0.001)
	
	
	
