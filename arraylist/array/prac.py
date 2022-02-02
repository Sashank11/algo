from array import *

arr = array('i', [1, 2, 3, 4, 5])

for i in arr:
    print(i)

print("Step 2")
print(arr[0])

print("Step 3")

arr.append(6)
print(arr)

print("Step 4")
arr.insert(3, 25)
print(arr)

print("Step 5")

arr2 = array('i', [10, 11, 12])

arr.extend(arr2)

print(arr)

print("Step 6")

templist = [40, 41, 42,]
arr.fromlist(templist)
print(arr)

print("Step 7")

arr.remove(42)
print(arr)

print("Step 8")

arr.pop()
print(arr)

print("Step 9")

print(arr.index(5))

print("Step 10")
arr.reverse()
print(arr)


print("Step 11")
print(arr.buffer_info())



print("Step 12")
arr.append(3)
print(arr.count(3))

print("Step 13")
#tempstr = arr.tostring()  #doesnot work after python 3.2
#print(tempstr)

print("Step 14")

print(arr.tolist())

#slice

print(arr[0:3])






