import sys
from collections import defaultdict

# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/
#
# as of 'abc', 'ab' can be seen as a sub problem, only here it may not be sub-optimal
# but its result can be cached to speed up the overall calculation
#
# left and right fingers can be represented by '0' and '1'
# so this is a problem of 2^n, where n is length of the input string
from functools import lru_cache


class Solution1320:
    # Constructor
    def __init__(self):
        self.cache_map = defaultdict(list)
        self.word = ''
        self.min_distance = sys.maxsize
        self.pos_map = {}
        for c in range(65, 91):
            i = (c - 65) // 6
            j = (c - 65) % 6
            self.pos_map[chr(c)] = (i, j)

    def initialize(self, word: str):
        self.cache_map = defaultdict(list)
        self.word = word
        self.min_distance = sys.maxsize

    def cost(self, p: str):
        if p in self.cache_map:
            return self.cache_map[p]

        left_appeared = False
        right_appeared = False
        distance = 0
        left_last = None
        right_last = None
        for i in range(0, len(p)):
            current = self.pos_map[self.word[i]]
            if left_last is None and right_last is None:
                distance = distance + 0
            else:
                if p[i] == '0':
                    if not left_appeared:
                        distance = distance + 0
                    else:
                        distance = distance + abs(current[0]-left_last[0]) + abs(current[1]-left_last[1])
                else:
                    if not right_appeared:
                        distance = distance + 0
                    else:
                        distance = distance + abs(current[0]-right_last[0]) + abs(current[1]-right_last[1])

            if p[i] == '0':
                left_appeared = True
                left_last = self.pos_map[self.word[i]]
            else:
                right_appeared = True
                right_last = self.pos_map[self.word[i]]

        self.cache_map[p] = distance

        return distance

    def backtrack(self, path: str, k: int):
        if k == 0:
            c = self.cost(path)
            if c < self.min_distance:
                self.min_distance = c
            return

        k = k - 1
        tmp = ['0', '1']
        p = path
        for t in tmp:
            path = t + path
            self.backtrack(path, k)
            path = p

        return

    def minimumDistance(self, word: str) -> int:
        self.initialize(word)
        p = ''
        self.backtrack(p, len(word))
        return self.min_distance


s = Solution1320()
print(s.minimumDistance('HAPPY'))
print(s.minimumDistance('CAKE'))
print(s.minimumDistance('OPVUWZLCKTDPSUKGHA'))
# print(s.minimumDistance('OPVUWZLCKTDPSUKGHAXIDWHLZFKNBDZEWHBSURTVCADUGTSDMCLDBTAGFWDPGXZBVARNTDICHCUJLNFBQOBTDWMGILXPSFWVGYBZVFFKQIDTOVFAPVNSQJULMVIERWAOXCKXBRI'))
