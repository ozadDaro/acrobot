# -*- coding: utf-8 -*-
import numpy as np


def BuildStateList() : 
	#BuildStateList retourn une liste d'états à partir d'une matrice d'états



	pi = np.pi

	x1   = np.linspace(-pi/2,pi/2,5)
	x2   = np.linspace(-pi/2,pi/2,5)
	x3   = np.linspace(-pi/4,pi/4,3)
	x4   = np.linspace(-pi/4,pi/4,3)

	I=x1.shape[0]
	J=x2.shape[0]
	K=x3.shape[0]
	L=x4.shape[0]

	print type(I)

	states= np.zeros((I*J*K*L, 4))
	index=0
	for i in range(I) :     
		for j in range(J) : 
			for k in range(K) : 
				for l in range(L) : 
					states[index,0]=x1[i]
					states[index,1]=x2[j]
					states[index,2]=x3[k]
					states[index,3]=x4[l]
					index=index+1
	return states

