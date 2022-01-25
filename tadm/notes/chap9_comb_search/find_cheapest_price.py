import collections
import heapq
import sys


# https://leetcode.com/problems/cheapest-flights-within-k-stops/
class Solution:
    # Constructor
    def __init__(self):
        self.finished = False
        self.graph = []
        self.n = 0
        self.src = -1
        self.dst = -1
        self.stops = -1
        self.cost = sys.maxsize

    def initialize(self, n: int, edges: list[list[int]], src: int, dst: int, k: int):
        self.graph = collections.defaultdict(list)
        for s, d, c in edges:
            self.graph[s].append((d, c))
        self.src = src
        self.dst = dst
        self.n = n
        self.stops = k

    def is_a_solution(self, a: [], k: int, n: int):
        length = len(a)
        if length > 0 and a[length-1][0] == self.dst and (length-2) <= self.stops:
            return True
        return False

    def process_solution(self, a: [], k: int, n: int):
        print('{', end='')
        for i in range(len(a)):
            if i == len(a)-1:
                print('{0}---cost: {1}'.format(a[i][0], a[i][1]), end='')
            else:
                print('{0} '.format(a[i][0]), end='')
        print('}\n', end='')

    def make_move(self, a: [], k: int, n: int):
        return

    def unmake_move(self, a: [], k: int, n: int):
        return

    def construct_candidates(self, a: [], k: int, n: int, c: []):
        if k > n:
            return

        if k == 1:
            c.append((self.src, 0))
        else:
            edges = self.graph[a[k-2][0]]
            for dst, cost in edges:
                b = False
                for av, ac in a:
                    if dst == av:
                        b = True
                        break
                if not b:
                    c.append((dst, a[k-2][1] + cost))

    def backtrack(self, a: [], k: int, n: int):
        candidates = []

        if self.is_a_solution(a, k, n):
            self.process_solution(a, k, n)
        else:
            k = k + 1
            self.construct_candidates(a, k, n, candidates)
            a.append((0, 0))
            for i in range(len(candidates)):
                a[k-1] = candidates[i]
                self.make_move(a, k, n)
                self.backtrack(a, k, n)
                self.unmake_move(a, k, n)

                if self.finished:
                    return

            del a[-1]

    def find_cheapest_price(self, n: int, flights: list[list[int]], src: int, dst: int, K: int) -> int:
        self.initialize(n, flights, src, dst, K)
        a = []
        return self.backtrack(a, 0, n)

    # reference solution:
    #   https://thatgirlcoder.com/2020/07/08/find-cheapest-flights-within-k-stops/
    def find_cheapest_price_ref(self, n: int, flights: list[list[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for s, d, c in flights:
            graph[s].append((d, c))

        pq = [(0, src, 0)]

        while pq:
            curr_cost, curr_node, curr_stops = heapq.heappop(pq)

            if curr_node == dst:
                return curr_cost

            if curr_stops <= K:
                for dest, cost in graph[curr_node]:
                    heapq.heappush(pq, (curr_cost + cost, dest, curr_stops + 1))

        return -1


g = Solution()
print(g.find_cheapest_price_ref(4,
                          [[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
                          0,
                          3,
                          1))
print(g.find_cheapest_price(4,
                          [[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
                          0,
                          3,
                          1))
print(g.find_cheapest_price_ref(3,
                          [[0,1,100],[1,2,100],[0,2,500]],
                          0,
                          2,
                          1))
print(g.find_cheapest_price(3,
                          [[0,1,100],[1,2,100],[0,2,500]],
                          0,
                          2,
                          1))