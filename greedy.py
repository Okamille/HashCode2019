"""
greedy

"""

import numpy as np

def greedy(matrix, init = 0):
	n= matrix.shape[0]
	max_score = 0
	L = []
	L_set = set()
	for i in range(n):
		if i%100 == 0:
			print(i)
		index = np.argmax(matrix[init])

		if i != n-1:
			max_score += matrix[init,index]


		matrix[:,init]= np.array([-1]*n)
		matrix[init,:]= np.array([-1]*n)
		L+=[init]
		L_set.add(init)
		init = index

	return L, max_score


