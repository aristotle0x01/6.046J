from collections import defaultdict
import sys

# https://leetcode.com/problems/network-delay-time/
class Solution:
    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.edges = defaultdict(list)
        self.discovered = []
        self.distance = []

    def initialize_graph(self, n, times: list[list[int]]):
        self.edges = defaultdict(list)
        self.discovered = [False] * (n+1)
        self.discovered[0] = True
        self.distance = [sys.maxsize] * (n+1)
        for t in times:
            self.add_edge(t[0], (t[1], t[2]))

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
    # if there is any vertex not discovered, return -1
    # otherwise sort all the path weights, return the maximum
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        self.initialize_graph(n, times)
        self.dijkstra(k)
        for b in self.discovered:
            if not b:
                return -1

        self.distance[0] = 0
        ascend = sorted(self.distance)
        return ascend[n]

g = Solution()
print(g.networkDelayTime([[1,2,1]], 2, 2))

# 0 - 2 - 3
# 0 - 1 - 2 - 3