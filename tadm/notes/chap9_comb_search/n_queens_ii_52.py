
class Solution:
    # Constructor
    def __init__(self):
        self.finished = False
        self.n = 0
        self.count = 0
        self.board = []

    def initialize(self, n: int):
        self.n = n
        self.count = 0
        # (n+1) * (n+1) board, exclude [0][*] and [*][0]
        self.board = [[0]*(n+1) for i in range(n+1)]

    def is_a_solution(self, a: [], k: int, n: int):
        if len(a) == n and k == n:
            return True
        return False

    def process_solution(self, a: [], k: int, n: int):
        self.count = self.count + 1
        print('{', end='')
        for x, y in a:
            print('[{0},{1}] '.format(x, y), end='')
        print('}\n', end='')

    def make_move(self, a: [], k: int, n: int):
        return

    def unmake_move(self, a: [], k: int, n: int):
        return

    def construct_candidates(self, a: [], k: int, n: int, c: []):
        if k > n:
            return

        for i in range(1, n+1):
            c.append((k, i))

    def can_be_attacked(self, a: [], x: int, y: int):
        # same row & column
        for i in range(1, self.n+1):
            if self.board[x][i] == 1 or self.board[i][y] == 1:
                return True
        # at most four diagonal position
        for dx, dy in a:
            if 1 <= dx <= self.n and 1 <= dy <= self.n and ((dx+dy) == (x+y) or (dx-dy) == (x-y)):
                return True

        return False

    def backtrack(self, a: [], k: int, n: int):
        if self.is_a_solution(a, k, n):
            self.process_solution(a, k, n)
        else:
            k = k + 1
            candidates = []
            self.construct_candidates(a, k, n, candidates)
            a.append((0, 0))
            for x, y in candidates:
                if self.can_be_attacked(a, x, y):
                    continue

                self.board[x][y] = 1

                a[k-1] = (x, y)
                self.make_move(a, k, n)
                self.backtrack(a, k, n)
                self.unmake_move(a, k, n)

                self.board[x][y] = 0

                if self.finished:
                    return

            del a[-1]

    def totalNQueens(self, n: int) -> int:
        a = []
        self.initialize(n)
        self.backtrack(a, 0, n)
        return self.count


g = Solution()
print(g.totalNQueens(6))
