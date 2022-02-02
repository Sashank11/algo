from this import d


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.Linked_list = Linked_list()

    def __str__(self):
        values = [str(x.value) for x in self.Linked_list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.Linked_list.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.Linked_list.head
        self.Linked_list.head = node

    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            nodeValue = self.Linked_list.head.value
            self.Linked_list.head = self.Linked_list.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            nodeValue = self.Linked_list.head.value
            return nodeValue

    def delete(self):
        self.Linked_list.head = None

custom_stack = Stack()
custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)
custom_stack.push(4)
print(custom_stack.peek())
print(custom_stack)
print('---------------')
custom_stack.pop()
custom_stack.pop()
#print(custom_stack.pop())
print(custom_stack)