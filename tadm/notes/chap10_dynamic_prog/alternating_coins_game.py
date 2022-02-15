import collections

# https://www.youtube.com/watch?v=Tw1k46ywN6E
# Coin In a Line Game Problem


class Solution:
    def find_optimal_inner(self, coins: [], start: int, end: int, lookup):
        if start >= end:
            return 0

        key = str(start) + '_' + str(end)
        if key in lookup:
            return lookup[key]

        # mv(i, j) = max(coins[i] + min{mv(i+2, j), mv(i+1, j-1)},
        #                coins[j] + min{mv(i+1, j-1), mv(i, j-2)})
        left1 = self.find_optimal_inner(coins, start+2, end, lookup)
        left2 = self.find_optimal_inner(coins, start+1, end-1, lookup)
        left = coins[start] + min(left1, left2)
        right1 = self.find_optimal_inner(coins, start+1, end-1, lookup)
        right2 = self.find_optimal_inner(coins, start, end-2, lookup)
        right = coins[end] + min(right1, right2)
        lookup[key] = max(left, right)
        return lookup[key]

    def find_optimal(self, coins: []):
        table = collections.defaultdict(list)
        return self.find_optimal_inner(coins, 0, len(coins)-1, table)


g = Solution()
my_coins = [6, 9, 1, 2]
print(g.find_optimal(my_coins))
