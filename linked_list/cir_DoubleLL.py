class Node:

    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
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

    def createCDLL(self, nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node
        return "The CDLL is created successfully"


    def insertCDLL(self, nodeValue, location):
        if self.head is None:
            return "The Circular Doubly Linked List does not have any nodes"
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location -1:
                    currentNode = currentNode.next
                    index +=1
                newNode.next = currentNode.next
                newNode.prev = currentNode
                newNode.next.prev = newNode
                currentNode.next = newNode
            return "The node has been inserted"

    def traverseCDLL(self):
        if self.head is None:
            print("The Circular Doubly Linked List does not have any nodes")
        else:
            linkList = self.head
            while linkList is not None:
                print(linkList.value)
                if linkList == self.tail:
                    break
                linkList = linkList.next
            

    def revTraverseCDLL(self):
        if self.head is None:
            print("The Circular Doubly Linked List does not have any nodes")
        else:
            linkList = self.tail
            while linkList is not None:
                print(linkList.value)
                if linkList ==self.head:
                    break
                linkList = linkList.prev

    def searchCDLL(self, value):
        if self.head is None:
            return "The Circular Doubly Linked List does not have any nodes"
        else:
            linkList = self.head
            while linkList:
                if linkList.value == value:
                    return linkList.value
                if linkList == self.tail:
                    return "loop terminated value not found"
                linkList = linkList.next

    def deleteNodeCDLL(self, location):
        if self.head is None:
            return "The Circular Doubly Linked list does not have any nodes"
        else:
            if  location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                    if self.head == self.tail:
                        self.head.prev = None
                        self.head.next = None
                        self.head = None
                        self.tail = None
                    else:
                        self.tail = self.tail.prev
                        self.tail.next = self.head
                        self.head.prev = self.tail
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index +=1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print("Node has been removed")

    def deleteCDLL(self):
        if self.head is None:
            print("The Circular Doubly Linked list does not have any nodes")
        else:
            self.tail.next = None
            currentNode = self.head
            while currentNode is not None:
                currentNode.prev = None
                currentNode = currentNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been deleted")



circularDLL = CircularDoublyLinkedList()
print(circularDLL.createCDLL(5))
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,1)
circularDLL.insertCDLL(2,2)
circularDLL.insertCDLL(3,3)
circularDLL.insertCDLL(4,4)
circularDLL.insertCDLL(6,-1)

print([node.value for node in circularDLL])

#circularDLL.deleteNodeCDLL(5)
circularDLL.deleteCDLL()

print([node.value for node in circularDLL])

#circularDLL.traverseCDLL()
#circularDLL.revTraverseCDLL()
#print(circularDLL.searchCDLL(6))
