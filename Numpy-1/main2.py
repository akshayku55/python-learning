import numpy as np

array = np.array([1,2,3])
print(array.ndim) # 1 dimensional array

array = np.array('A')
print(array.ndim) # 0 dimensional array

array = np.array([[1,2,3],[4,6,7]]) 
print(array.ndim) # 2 dimensioanl array
# print(array.shape)
print(array[0][0]) # chain indexing
#should be consistent elements in np array 

print(array[0,1]) # multidimensional indexing -> faster than chan indexinf