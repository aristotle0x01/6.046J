# https://leetcode.com/problems/number-of-squareful-arrays/
from collections import Counter


class Solution:
    def __init__(self):
        self.nums = []
        self.count = 0
        self.valid_squares = {}
        self.valid_permutations = {}
        self.cnt = None

    def init(self, nums: list[int]):
        self.nums = nums
        self.count = 0
        self.valid_permutations = {}
        self.cnt = Counter(nums)

        # 14 * 14 = 196
        # 15 * 15 = 225
        # 0 <= nums[i] + nums[i + 1] <= 218
        self.valid_squares = {}
        for i in range(15):
            self.valid_squares[i*i] = 1

    # Constraints:
    #   1 <= nums.length <= 12
    #   0 <= nums[i] <= 109
    def numSquarefulPerms(self, nums: list[int]) -> int:
        self.init(nums)
        path = []
        remains = self.cnt.copy()
        self.backtrack(path, remains, 0, len(nums))
        return self.count

    def find_candidates(self, path: [], remains, k: int, n: int):
        if k == 1:
            return self.nums
        else:
            last_element = path[-1]
            a = []
            for r in remains:
                if remains[r] > 0 and (last_element + r) in self.valid_squares:
                    a.append(r)
            return a

    def backtrack(self, path: [], remains: [], k: int, n: int):
        if k > n:
            return

        if k == n:
            repeats = ''
            for p in path:
                repeats = repeats + '_' + str(p)
            if repeats not in self.valid_permutations:
                self.valid_permutations[repeats] = 1
                self.count += 1
            return

        k = k + 1
        candidates = self.find_candidates(path, remains, k, n)
        for c in candidates:
            path.append(c)
            remains[c] -= 1
            self.backtrack(path, remains, k, n)
            remains[c] += 1
            del path[-1]


g = Solution()
s = [1,17,8]
print(g.numSquarefulPerms(s))