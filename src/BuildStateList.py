import numpy as np


def BuildStateList()
	#BuildStateList retourn une liste d'états à partir d'une matrice d'états





	x1   = np.linspace(-pi/2,pi/2,5)
	x2   = np.linspace(-pi/2,pi/2,5)
	x3   = np.linspace(-pi/4,pi/4,3)
	x4   = np.linspace(-pi/4,pi/4,3)

	I=x1.size(1)
	J=x2.size(1)
	K=x3.size(1)
	L=x4.size(1)



	states= np.zeros(I*J*K*L, 4)
	index=0
	for i=1:I    
		for j=1:J
			for k=1:K
				for l=1:L
					states[index,1]=x1[i]
					states[index,2]=x2[j]
					states[index,3]=x3[k]
					states[index,4]=x4[l]
					index=index+1

