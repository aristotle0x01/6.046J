from collections import defaultdict


# https://leetcode.com/problems/implement-strstr/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ln = len(needle)
        lh = len(haystack)
        if ln == 0:
            return 0
        if lh == 0 or lh < ln:
            return -1

        h_map = defaultdict(list)
        h_map[needle] = needle

        i = 0
        k = i+ln
        while k <= lh:
            sub = haystack[i:k]
            if sub in h_map and sub == needle:
                return i
            else:
                i += 1
                k = i+ln

        return -1


g = Solution()
print(g.strStr("abc", "b"))