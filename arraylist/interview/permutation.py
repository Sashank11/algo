def permutation(list1, list2):
    if len(list1) != len(list2):
        print("no permutation")
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("permutation")
        return True
    else:
        return False

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['e', 'd', 'c', 'b', 'a']

print(permutation(list1, list2))