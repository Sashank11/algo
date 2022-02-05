class Queue:
    def __init__(self):
        self.item = []
    
    def __str__(self):
        values = [str(x) for x in self.item]
        return " ".join(values)

    def isEmpty(self):
        if self.item == []  or self.item is None:
            return True
        else:
            return False

    def enqueue(self, value):
        self.item.append(value)
        return "The element is inserted at the end of the queue"

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            return self.item.pop(0) #O(n) because each element is shifted to left


    def peek(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            return self.item[0]
    
    def delete(self):
        self.item = None

custom_queue = Queue()
#print(custom_queue.isEmpty())
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
print(custom_queue.peek())
print(custom_queue.delete())
print(custom_queue.isEmpty())