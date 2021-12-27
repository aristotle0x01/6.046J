# The Algorithm Design Manual Third Edition
# chapter 7 Graph Traversal
# python implementation
from collections import defaultdict

class GraphWar:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.edges = defaultdict(list)
        self.degree = defaultdict(list)
        self.nedges = 0
        self.directed = 0

    def initialize_graph(self, directed):
        self.edges = defaultdict(list)
        self.degree = defaultdict(list)
        self.nedges = 0
        self.directed = directed

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.edges[u].append(v)
        self.nedges = self.nedges + 1
        if u in self.degree:
            self.degree[u] = self.degree[u] + 1
        else:
            self.degree[u] = 1

    def print_graph(self):
        for (k, list) in self.edges.items():
            print(k, end=": ")
            for i in list:
                print(i, end=" ")
            print('\n')

    # Function to print a BFS of graph
    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.edges) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.edges[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    # Function to print a DFS of graph
    def DFS(self, s, visited):
        visited[s] = True

        print(s, end=" ")
        for i in self.edges[s]:
            if not visited[i]:
                self.DFS(i, visited)

# Driver code

def findMinHeightTrees(n: int, edges: list[list[int]]) -> list[int]:
    for arr in edges:
        print(arr[0], end=": ")
        print(arr[1], end=" ")
        print('\n')

findMinHeightTrees(2, [[3,0],[3,1],[3,2],[3,4],[5,4]])

# Create a graph given in
# the above diagram
g = GraphWar()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.print_graph()