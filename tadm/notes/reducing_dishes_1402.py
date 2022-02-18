# https://leetcode.com/problems/reducing-dishes/
class Solution:
    # Constructor
    def __init__(self):
        self.finished = False
        self.optimal = 0
        self.optimal_way = []
        self.satisfaction = []

    def initialize(self, satisfaction: list[int]):
        self.finished = False
        self.optimal = 0
        self.optimal_way = []
        self.satisfaction = satisfaction

    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        if len(satisfaction) == 0:
            return 0

        stats = sorted(satisfaction)
        if stats[-1] <= 0:
            return 0

        v = self.max_stats(stats, len(stats)-1, 0, 0, 0)
        if v > 0:
            return v
        else:
            return 0

    # like 'Optimal Binary Search Trees'
    #
    # do it the greedy way:
    # 1. sort original array
    # 2. pop the largest, then process the remaining array recursively, increase the popped values with each recursion
    # 3. do the accumulation along the way
    #
    # it is easy to prove the correctness of greedy algo
    #
    # 'acc' per recursion accumulation satisfaction value
    # 'optimal' max of 'acc' during recursion
    # 'sums' array elements sum
    def max_stats(self, satisfaction: list[int], end: int, acc: int, sums: int, optimal: int) -> int:
        if acc > optimal:
            optimal = acc

        if end < 0:
            return optimal

        sums = satisfaction[end] + sums
        new_acc = acc + sums

        return self.max_stats(satisfaction, end-1, new_acc, sums, optimal)

    def backtrack(self, path: [], k: int, n: int, pre_sum: int):
        if k > n:
            return

        if k == n:
            if pre_sum > self.optimal:
                self.optimal = pre_sum
            return

        k = k + 1
        for i in range(2):
            if i == 0:
                path.append(self.satisfaction[k-1])
                old = pre_sum
                pre_sum = pre_sum + len(path) * path[-1]
                self.backtrack(path, k, n, pre_sum)
                del path[-1]
                pre_sum = old
            else:
                self.backtrack(path, k, n, pre_sum)

        return

    def maxSatisfaction2(self, satisfaction: list[int]) -> int:
        if len(satisfaction) == 0:
            return 0

        stats = sorted(satisfaction)
        self.initialize(stats)

        path = []
        self.backtrack(path, 0, len(stats), 0)

        return self.optimal

    def maxSatisfaction3(self, satisfaction: list[int]) -> int:
        if len(satisfaction) == 0:
            return 0

        stats = sorted(satisfaction)
        if stats[-1] <= 0:
            return 0

        # observe that when abs of sum of negative elements is larger than sum of positive elements
        # we should stop
        positive_element_sum = 0
        negative_element_sum = 0
        result = []
        for i in range(len(stats)-1, -1, -1):
            if stats[i] >= 0:
                positive_element_sum += stats[i]
            else:
                negative_element_sum += stats[i]

            result.insert(0, stats[i])

            if abs(negative_element_sum) > positive_element_sum:
                del result[0]
                break

            if abs(negative_element_sum) == positive_element_sum:
                break

        tmp = 0
        for i in range(len(result)):
            tmp = tmp + (i+1) * result[i]
        return tmp


g = Solution()
sats = [34,-27,-49,-6,65,70,72,-37,-57,92,-72,36,6,-91,18,61,77,-91,5,64,-16,5,20,-60,-94,-15,-23,-10,-61,27,89,38,46,57,33,94,-79,43,-67,-73,-39,72,-52,13,65,-82,26,69,67]
# sats = [-1,-8,0,5,-7]
print(g.maxSatisfaction3(sats))
print(g.maxSatisfaction(sats))