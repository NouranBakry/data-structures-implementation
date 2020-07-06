# Implementing basic queue

class Queue:

    def __init__(self):
        self.front = -1
        self.end = -1
        self.data = []
    
    def enqueue(self, value):
        self.front = 0
        self.end += 1
        self.data.insert(self.front, value)
    
    def dequeue(self):
        if self.end == -1:
            print('Queue is empty')
            return
        print(self.data[-1], ' dequeued successfully')
        del self.data[self.end]
        self.end -= 1

    def printQueue(self):
        print('Queue ', self.data)