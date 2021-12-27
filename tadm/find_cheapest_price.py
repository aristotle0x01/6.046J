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
        self.level = [0] * n
        for item in flights:
            u = item[0]
            v = item[1]
            price = item[2]
            self.add_edge(u, (v, price))

    def add_edge(self, u, pair):
        self.edges[u].append(pair)

    def bfs(self, s, n):
        self.level = [0] * n

        # Mark all the vertices as not visited
        visited = [False] * n

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)

            for (i, price) in self.edges[s]:
                if not visited[i]:
                    self.level[i] = self.level[s] + 1
                    queue.append(i)
                    visited[i] = True
        return

    def dijkstra(self, src: int, dst: int, k: int):
        v = src
        self.distance[v] = 0

        max_number_of_edges_allowed = k + 1

        weight = 0
        dist = sys.maxsize
        all_routes = []
        while not self.discovered[v]:
            self.discovered[v] = True

            if v != src:
                weight = weight + dist

            edges = self.edges[v]
            for (w, price) in edges:
                if self.distance[w] > (self.distance[v]+price):
                    if w != dst:
                        self.parent[w] = v
                        self.level[w] = self.level[v] + 1
                        self.distance[w] = self.distance[v] + price
                    else:
                        if self.level[v] >= max_number_of_edges_allowed:
                            continue

                        self.parent[w] = v
                        self.level[w] = self.level[v] + 1
                        path = []
                        self.find_path(dst, path)
                        self.distance[w] = self.distance[v] + price
                        all_routes.append((self.distance[dst], path))

            dist = sys.maxsize
            for i in range(len(self.discovered)):
                if not self.discovered[i] and dist > self.distance[i]:
                    dist = self.distance[i]
                    v = i

        return all_routes

    def find_path(self, dst: int, path:[]):
        path.append(dst)

        if self.parent[dst] == -1:
            return
        else:
            return self.find_path(self.parent[dst], path)

    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        if src >= n or dst >= n or src < 0 or dst < 0 or k >= n or k < 0:
            return -1

        self.initialize_graph(n, flights)
        #self.bfs(src, n)
        all_routes = self.dijkstra(src, dst, k)
        if len(all_routes) == 0:
            return -1

        sorted_routes = sorted(all_routes, key=lambda x: x[0])
        for (weight, routes) in sorted_routes:
            if len(routes) - 2 <= k:
                return weight

        return -1

g = Solution()
print(g.findCheapestPrice(4,
                          [[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
                          0,
                          3,
                          1))

# 0 - 2 - 3
# 0 - 1 - 2 - 3