# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# Example 1:
#
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        def merge_count_smaller_rights(lst: [], start: int, end: int):
            if start >= end:
                return

            mid = start + (end - start) // 2
            merge_count_smaller_rights(lst, start, mid)
            merge_count_smaller_rights(lst, mid+1, end)

            # only right side would affect count in the left side
            k = mid+1
            for j in range(start, mid+1):
                while k <= end and lst[k][0] < lst[j][0]:
                    k += 1
                t = lst[j][1] + (k - (mid+1))
                lst[j] = (lst[j][0], t, lst[j][2])

            tmp = []
            k, p = start, mid+1
            while k <= mid and p <= end:
                if lst[k][0] < lst[p][0]:
                    tmp.append(lst[k])
                    k += 1
                else:
                    tmp.append(lst[p])
                    p += 1
            while k <= mid:
                tmp.append(lst[k])
                k += 1
            while p <= end:
                tmp.append(lst[p])
                p += 1
            for t in range(start, end+1):
                lst[t] = tmp[t-start]
            return

        smaller_rights = []
        smaller_rights_count = 0
        for i in range(len(nums)):
            smaller_rights.append((nums[i], smaller_rights_count, i))

        merge_count_smaller_rights(smaller_rights, 0, len(smaller_rights)-1)

        # sort by original index, then output count
        sorted_array = sorted(smaller_rights, key=lambda x: x[2])
        counts = []
        for (_, count, _) in sorted_array:
            counts.append(count)

        return counts

    def countSmaller_ref(self, nums):
        rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res += getSum(rank[x] - 1),
            update(rank[x])
        return res[::-1]

g = Solution()
a = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
print(g.countSmaller(a))
print(g.countSmaller_ref(a))
# [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]