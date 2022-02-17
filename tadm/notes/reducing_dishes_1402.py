# https://leetcode.com/problems/reducing-dishes/
class Solution:
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


g = Solution()
sats = [-1,-8,0,5,-9]
print(g.maxSatisfaction(sats))
