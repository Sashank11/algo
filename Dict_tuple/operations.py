englishtoSpanish = {"one": "uno", "two":"dos", "three":"tres"}
englishtoSpanish['four'] = "cuarto"
dict = {'a': '1', 'b': '2'}
#print('uno' in englishtoSpanish.values())
#print(len(englishtoSpanish))
##print(sorted(myDict, reverse=False))
#for _ in sorted(dict):
    #print (dict[_])

crates = {}
box = {}
box['biscuit'] = 1
box['cake'] = 3
crates['box'] = box
#print(len(dict))
arr = {}
arr[1] = 1
arr['1'] = 2
arr[1] += 1

sum = 0
for k in arr:
    sum += arr[k]

print(sum)
my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12

sum = 0
for k in my_dict:
    sum += my_dict[k]

print(sum)
print(my_dict)
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1 == id2)
my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4
 
sum = 0
for k in my_dict:
    sum += my_dict[k]
    
print (sum)