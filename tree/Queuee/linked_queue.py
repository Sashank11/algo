class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return(str(self.value))

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linked_list = Linked_list()

    def __str__(self):
        values = [str(x) for x in self.linked_list]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linked_list.head ==None:
            self.linked_list.head = newNode
            self.linked_list.tail = newNode
        else:
            self.linked_list.tail.next = newNode
            self.linked_list.tail = newNode

    def isEmpty(self):
        if self.linked_list.head == None:
            return True
        else:
            return False
        
    def dequeue(self):
        if self.isEmpty():
            return "There is no node in the Queue"
        else:
            tempNode = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = self.linked_list.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "There is no node in the Queue"
        else:
            return self.linked_list.head

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None

#custom_queue = Queue()
#custom_queue.enqueue(1)
#custom_queue.enqueue(2)
#custom_queue.enqueue(3)
#print(custom_queue)
#print(custom_queue.peek())
#print(custom_queue)