class Queue:
    def __init__(self, max_size):
        self.item = max_size * [None]
        self.max_size = max_size
        self.top = -1
        self.start = -1

    def __str__(self):
        values = [str(x) for x in self.item]
        return ' '.join(values)

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top +=1
                if self.start == -1:
                    self.start = 0
            self.item[self.top] = value
            return "The element is inserted at the end of the Queue"

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            element = self.item[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start +=1
            self.item[start] = None
            return element

    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.item[self.start]

    def delete(self):
        self.item = self.max_size * [None]
        self.top = -1
        self.start = -1

custom_queue = Queue(3)
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
#print(custom_queue.dequeue())
#print(custom_queue.dequeue())
#print(custom_queue.peek())
custom_queue.delete()
print(custom_queue)