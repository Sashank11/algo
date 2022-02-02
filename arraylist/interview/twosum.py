
def findPairs(num, target):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i] == num[j]:
                continue
            elif num[i] + num[j] == target:
                print(i,j)

myList = [1, 2, 3, 2, 3, 4, 5, 6]
findPairs(myList, 6)