"""
Prends en param les images, calcule matrice des scores

"""


from image import Image

import numpy as np


def scoring(S1, S2):
	return np.min([len(S1.tags & S2.tags), len(S1.tags - S2.tags), len(S2.tags - S1.tags)])



def score_matrix(list_images):
	n = len(list_images)
	matrix = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			matrix[i,j] = scoring(list_images[i], list_images[j])
	return matrix
# def create_matrix(list_images):

A = Image(set([0,1,2,3]), 'H', 3)
B = Image(set([1,2,3, 4,5]), 'H', 3)
C = Image(set([1,2,5, 10]), 'H',3)
D = Image(set([1,2,4,5]), 'H', 3)
E = Image(set([1,5]), 'H', 3)

list_images = [A,B,C,D,E]

print(score_matrix(list_images))


# print(scoring(A,B))


