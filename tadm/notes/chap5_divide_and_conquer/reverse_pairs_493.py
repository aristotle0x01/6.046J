# https://leetcode.com/problems/reverse-pairs/
class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_sort_it(lst: [], start: int, end: int):
            if start >= end:
                return 0

            mid = start + (end - start) // 2
            count = merge_sort_it(lst, start, mid) + merge_sort_it(lst, mid+1, end)

            k = end
            for j in range(mid, start-1, -1):
                while k > mid and lst[j] <= 2*lst[k]:
                    k = k - 1
                count += k - mid

            tmp = []
            k, p = start, mid+1
            while k <= mid and p <= end:
                if lst[k] < lst[p]:
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

            return count

        return merge_sort_it(nums, 0, len(nums)-1)

    def reversePairs_ref(self, nums):
        return 0

g = Solution()
a = [2,4,3,5,1]
print(g.reversePairs(a))
print(g.reversePairs_ref(a))
# [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]