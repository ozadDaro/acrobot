from math import cos, sin
import matplotlib.pyplot as plt

def AcrobotPlot( x,a,steps ):
	
	plt.subplot(2,1,2)

	theta1 = x[0]
	theta2 = x[1]


	x_acrobot[0] =0
	y_acrobot[0]=0

	x_acrobot[1] = x_acrobot[0] + sin(theta1) 
	y_acrobot[1] = y_acrobot[0] - cos(theta1)

	x_acrobot[2] = x_acrobot[1] + sin(theta2)
	y_acrobot[2] = y_acrobot[1] - cos(theta2) 

	plt.plot(x_acrobot ,y_acrobot,'ok-','LineWidth',1,'markersize',7,'MarkerFaceColor',[.7, .7, .7])
 	
 	plt.plot(x_acrobot[2],y_acrobot[2] ,'.r','markersize',20)

	plt.set_title(  'Step: '+str(steps))

	plt.axis([-2.1, 2.1, -2.1, 2.1])
	
	plt.show()
