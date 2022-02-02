from array import *

arr = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.34, 2.67, 3.45])


# print(arr)


# def traverseArray(array):
#     for i in array:
#         print(i)


# traverseArray(arr)

def accessElement(array, index):
    if index >= len(array):
        print('Invalid index for the array')
    else:
        print(array[index])

def searchInArray(array, value):
    for i in array:
        if i  == value:
            return array.index(value)
    
    return "The element doesnot exist in the array"

# print(searchInArray(arr, 9))

#arr.remove(4)
print(arr)

