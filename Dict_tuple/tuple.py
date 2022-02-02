newTuple = ('a', 'b', 'c' ,'d')
tup = tuple('abcde')
print(newTuple)
print(tup)
print(newTuple[-2])
print(newTuple[0:2])

for i in range(len(newTuple)):
    print(newTuple[i])

print('f' in newTuple)

def searchTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'The element does not exist'

print(searchTuple(newTuple, 'c'))
print(max(newTuple) )
print(newTuple.count('a'))
init_tuple = ()
print (init_tuple.__len__())

init_tuple = [(0, 1), (1, 2), (2, 3)]

result = sum(n for _, n in init_tuple)

print(result)