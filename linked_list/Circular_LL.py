class Node:

    def __init__(self, value =None):
        self.value = value
        self.next = None

class CircularSignglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node =node.next
            if node == self.tail.next:
                break
            

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"


    def insertCSLL(self, nodeValue, location):
        if self.head is None:
            return "The head reference is None" 
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode 
            elif location == -1:
                    newNode.next = self.tail.next
                    self.tail.next = newNode
                    self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location -1:
                    currentNode = currentNode.next
                    index +=1
                nextNode = currentNode.next
                currentNode.next = newNode
                newNode.next = nextNode
            
            return "The node has been inserted"


    def traverseCSLL(self):
        if self.head is None:
            print("The Circular Singly Linked List does not exist")
        else:
            linkList = self.head
            while linkList:
                print(linkList.value)
                linkList = linkList.next
                if linkList == self.tail.next:
                    break
            
    def searchCSLL(self, value):
        if self.head is None:
            return "The Circular Singly Linked List does not exist"
        else:
            linkList = self.head
            while linkList:
                if linkList.value == value:
                    return linkList.value
                linkList = linkList.next 
                if linkList == self.tail.next:
                    return "Loop terminated value not found"

    def deleteNode(self,location):
        if self.head is None:
            print("The Circular Singly Linked List does not exist")
        else:
            if location ==0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    linkList = self.head
                    while linkList is not None:
                        if linkList.next == self.tail:
                            break
                        linkList = linkList.next
                    linkList.next = self.head
                    self.tail = linkList
            else:
                currentNode = self.head
                index = 0
                while index < location -1:
                    currentNode = currentNode.next
                    index +=1
                nextNode = currentNode.next
                currentNode.next = nextNode.next

    def deleteCSLL(self):
        if self.head is None:
            print("The Circular Singly Linked List does not exist")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None

circularSLL = CircularSignglyLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,-1)
circularSLL.insertCSLL(4,-1)
circularSLL.insertCSLL(5,-1)
circularSLL.insertCSLL(3,3)
#circularSLL.traverseCSLL()
print([node.value for node in circularSLL])
#circularSLL.deleteNode(-1)
circularSLL.deleteCSLL()
print([node.value for node in circularSLL])

