# Implementation of adjacency list and adjacency matrix

class Graph:
    def __init__(self, totalNodes):
        self.totalNodes = totalNodes
        self.adjMatrix = []
        self.adjList = []
    
    def acceptAdjMatrix(self):
        print('The total number of nodes: ', self.totalNodes)
        for row in range(self.totalNodes):
            temp = list(map(int, input('Enter Row '+ str(row) + ' of matrix:').split(' ')))
            self.adjMatrix.append(temp)
    def printAdjMatrix(self):
        if len(self.adjMatrix)  == 0:
            print('Adjacency matrix is empty ')
            return
        print('Adjacency Matrix: ')
        for row in self.adjMatrix:
            print(row)
    
    def acceptAdjList(self):
        print('The total number of nodes: ', self.totalNodes)
        for node in range(self.totalNodes):
            temp = list(map(int, input('Enter adjacency list node' + str(node) + ': ').split(' ')))
            self.adjList.append(temp)
    def printAdjList(self):
        if len(self.adjList) == 0:
            print('Adjacency list is empty ')
            return
        print('Adjacency list')
        for row in self.adjList:
            print(row)

    # breadth first search traversal
    def BFS(self):
        iterator = 0
        queue = [iterator]
        visited = [0]* self.totalNodes
        visited[iterator] = 1
        while len(queue) > 0:
            queue.extend([ node for node in self.adjList[iterator]if visited[node] != 1 and node not in queue])
            print(queue[0], end='')
            visited[iterator] = 1
            iterator = queue[0]
            queue = queue[1:]




