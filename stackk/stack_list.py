#Stack  based on python list  with no limits

class Stack:

    def __init__(self):
        self.list  = []

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

    # push
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully pushed"
    
    #pop
    def pop(self):
        if self.isEmpty():
            return "Ther is not any element in the stack"
        else:
            return self.list.pop()

    #peek
    def peek(self):
        if self.isEmpty():
            return "Ther is not any element in the stack"
        else:
            return self.list[-1]

    #delete
    def delete(self):
        self.list = None



custom_stack = Stack()
custom_stack.push(4)
custom_stack.push(3)
custom_stack.push(2)
#print(custom_stack)
print(custom_stack.pop())
#print(custom_stack)

