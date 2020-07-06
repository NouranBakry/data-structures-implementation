# Implementing basic stack 

class Stack:
    def __init__(self):
        self.top = -1
        self.data = []
    
    def push(self, value):
        self.data.append(value)
        self.top +=1
        print(value, ' pushed successfully')
    
    def pop(self):
        if self.top == -1:
            print('Cant pop from an empty stack')
            return
        print(self.data[self.top], ' popped successfully')
        del self.data[self.top]
        self.top -= 1

    def printStack(self):
        print('Stack: ', self.data)
