from collections import defaultdict
import sys

# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
class Solution:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.edges = defaultdict(list)
        self.discovered = []
        self.distance = []

    def initialize_graph(self, n, from_edges: list[list[int]]):
        self.edges = defaultdict(list)
        self.discovered = [False] * n
        self.distance = [sys.maxsize] * n
        for t in from_edges:
            self.add_edge(t[0], (t[1], t[2]))
            self.add_edge(t[1], (t[0], t[2]))

    def add_edge(self, u, pair):
        self.edges[u].append(pair)

    def dijkstra(self, src: int):
        v = src
        self.distance[v] = 0

        weight = 0
        dist = sys.maxsize
        while not self.discovered[v]:
            self.discovered[v] = True

            if v != src:
                weight = weight + dist

            edges = self.edges[v]
            for (w, time) in edges:
                if self.distance[w] > (self.distance[v] + time):
                    self.distance[w] = self.distance[v] + time

            dist = sys.maxsize
            for i in range(len(self.discovered)):
                if not self.discovered[i] and dist > self.distance[i]:
                    dist = self.distance[i]
                    v = i

    # impose dijkstra on graph from k
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        cities = []

        for i in range(n):
            self.initialize_graph(n, edges)
            self.dijkstra(i)

            array = []
            for j in range(n):
                if i == j:
                    continue
                d = self.distance[j]
                if d <= distanceThreshold:
                    array.append(j)

            cities.append((i, array))

        i = -1
        min_len = sys.maxsize
        for (k, array) in cities:
            if len(array) < min_len:
                i = k
                min_len = len(array)
            elif len(array) == min_len and k > i:
                i = k

        return i

g = Solution()
print(g.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))

# 0 - 2 - 3
# 0 - 1 - 2 - 3