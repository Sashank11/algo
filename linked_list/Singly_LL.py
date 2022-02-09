
class Node:
    
    def __init__(self, value =None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node =self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                currentNode = self.head
                index = 0
                while index < location -1:
                    currentNode = currentNode.next
                    index += 1

                nextNode = currentNode.next
                currentNode.next = newNode
                newNode.next= nextNode
                if currentNode == self.tail:
                    self.tail = newNode
    
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            linkList = self.head
            while linkList is not None:
                print(linkList.value)
                linkList = linkList.next
            

    def searchSLL(self, value):
        if self.head is None:
            return("The Singly Linked List does not exist")
        else:
            linkList = self.head
            while linkList is not None:
                if linkList.value == value:
                    return linkList.value
                linkList = linkList.next
            else:
                return "Value Not Found"
    
    def deleteNode(self, location):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            if location == 0:
                #if linkList.next == None:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:   
                    self.head = self.head.next
            elif location == -1:
                #if linkList.next == None:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else: 
                    linkList = self.head
                    while linkList is not None:
                        if linkList.next == self.tail:
                            break
                        linkList = linkList.next
                    linkList.next = None
                    self.tail = linkList        
            else:
                currentNode = self.head
                index = 0
                while index < location - 1:
                    currentNode = currentNode.next
                    index += 1
                nextNode = currentNode.next
                currentNode.next = nextNode.next

    def deleteSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            self.head = None
            self.tail = None

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 0)
singlyLinkedList.insertSLL(2, -1)
singlyLinkedList.insertSLL(4, -1)
singlyLinkedList.insertSLL(5, -1)
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(3, 3)
print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteSLL()  
#singlyLinkedList.deleteNode(3)
print([node.value for node in singlyLinkedList])  
#singlyLinkedList.traverseSLL()






#     def insertSLL(self, value, location):
#         newNode = Node(value)
#         if self.head is None:                     # This does not work
#             self.head = newNode
#             self.tail = newNode
        
#         else:
#             if location == 0:
#                 newNode.next = self.head
#                 self.head = newNode
#             elif location == -1:
#                 newNode.next = None
#                 self.tail.next = newNode
#                 self.tail = newNode
#             else:
#                 tempNode = self.head
#                 index = 0
#                 while index < location - 1:
#                     tempNode = tempNode.next
#                     index +=1
#                 nextNode = tempNode.next
#                 tempNode.next = newNode
#                 newNode.next = nextNode
#                 if tempNode == self.tail:
#                     self.tail = newNode



# singlyLinkedList.insertSLL(1, -1)
# singlyLinkedList.insertSLL(2, -1)
# singlyLinkedList.insertSLL(3, -1)
# singlyLinkedList.insertSLL(4, -1)
# singlyLinkedList.insertSLL(0, 0)
# singlyLinkedList.insertSLL(0, 3)

