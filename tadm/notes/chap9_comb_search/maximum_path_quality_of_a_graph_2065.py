import collections
import sys


# https://leetcode.com/problems/maximum-path-quality-of-a-graph/
class Solution:
    def __init__(self):
        self.finished = False
        self.graph = []
        self.n = 0
        self.max_time = 0
        self.values = None
        self.max_path_quality = 0
        self.max_path = []
        self.cur_path_time = 0

    def initialize(self, values: list[int], edges: list[list[int]], max_time: int):
        self.finished = False
        self.graph = collections.defaultdict(list)
        for s, d, time in edges:
            self.graph[s].append((d, time))
            self.graph[d].append((s, time))
        self.n = len(values)
        self.max_time = max_time
        self.values = values
        self.max_path_quality = 0
        self.max_path = []
        self.cur_path_time = 0

    def is_a_solution(self, a: [], k: int, n: int):
        length = len(a)
        if length > 0 and a[length-1] == 0 and self.cur_path_time <= self.max_time:
            edges = self.graph[0]
            t = sys.maxsize
            for dst, time in edges:
                if time < t:
                    t = time
            if self.cur_path_time + 2*t > self.max_time:
                return True

        return False

    def process_solution(self, a: [], k: int, n: int):
        tmp = {}
        s = 0
        for i in a:
            if i not in tmp:
                s = s + self.values[i]
                tmp[i] = 1
        if s > self.max_path_quality:
            self.max_path_quality = s
            self.max_path = a.copy()

    def make_move(self, a: [], k: int, n: int):
        return

    def unmake_move(self, a: [], k: int, n: int):
        return

    def construct_candidates(self, a: [], k: int, n: int, c: []):
        if k == 1:
            c.append((0, 0))
        else:
            edges = self.graph[a[k-2]]
            for dst, time in edges:
                if (self.cur_path_time + time) <= self.max_time:
                    c.append((dst, time))

    def backtrack(self, a: [], k: int, n: int):
        if self.is_a_solution(a, k, n):
            self.process_solution(a, k, n)
        else:
            k = k + 1
            candidates = []
            self.construct_candidates(a, k, n, candidates)
            a.append(0)
            for i in range(len(candidates)):
                dst, time = candidates[i]
                a[k-1] = dst
                self.cur_path_time = self.cur_path_time + time
                self.make_move(a, k, n)
                self.backtrack(a, k, n)
                self.unmake_move(a, k, n)
                self.cur_path_time = self.cur_path_time - time

                if self.finished:
                    return

            del a[-1]

    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        self.initialize(values, edges, maxTime)
        a = []
        self.backtrack(a, 0, len(values))
        print('{', end='')
        for i in range(len(self.max_path)):
            print('{0}-'.format(self.max_path[i]), end='')
        print('{0}={1}\n'.format('}', self.max_path_quality), end='')
        return self.max_path_quality


g = Solution()
print(g.maximalPathQuality([9,7,4], [[0,1,10],[0,2,20]], 20))
print(g.maximalPathQuality([95], [], 83))
print(g.maximalPathQuality([39,73,63,17], [[0,1,61],[1,2,13],[2,3,44],[0,3,11]], 10))
print(g.maximalPathQuality([61,11,18,43,81], [[0,3,45],[0,2,16],[0,1,36],[3,4,38],[2,3,29]], 88))
print(g.maximalPathQuality([5,10,15,20], [[0,1,10],[1,2,10],[0,3,10]], 30))
print(g.maximalPathQuality([0,32,10,43], [[0,1,10],[1,2,15],[0,3,10]], 49))
print(g.maximalPathQuality([1,2,3,4], [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], 50))