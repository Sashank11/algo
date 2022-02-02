
import random
integers = [1, 2, 3,4]
shoplist = ['Milk', 'Cheese', 'Butter']
mixedlist = [1, 23.7, 'spam']
nestedlist = [1, 2, 3, 4, 5, [5.1, 5.2], ['test']]
empty = []

#print(shoplist[2])
#print('Milk' in shoplist)

#print(shoplist[-1])
for i in range(len(shoplist)):
    shoplist[i] = shoplist[i] + "+"
    print(shoplist[i])

for i in empty:
    print("Emptyness")

#print(shuffle(integers))
print(integers[: :2])
a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50
# print(a)
random.shuffle(a)
#print(a)
v=[1,2,3,4,5]
#print(v[3:0:-1])


fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print(sum)