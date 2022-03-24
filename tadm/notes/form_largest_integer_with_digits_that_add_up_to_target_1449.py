# https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/
import time


class Solution:
    # Constructor
    def __init__(self):
        self.maximum = ''
        self.cost = []
        self.target = 0
        self.map = {}
        self.candidates = []
        self.acc = ''
        self.target_map = {}

    def initialize(self, cost: list[int], target: int):
        self.maximum = ''
        self.cost = cost
        self.target = target
        self.map = {}
        for i in range(len(cost)):
            c = cost[i]
            # preserve largest index for each unique cost
            self.map[c] = i + 1

        self.candidates = []
        for k in self.map.keys():
            self.candidates.append((k, self.map[k]))
        self.acc = ''
        self.target_map = {}

    def get_larger(self, left, right):
        if len(left) < len(right):
            return right
        if len(left) > len(right):
            return left
        if str(left) > right:
            return left
        return right

    def recur(self, acc: str, obj: int):
        if obj == 0:
            self.maximum = self.get_larger(acc, self.maximum)
            return

        t_acc = acc
        for c, i in self.candidates:
            acc = t_acc

            t_obj = obj - c
            if t_obj < 0:
                continue

            acc = acc + str(i)

            if t_obj == 0:
                self.recur(acc, 0)
            else:
                if t_obj in self.target_map:
                    left = self.target_map[t_obj]
                else:
                    old = self.maximum

                    self.maximum = ''
                    self.recur('', t_obj)
                    left = self.maximum
                    self.target_map[t_obj] = left

                    self.maximum = old

                # means there is not a permutation for t_obj, just ignore it
                if left == '':
                    continue
                else:
                    t = acc + left
                    self.recur(t, 0)

        return

    def largestNumber(self, cost_list: list[int], target_obj: int) -> str:
        self.initialize(cost_list, target_obj)
        self.recur('', target_obj)
        if self.maximum == '':
            return '0'
        return self.maximum


g = Solution()
cost = [4,3,2,5,6,7,2,5,5]
target = 9
start_time = time.time()
print(g.largestNumber(cost, target))
print("--- %s seconds ---" % (time.time() - start_time))

g = Solution()
cost = [7,6,5,5,5,6,8,7,8]
target = 12
start_time = time.time()
print(g.largestNumber(cost, target))
print("--- %s seconds ---" % (time.time() - start_time))

g = Solution()
cost = [70,84,55,63,74,44,27,76,34]
target = 659
start_time = time.time()
print(g.largestNumber(cost, target))
print("--- %s seconds ---" % (time.time() - start_time))


g = Solution()
cost = [2,4,6,2,4,6,4,4,4]
target = 5
start_time = time.time()
print(g.largestNumber(cost, target))
print("--- %s seconds ---" % (time.time() - start_time))