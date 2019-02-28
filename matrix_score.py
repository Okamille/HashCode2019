"""
Prends en param les images, calcule matrice des scores

"""


from image import Image
from greedy import *

import numpy as np
from scipy.sparse import dok_matrix

from joblib import Parallel, delayed

def scoring(S1, S2):
	# print(S2.tags & S1.tags)
	return np.min([len(S1.tags & S2.tags), len(S1.tags - S2.tags), len(S2.tags - S1.tags)])



def matrix_score(list_images):
	n = len(list_images)
	print(n)
	matrix = np.zeros((n,n)) #dok_matrix((n,n))
	for i in range(n):
		if i%100 == 0:
			print(i)
		for j in range(0,i):
			if i==j:
				matrix[i,j] = -1
			else:
				matrix[i,j] = scoring(list_images[i], list_images[j])
	return matrix + np.transpose(matrix)


def par_matrix_score(list_images, batch):
	inf = 2000*i
	sup = 2000*(i+1)
	n = len(list_images)
	print(n)
	matrix = np.zeros((2000,n)) #dok_matrix((n,n))
	for i in range(inf, sup):
		if i%100 == 0:
			print(i)
		for j in range(i,n):
			if i==j:
				matrix[i,j] = -1
			else:
				matrix[i,j] = scoring(list_images[i], list_images[j])
	return matrix



# def create_matrix(list_images):

# A = Image(set([0,1,2,3]), 'H', 3)
# B = Image(set([1,2,3, 4,5]), 'H', 3)
# C = Image(set([1,2,5, 10]), 'H',3)
# D = Image(set([1,2,4,5]), 'H', 3)
# E = Image(set([1,5]), 'H', 3)

# list_images = [A,B,C,D,E]

# print(matrix_score(list_images))
# print(np.argmax(matrix_score(list_images)))


# # print(scoring(A,B))
# for i in range(len(list_images)):
# 	print(greedy(matrix_score(list_images),i))