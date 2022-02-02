myList = [1, 2, 3, 4, 5, 6, 7]
#print(myList)
# mylist[2] = 33
# mylist[4] = 55
# print(mylist)

#myList.insert(4, 15)
#myList.append(55)
#print(myList)

newList = [11, 12, 13, 14]
myList.extend(newList)
#print(myList)

list = ['a', 'b', 'c', 'd', 'e', 'f'] #list is a built in function so dont use it like this!
#list[0:2] = ['x', 'y']
#print(list[:])

#print(list.pop())
#del list[2:4]


#list.remove('e')
#print(list)

# if 7 in myList:
#     print(myList.index(7))
# else:
#     print('Value does not exist in the list')


def searchinList(list, value):
    for i in myList:
        if i == value:
            return myList.index(value)
    return 'The Value does not exist in the list '

#print(searchinList(myList, 7))    

b = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
#a = a * 4
# print(len(a))
# print(max(a))
# print(min(a))
# print(sum(a)/len(a))
#print(a)

n = int(input('Enter no of elements'))
a =[] 
for x in range(0,n):
    a.append(int(input('Enter element')))

total = sum(a)
avg = total / n
print(avg)
