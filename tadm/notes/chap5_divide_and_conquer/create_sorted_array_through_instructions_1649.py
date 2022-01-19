# https://leetcode.com/problems/create-sorted-array-through-instructions/
class Solution:
    # divide and conquer
    # key observations:
    #     1) using d&c, the cost on the right side would omit which incurred by the left
    #        so we just preserve each insertion cost, accumulate when needed. add up finally
    #        instructions[i] -> cost_list[i, left_cost, right_cost]
    #     2) during the merge phase, both left and right side can be sorted, it doesn't matter its original index
    #        only the possible left side cost needs be added to the right side. besides, the search process can be
    #        speed up due to the sorted property
    #
    # there are binary indexed tree solution: https://www.wikiwand.com/en/Fenwick_tree
    #                                         https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees
    def createSortedArray(self, instructions: list[int]) -> int:
        def dv_conquer(cost_list: [], start: int, end: int):
            if start >= end:
                return

            mid = start + (end - start) // 2
            dv_conquer(cost_list, start, mid)
            dv_conquer(cost_list, mid+1, end)
            k, p = start, start
            for j in range(mid+1, end+1):
                while k <= mid and cost_list[k][0] < cost_list[j][0]:
                    k = k + 1
                while p <= mid and cost_list[p][0] <= cost_list[j][0]:
                    p = p + 1
                cost_list[j][1] += k - start
                cost_list[j][2] += mid - p + 1

            k, p = start, mid+1
            tmp = []
            while k <= mid and p <= end:
                if cost_list[k][0] < cost_list[p][0]:
                    tmp.append(cost_list[k])
                    k += 1
                else:
                    tmp.append(cost_list[p])
                    p += 1
            while k <= mid:
                tmp.append(cost_list[k])
                k += 1
            while p <= end:
                tmp.append(cost_list[p])
                p += 1
            for i in range(start, end+1):
                cost_list[i] = tmp[i-start]

        if len(instructions) == 0:
            return 0

        cost_list = []
        for v in instructions:
            cost_list.append([v, 0, 0])

        dv_conquer(cost_list, 0, len(instructions)-1)
        cost = 0
        for lst in cost_list:
            m = min(lst[1], lst[2])
            cost += m

        return cost % (10 ** 9 + 7)

    # binary search
    def createSortedArray_binary(self, instructions: list[int]) -> int:
        def get_less_cost(sorted_list: list[int], v: int):
            low = 0
            high = len(sorted_list) - 1
            mark = -1
            while low <= high:
                mid = low + (high - low) // 2
                if sorted_list[mid] >= v:
                    mark = mid
                    high = mid - 1
                else:
                    low = mid + 1

            if mark >= 0:
                cost = (mark - 1) - 0 + 1
            else:
                cost = len(sorted_list)

            return cost

        def get_greater_cost(sorted_list: list[int], v: int):
            low = 0
            high = len(sorted_list) - 1
            mark = -1
            while low <= high:
                mid = low + (high - low) // 2
                if sorted_list[mid] <= v:
                    mark = mid
                    low = mid + 1
                else:
                    high = mid - 1

            return (len(sorted_list) - 1) - (mark + 1) + 1

        if len(instructions) == 0:
            return 0

        # for all elements already processed, maintain a sorted list
        # then for each of the remaining elements, do a binary search on the sorted list
        sorted_instructions = [instructions[0]]
        cost = 0
        for i in range(1, len(instructions)):
            vi = instructions[i]

            low_cost = get_less_cost(sorted_instructions, vi)
            high_cost = get_greater_cost(sorted_instructions, vi)
            cost = cost + min(high_cost, low_cost)

            if low_cost == 0:
                sorted_instructions.insert(0, instructions[i])
            elif high_cost == 0:
                sorted_instructions.append(instructions[i])
            else:
                sorted_instructions.insert(low_cost, instructions[i])

        return cost % (10 ** 9 + 7)

    # reference impl
    def createSortedArray_ref(self, A):
        m = max(A)
        c = [0] * (m + 1)

        def update(x):
            while (x <= m):
                c[x] += 1
                x += x & -x

        def get(x):
            res = 0
            while (x > 0):
                res += c[x]
                x -= x & -x
            return res

        res = 0
        for i, a in enumerate(A):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10 ** 9 + 7)

    # brute force
    def createSortedArray0(self, instructions: list[int]) -> int:
        if len(instructions) == 0:
            return 0

        # for all elements already processed, maintain a sorted list
        # then for each of the remaining elements, do a binary search on the sorted list
        sorted_instructions = [instructions[0]]
        cost = 0
        for i in range(1, len(instructions)):
            vi = instructions[i]
            
            low_cost = 0
            for k in range(len(sorted_instructions)):
                if sorted_instructions[k] < vi:
                    low_cost += 1
                else:
                    break
            high_cost = 0
            for k in range(len(sorted_instructions)-1, -1, -1):
                if sorted_instructions[k] > vi:
                    high_cost += 1
                else:
                    break

            cost = cost + min(high_cost, low_cost)

            if low_cost == 0:
                sorted_instructions.insert(0, instructions[i])
            elif high_cost == 0:
                sorted_instructions.append(instructions[i])
            else:
                sorted_instructions.insert(low_cost, instructions[i])

        return cost % (10**9 + 7)

g = Solution()
a = []
print(g.createSortedArray(a))
print(g.createSortedArray_ref(a))