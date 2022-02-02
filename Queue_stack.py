class Stack():
    def __init__(self):
        self.list = []
    
    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()
        
class Queue_Stack():
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    
    def dequeue(self):
        while len(self.in_stack):
            self.out_stack.push(self.in_stack.pop())
        result = self.out_stack.pop()
        while len(self.out_stack):
            self.in_stack.push(self.out_stack.pop())
        return result


cust_queue = Queue_Stack()
cust_queue.enqueue(1)
cust_queue.enqueue(2)
cust_queue.enqueue(3)
#print(cust_queue.dequeue())
print(cust_queue.dequeue())
#print(cust_queue)
# cust_queue.dequeue()
# print(cust_queue)