#Implementing basic LinkedList

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.headNode = None
        self.tailNode = None
    
    def insertNode(self, value):
        node = Node(value)
        if self.headNode == None:
            self.headNode = node
            self.lastNode = node
        else:
            self.lastNode.next = node
            self.lastNode = node
        print(value, ' inserted successfully')
    
    def insertNodeAfter(self, value, referencedValue):
        node = Node(value)
        if self.headNode == None:
            self.headNode = node
            self.lastNode = node
        else:
            iterator = self.headNode
            while iterator.value != referencedValue:
                iterator = iterator.next
                node.next = iterator.next
            iterator.next = node
            print(value, ' inserted successfully')
    
    def traverseList(self):
        iterator = self.headNode
        while iterator != None:
            print(iterator.value)
            iterator = iterator.next
    
    def deleteNode(self, value):
        iterator = self.headNode
        while iterator.next.value != value:
            iterator = iterator.next
        temp = iterator.next
        iterator.next = temp.next
        del(temp)
        print(value, ' deleted successfully')
    