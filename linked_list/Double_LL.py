class Node:

    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def createDLL(self, nodeValue):
        node =Node(nodeValue)
        self.head = node
        self.tail = node
        return "The DLL is created successfully"

    def insertDLL(self, nodeValue, location):
        if  self.head is None:
            print("Doubly Linked List does not exist")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                currentNode= self.head
                index = 0
                while index < location -1:
                    currentNode = currentNode.next
                    index +=1
                newNode.next = currentNode.next
                newNode.prev = currentNode
                newNode.next.prev = newNode
                currentNode.next = newNode

    def traverseDLL(self):
        if self.head is None:
            print("The Doubly Linked List does not exist")
        else:
            linkList = self.head
            while linkList is not None:
                print(linkList.value)
                linkList = linkList.next


    def revTraverseDLL(self):
        if self.head is None:
                print("The Doubly Linked List does not exist")
        else:
            linkList =self.tail
            while linkList is not None:
                print(linkList.value)
                linkList = linkList.prev
        
    def searchDLL(self, value):
        if self.head is None:
            return("The Doubly Linked List does not exist")
        else:
            linkList = self.head
            while linkList is not None:
                if linkList.value == value:
                    return(linkList.value)
                linkList = linkList.next
            return "Value not found in Doubly Linked List"

    def deleteNode(self, location):
        if self.head is None:
            return("The Doubly Linked List does not have any nodes")
        else:
            if location ==0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                currentNode = self.head
                index = 0
                while index < location -1:
                    currentNode = currentNode.next
                    index +=1
                currentNode.next = currentNode.next.next
                currentNode.next.prev = currentNode
            print("The node has been successfully deleted")

    def deleteDLL(self):
        if self.head is None:
            print("The Doubly Linked List does not have any nodes")
        else:
            currentNode = self.head
            while currentNode:
                currentNode.prev = None
                currentNode = currentNode.next
            self.head = None
            self.head = None
            print("The DLL has been deleted")

doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)
doublyLL.insertDLL(0,0)
doublyLL.insertDLL(2,-1)
doublyLL.insertDLL(6, 2)

print([node.value for node in doublyLL])

#doublyLL.deleteNode(2)
doublyLL.deleteDLL()

print([node.value for node in doublyLL])
#print(doublyLL.searchDLL(6))
#doublyLL.traverseDLL()
#doublyLL.revTraverseDLL()