import collections

# https://www.youtube.com/watch?v=Tw1k46ywN6E
# Optimal Binary Search Trees
import sys


class Solution:
    def do_sum(self, freq: [], start: int, end: int):
        sum_ = 0
        for i in range(start, end + 1):
            sum_ += freq[i]
        return sum_

    def find_optimal_bst_inner(self, freq: [], start: int, end: int, lookup):
        if start > end:
            return 0

        n = len(freq)
        if start >= n or end >= n or start < 0 or end < 0:
            return 0

        if start == end:
            return freq[start]

        key = str(start) + '_' + str(end)
        if key in lookup:
            return lookup[key]

        # cost(i, j) = min{cost(i, r-1), cost(r+1, j)} + sum(i, j)
        sum_ = self.do_sum(freq, start, end)
        optimal_cost = sys.maxsize
        for r in range(start, end + 1):
            root = r
            tmp = self.find_optimal_bst_inner(freq, start, root - 1, lookup) \
                  + self.find_optimal_bst_inner(freq, root + 1, end, lookup) + sum_
            if tmp < optimal_cost:
                optimal_cost = tmp

            lookup[key] = optimal_cost
        return optimal_cost

    def find_optimal_bst(self, freq: [], n: int):
        lookup = collections.defaultdict(list)
        return self.find_optimal_bst_inner(freq, 0, n - 1, lookup)


g = Solution()
lookup = collections.defaultdict(list)
frequency = [25, 10, 20]
print(g.find_optimal_bst(frequency, len(frequency)))
