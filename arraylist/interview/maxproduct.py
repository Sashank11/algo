import numpy as np

myArray = np.array([1, 20, 30, 44, 5, 56, 57, 8,  9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])


def maxProduct(array):
    current = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if  array[i] * array[j] > current:
                current = array[i] * array[j]
                pairs = str(array[i]) + ", " + str(array[j])
    
    print(pairs)
    print(current)
maxProduct(myArray)