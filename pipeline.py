"""
load file

"""


import loader
from matrix_score import *
from greedy import *

path_b = "/mnt/d/hashcode_2019/HashCode2019/b_lovely_landscapes.txt"
path_c = "/mnt/d/hashcode_2019/HashCode2019/c_memorable_moments.txt"
path_d = "/mnt/d/hashcode_2019/HashCode2019/d_pet_pictures.txt"
path_e = "/mnt/d/hashcode_2019/HashCode2019/e_shiny_selfies.txt"

# print(loader.load_file(path))

images = loader.load_file(path_e) # + loader.load_file(path_c) #+ loader.load_file(path_d) + loader.load_file(path_e)

images = images[:10000]

matrix = matrix_score(images)

index = matrix.argmax(axis=0).argmax(axis=0)
# print(index)
# print(greedy(matrix, index))


a = Parallel(n_jobs = -1)(delayed(par_matrix_score)(list_images, i) for i in range(5))
print(a)


# print(np.sum(matrix_score(images)[1]))