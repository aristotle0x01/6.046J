
from collections import defaultdict

# from https://leetcode.com/problems/course-schedule/
class Solution:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.edges = defaultdict(list)
        self.discovered = []
        self.processed = []
        self.ok = True

    def initialize_graph(self, n):
        self.edges = defaultdict(list)
        self.discovered = [False] * n
        self.processed = [False] * n
        self.ok = True

    def addEdge(self, u, v):
        self.edges[u].append(v)

    def dfs(self, s):
        if not self.ok:
            return

        self.discovered[s] = True

        for i in self.edges[s]:
            if self.discovered[i] is False:
                self.dfs(i)
            elif not self.processed[i]:
                # discovered but not processed, back edge found
                self.ok = False
                return

        self.processed[s] = True

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        self.initialize_graph(numCourses)

        exists = defaultdict(list)

        for arr in prerequisites:
            exists[arr[1]] = 1
            exists[arr[0]] = 1
            self.addEdge(arr[1], arr[0])

        for i in range(numCourses):
            if i not in exists.keys():
                self.processed[i] = True
                self.discovered[i] = True

        for i in range(numCourses):
            if i in exists.keys() and not self.processed[i] and self.ok:
                self.dfs(i)

        return self.ok

# Create a graph given in
# the above diagram
g = Solution()
print(g.canFinish(5,[[1,4],[2,4],[3,1],[3,2]]))