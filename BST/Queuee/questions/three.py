class Multi_stack:
    def __init__(self, stack_size):
        self.number_stacks = 3
        self.cust_list = [0] *(self.number_stacks * stack_size)
        self.sizes = [0] * self.number_stacks
        self.stack_size = stack_size

    def is_full(self, stack_num):
        if self.sizes[stack_num] == self.stack_size:
            return True
        else:
            return False

    def is_empty(self, stack_num):
        if self.sizes[stack_num] == 0:
            return True
        else:
            return False

    def indexofTop(self, stack_num):
        offset = stack_num * self.stack_size # the xth stack multiplied by stack size
        return offset + self.sizes[stack_num] -1 # self.sizes[stack_num] is the no of element in stack 

    def push(self, item, stack_num):
        if self.is_full(stack_num):
            return "The stack is full"
        else:
            self.sizes[stack_num] +=1
            self.cust_list[self.indexofTop(stack_num)] = item 
    
    def pop(self, stack_num):
        if self.is_empty(stack_num):
            return "The stack is empty"
        else:
            value = self.cust_list[self.indexofTop(stack_num)]
            self.cust_list[self.indexofTop(stack_num)] = 0
            self.sizes[stack_num] -=1
            return value


    def peek(self, stack_num):
        if self.is_empty(stack_num):
            return "The stack is empty"
        else:
            return self.cust_list[self.indexofTop(stack_num)]

cust_stack = Multi_stack(6)
print(cust_stack.is_full(0))
print(cust_stack.is_empty(1))
cust_stack.push(1, 0)
cust_stack.push(2, 0)
cust_stack.push(3, 2)
print(cust_stack.peek(1))
print(cust_stack.pop(0))