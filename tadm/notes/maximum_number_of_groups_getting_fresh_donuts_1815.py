# https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/
from functools import lru_cache


class Solution:
    def __init__(self):
        self.batch_size = 0
        self.groups = []
        self.max_happy_group_num = 0
        self.memo = {}
        self.path = []
        self.n = 0
        self.remains = []

    def init(self, batchSize: int, groups: list[int]):
        self.batch_size = batchSize
        self.groups = groups
        self.max_happy_group_num = 0
        self.memo = {}
        self.n = len(groups)
        self.path = [0] * self.n
        self.remains = groups.copy()

    def get_candidates(self):
        return self.remains

    @lru_cache(None)
    def backtrack(self, k: int, acc: int, leftover: int):
        if k == self.n:
            if acc > self.max_happy_group_num:
                self.max_happy_group_num = acc
            return

        k = k + 1
        candidates = self.get_candidates()
        for i in range(len(candidates)):
            c = candidates[i]
            if c == 0:
                continue

            if leftover == 0:
                t_acc = acc + 1
            else:
                t_acc = acc

            # left donuts more than this group of people
            if leftover >= c:
                t_leftover = leftover - c
            else:
                # the number of needed donuts
                need = (c - leftover)
                if self.batch_size >= need:
                    t_leftover = self.batch_size - need
                else:
                    remain = need % self.batch_size
                    if remain == 0:
                        t_leftover = 0
                    else:
                        t_leftover = self.batch_size - remain

            self.remains[i] = 0
            self.backtrack(k, t_acc, t_leftover)
            self.remains[i] = c
        return

    def maxHappyGroups(self, batchSize: int, groups: list[int]) -> int:
        self.init(batchSize, groups)
        self.backtrack(0, 0, 0)
        return self.max_happy_group_num

    # Recursive function to find the
    # maximum number of groups that
    # will receive fresh donuts
    def dfs(self, V, left, K):

        # Store the result for the
        # current state
        q = 0

        # Store the key and check
        # if it is present in the
        # hashmap
        v = [str(int) for int in V]
        key = ",".join(v)

        key += str(left)

        # If already calculated
        if key in self.memo:
            return self.memo[key]

        # If left is 0
        elif left == 0:

            # Traverse the array []arr
            for i in range(1, K):
                if V[i] > 0:
                    # Decrement arr[i]
                    V[i] -= 1

                    # Update the maximum
                    # number of groups
                    q = max(q, 1 + self.dfs(V, K - i, K))

                    # Increment arr[i] by 1
                    V[i] += 1

        # Otherwise, traverse the given
        # array []arr
        else:
            for i in range(1, K):
                if V[i] > 0:
                    # Decrement arr[i]
                    V[i] -= 1

                    if i <= left:
                        nleft = left - i
                    else:
                        nleft = K + left - i

                    # Update the maximum
                    # number of groups
                    q = max(q, self.dfs(V, nleft, K))

                    # Increment arr[i] by 1
                    V[i] += 1

        # Memoize the result and
        # return it
        if key in self.memo:
            self.memo[key] = q
        else:
            self.memo[key] = q

        return q

    def maxGroups(self, K, arr):
        self.init(K, arr)

        # Stores count of remainder by K
        V = [0] * (K)

        # Traverse the array []arr
        for x in range(len(arr)):
            V[arr[x] % K] += 1

        # Hashmap to memoize the results
        memo = {}

        # Store the maximum number
        # of groups
        ans = V[0] + self.dfs(V, 0, K)

        # Return the answer
        return ans

g = Solution()
batch_size = 4
groups = [1,3,2,5,2,2,1,6]
g = Solution()
print(g.maxGroups(batch_size, groups))
print(g.maxHappyGroups(batch_size, groups))
batch_size = 6
groups = [369205928,981877451,947462486,899465743,737778942,573732515,520226542,824581298,571789442,251943251,70139785,778962318,43379662,90924712,142825931,182207697,178834435,978165687]
g = Solution()
print(g.maxGroups(batch_size, groups))
print(g.maxHappyGroups(batch_size, groups))
batch_size = 7
groups = [2,7,5,2,3,2,6,5,3,6,2,3,7,2,2,5,4,6,6,4,7,5,6,1,6,2,6,6,2,5]
g = Solution()
print(g.maxGroups(batch_size, groups))
print(g.maxHappyGroups(batch_size, groups))
batch_size = 2
groups = [903816625,722750145,75648842,89371973,932091758]
g = Solution()
print(g.maxGroups(batch_size, groups))
print(g.maxHappyGroups(batch_size, groups))
