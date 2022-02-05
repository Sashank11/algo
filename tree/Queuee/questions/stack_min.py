class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next:
            string  += ' , ' + str(self.next)
        return string

class Stack():
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            return None
        else:
            return self.minNode.value
        
    def push(self, item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value = self.minNode.value, next = self.minNode) # next minimum node
        else:
            self.minNode = Node(value = item, next = self.minNode)
        self.top = Node(value= item, next = self.top)
    
    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item
        

cust_stack = Stack()

cust_stack.push(5)
print(cust_stack.min())
cust_stack.push(6)
print(cust_stack.min())
cust_stack.push(3)
print(cust_stack.min())
cust_stack.push(1)
print(cust_stack.min())
print(cust_stack.pop())
print(cust_stack.min())