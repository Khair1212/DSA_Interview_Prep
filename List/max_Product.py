# Question - How to find the maximum product of two integers in the array where all elements are positive

import numpy as np
myArray = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])

max = 1

for i in range(len(myArray)):
    for j in range(i, len(myArray)):
        product = myArray[i]*myArray[j]
        if product > max:
            max = product
            pairs = str(myArray[i])+','+str(myArray[j])

print(max)