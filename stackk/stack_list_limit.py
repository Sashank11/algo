class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    #isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #isFull
    def isFull(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    #push 
    def push(self, value):
        if self.isFull():
            return "The Stack is Full"
        else:
            self.list.append(value)
            return "The element has already been pushed"
    
    #pop
    def pop(self):
        if  self.isEmpty():
            return "The Stack is Empty"
        else:
            return self.list.pop()

    #peek
    def peek(self):
        if  self.isEmpty():
            return "The Stack is Empty"
        else:
            return self.list[-1]

    #delete
    def delete(self):
        self.list = None

custom_stack = Stack(4)
print(custom_stack.isEmpty())
print(custom_stack.isFull())
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(4)
print(custom_stack)
print(custom_stack.push(5))
print(custom_stack.pop())
print(custom_stack.pop())
print(custom_stack.pop())
print(custom_stack.peek())
print(custom_stack.pop())
print(custom_stack.isEmpty())