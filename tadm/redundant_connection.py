
from collections import defaultdict

# remove the last back edge, it will be done
class Solution:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.edges = defaultdict(list)

    def initialize_graph(self):
        self.edges = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    # Function to print a BFS of graph
    def BFS(self, s, n):
        visited = [False] * n

        queue = []
        queue.append(s)

        visited[s] = True

        while queue:
            k = queue.pop(0)

            for i in self.edges[k]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

        for i in range(1, n):
            if visited[i] is False:
                return False
        return True

    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        length = len(edges)
        if length <= 2:
            return []

        for r in reversed(edges):
            self.initialize_graph()
            for arr in edges:
                if r != arr:
                    self.addEdge(arr[0], arr[1])
            b = self.BFS(1, (length + 1))
            if b is True:
                return r

        return []

g = Solution()
print(g.findRedundantConnection([[1,2],[1,3],[2,3]]))