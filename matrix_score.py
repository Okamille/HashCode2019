"""
Prends en param les images, calcule matrice des scores

"""


from image import Image

import numpy as np


def scoring(S1, S2):
	return np.min([len(S1.tags & S2.tags), len(S1.tags - S2.tags), len(S1.tags - S2.tags)])


# def create_matrix(list_images):

A = Image(set([0,1,2,3]), 'H')
B = Image(set([1,2,3, 4,5]), 'H')


print(scoring(A,B))