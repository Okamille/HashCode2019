"""
greedy

"""

import numpy as np

def greedy(matrix, init = 0):
	n= matrix.shape[0]
	max_score = 0
	L = []
	for i in range(n):
		index = np.argmax(matrix[init])
		if i != n-1:
			max_score += matrix[init,index]
		matrix[:,init]= np.array([-1]*n)
		matrix[init,:]= np.array([-1]*n)
		# np.delete(matrix, init, 1)
		# np.delete(matrix, init, 0)
		L+=[init]
		init = index

	return L, max_score


