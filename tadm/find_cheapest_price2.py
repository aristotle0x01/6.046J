from collections import defaultdict
import sys

# https://leetcode.com/problems/cheapest-flights-within-k-stops/
class Solution:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.edges = defaultdict(list)
        self.discovered = []
        self.distance = []
        self.parent = []
        self.level = []

    def initialize_graph(self, n, flights: list[list[int]]):
        self.edges = defaultdict(list)
        self.discovered = [False] * n
        self.distance = [sys.maxsize] * n
        self.parent = [-1] * n
        for item in flights:
            u = item[0]
            v = item[1]
            price = item[2]
            self.add_edge(u, (v, price))

    def add_edge(self, u, pair):
        self.edges[u].append(pair)

    def find_path(self, dst: int, path: []):
        path.append(dst)

        if self.parent[dst] == -1:
            return
        else:
            return self.find_path(self.parent[dst], path)

    def bfs(self, src, dst, n, k):
        routes = []

        # Mark all the vertices as not visited
        visited = [False] * n

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(src)
        visited[src] = True
        self.distance[src] = 0
        while queue:
            s = queue.pop(0)

            for (i, price) in self.edges[s]:
                if not visited[i]:
                    self.parent[i] = s
                    self.distance[i] = self.distance[s] + price
                    queue.append(i)
                    visited[i] = True

                if i == dst:
                    path = []
                    self.find_path(s, path)
                    if (len(path) - 1) <= k:
                        routes.append(self.distance[s] + price)

        return routes

    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        if src >= n or dst >= n or src < 0 or dst < 0 or k >= n or k < 0:
            return -1

        self.initialize_graph(n, flights)
        routes = self.bfs(src, dst, n, k)
        if len(routes) == 0:
            return -1

        sorted_routes = sorted(routes)
        return sorted_routes[0]

g = Solution()
print(g.findCheapestPrice(5,
                          [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]],
                          0,
                          4,
                          1))
# 1 - 2 - 0
# 1 - 3 - 4
# 4 - 0 - 3 -1
# 4 - 2 - 4
# 0 - 2 - 3
# 0 - 1 - 2 - 3