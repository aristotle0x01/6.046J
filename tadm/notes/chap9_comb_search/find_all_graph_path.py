import collections


class Solution:
    # Constructor
    def __init__(self):
        self.finished = False
        self.graph = []
        self.n = 0
        self.src = -1
        self.dst = -1

    def initialize(self, n: int, edges: list[list[int]], src: int, dst: int):
        self.graph = collections.defaultdict(list)
        for s, d in edges:
            self.graph[s].append(d)
        self.src = src
        self.dst = dst
        self.n = n

    def is_a_solution(self, a: [], k: int, n: int):
        length = len(a)
        if length > 0 and a[length-1] == self.dst:
            return True
        return False

    def process_solution(self, a: [], k: int, n: int):
        print('{', end='')
        for i in range(len(a)):
            print('{0} '.format(a[i]), end='')
        print('}\n', end='')

    def make_move(self, a: [], k: int, n: int):
        return

    def unmake_move(self, a: [], k: int, n: int):
        return

    def construct_candidates(self, a: [], k: int, n: int, c: []):
        if k > n:
            return

        if k == 1:
            c.append(self.src)
        else:
            edges = self.graph[a[k-2]]
            for dest in edges:
                if dest not in a:
                    c.append(dest)

    def backtrack(self, a: [], k: int, n: int):
        candidates = []

        if self.is_a_solution(a, k, n):
            self.process_solution(a, k, n)
        else:
            k = k + 1
            self.construct_candidates(a, k, n, candidates)
            a.append(0)
            for i in range(len(candidates)):
                a[k-1] = candidates[i]
                self.make_move(a, k, n)
                self.backtrack(a, k, n)
                self.unmake_move(a, k, n)

                if self.finished:
                    return

            del a[-1]

    def find_all_paths(self, n: int, edges: list[list[int]], src: int, dst: int):
        self.initialize(n, edges, src, dst)
        a = []
        return self.backtrack(a, 0, n)


g = Solution()
g.find_all_paths(3,
                       [[0,1],[1,2],[0,2]],
                       0,
                       2)
g.find_all_paths(4,
                        [[0,1],[0,2],[1,2],[2,3]],
                        0,
                        3)
