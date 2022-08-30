# Question 1 - Missing Number

from array import *

arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]
n = 10
expected_sum = 10*(10+1)/2
received_sum = sum(arr)

value = expected_sum-received_sum
print(int(value))

# Question Rotate MAtrix (Medium)
import numpy as np

myArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(myArray)
def rotateMatrix(matrix):
    n = len(matrix)

    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # save top elemenet
            top = matrix[layer][i]

            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]

            # move bottom to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]

            # move right to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]

            # move top to right
            matrix[i][-layer-1] = top
    return matrix

print(rotateMatrix(myArray))