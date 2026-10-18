import numpy as np

array = np.array([
    [['A', 'B', 'C'],     # page 0
     ['D', 'E', 'F']],

    [['G', 'H', 'I'],     # page 1
     ['J', 'K', 'L']]
])

word = array [0,0,0]+array[0,1,2]+array[1,1,1]
print(word)