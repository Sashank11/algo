import numpy as np

arr = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 1, 9]])
print(arr)

#newarr = np.insert(arr, 0, [[1, 2, 3, 4]], axis=0)
#print(newarr)

#newarr = np.append(arr, [[1, 2, 3, 4]],  axis=0)
#print(newarr)

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Invalid index')
    else:
        print(array[rowIndex, colIndex])

#accessElements(arr,2, 3 )

def traverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

#traverse(arr)

def search(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'Value found at index ' + str(i) + " " + str(j)
    
    return 'Element not found'


#print(search(arr, 35))

newarr = np.delete(arr, 0, axis = 1)
print(newarr)

