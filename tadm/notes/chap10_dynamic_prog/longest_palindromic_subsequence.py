import collections


# https://www.youtube.com/watch?v=Tw1k46ywN6E
# Longest Palindromic Subsequence using Dynamic Programming
class Solution:
    def find_palin_subsequence(self, s: str, start: int, end: int, lookup):
        if start > end:
            return 0
        if (end-start) == 0:
            return 1

        key = str(start) + '-' + str(end)
        if key in lookup:
            return lookup[key]
        else:
            if s[start] == s[end]:
                lookup[key] = 2 + self.find_palin_subsequence(s, start+1, end-1, lookup)
            else:
                lookup[key] = max(self.find_palin_subsequence(s, start+1, end, lookup), self.find_palin_subsequence(s, start, end-1, lookup))

            return lookup[key]


g = Solution()
string = "ABBDCACB"
lookup = collections.defaultdict(list)
# BCACB
print(g.find_palin_subsequence(string, 0, len(string)-1, lookup))
