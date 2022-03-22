# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/
from functools import lru_cache


class Solution:
    def __init__(self):
        self.n = 0
        self.MOD = 10 ** 9 + 7

    def init(self, n: int):
        self.n = n

    def numOfWays_ref2(self, n):
        Mod = 1e9 + 7
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[1][0] = 6
        dp[1][1] = 6
        for i in range(2, n + 1):
            dp[i][0] = dp[i - 1][0] * 2 + dp[i - 1][1] * 2
            dp[i][1] = dp[i - 1][0] * 2 + dp[i - 1][1] * 3
        return (dp[n][0] + dp[n][1])

    # https://www.geeksforgeeks.org/count-number-of-unique-ways-to-paint-a-n-x-3-grid/
    def numOfWays_ref(self, n):
        f = g = 6
        M = 10 ** 9 + 7
        for _ in range(n - 1):
            f, g = (2 * f + 2 * g) % M, (2 * f + 3 * g) % M
        return (f + g) % M

    # let red = 1, yellow = 2, green = 3
    # p1,p2,p3 are color value of layer k+1
    # by local testing, only works when n <= 497, but submitted successfully to leetcode
    @lru_cache(None)
    def recur(self, p1: int, p2: int, p3: int, k: int):
        if k == 0:
            return 1

        loop_count = 0
        # for layer k, p1 candidates
        for i in range(1, 4):
            if i == p1:
                continue
            for j in range(1, 4):
                if j == p2 or j == i:
                    continue
                for p in range(1, 4):
                    if p == p3 or p == j:
                        continue

                    t = self.recur(i, j, p, k-1) % self.MOD
                    loop_count = (loop_count + t) % self.MOD

        return loop_count % self.MOD

    def numOfWays(self, n: int) -> int:
        self.init(n)
        return self.recur(0, 0, 0, n)


g = Solution()
n = 497
print(g.numOfWays_ref(n))
print(g.numOfWays(n))
