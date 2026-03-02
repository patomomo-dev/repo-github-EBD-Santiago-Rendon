import numpy as np
import random

row = np.array(100000)
column = np.array(100000)

matrix = row * column
print(matrix)


for i in range(99999):
    for j in range(99999):
        row[i] = random.randint(0,1)
        column[j] = random.randint(0,1)

