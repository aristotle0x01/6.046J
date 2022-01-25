
# https://leetcode.com/problems/unique-paths-iii/
class Solution:
    # Constructor
    def __init__(self):
        self.finished = False
        self.count = 0
        self.board = []
        self.rows = 0
        self.columns = 0
        self.start = (0, 0)
        self.end = (0, 0)
        self.obstacles_count = 0

    def initialize(self, grid: list[list[int]]):
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.count = 0
        self.board = [[0]*(self.columns+1) for i in range(self.rows+1)]
        for i in range(1, self.rows+1):
            for j in range(1, self.columns+1):
                self.board[i][j] = grid[i-1][j-1]
                if self.board[i][j] == 1:
                    self.start = (i, j)
                if self.board[i][j] == 2:
                    self.end = (i, j)
                if self.board[i][j] == -1:
                    self.obstacles_count += 1

    def is_a_solution(self, a: [], k: int, n: int):
        if len(a) == 0:
            return False

        x, y = a[-1][0], a[-1][1]
        if len(a) == n and self.board[x][y] == 2:
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

        if k == 1:
            c.append(self.start)
        else:
            x, y = a[-1]
            tmp = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
            for tx, ty in tmp:
                if tx > self.rows or tx < 1:
                    continue
                if ty > self.columns or ty < 1:
                    continue
                if self.board[tx][ty] == -1:
                    continue

                b = False
                for ax, ay in a:
                    if ax == tx and ay == ty:
                        b = True
                        break
                if b is True:
                    continue

                c.append((tx, ty))

    def backtrack(self, a: [], k: int, n: int):
        if self.is_a_solution(a, k, n):
            self.process_solution(a, k, n)
        else:
            k = k + 1
            candidates = []
            self.construct_candidates(a, k, n, candidates)
            a.append((0, 0))
            for x, y in candidates:
                a[k-1] = (x, y)
                self.make_move(a, k, n)
                self.backtrack(a, k, n)
                self.unmake_move(a, k, n)

                if self.finished:
                    return

            del a[-1]

    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        a = []
        self.initialize(grid)
        self.backtrack(a, 0, self.rows * self.columns - self.obstacles_count)
        return self.count


g = Solution()
print(g.uniquePathsIII([[0,1],[2,0]]))
