from LinkedList import LinkedList, Node

def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)
    shorter = llA if lenA < lenB else llB
    longer = llA if lenA > lenB else llB

    diff = len(longer) - len(shorter)

    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next
        

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode

def addSameNode(llA, llB, value):
    currNode = Node(value)
    llA.tail.next = currNode
    llA.tail = currNode
    llB.tail.next = currNode
    llB.tail = currNode

llA = LinkedList()
llA.generate(3, 0, 10)
llB = LinkedList()
llB.generate(4, 0, 10)

addSameNode(llA, llB, 7)
addSameNode(llA, llB, 1)
addSameNode(llA, llB, 6)

print(llA)
print(llB)

print(intersection(llA, llB))