class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Number of distinct combinations - not minimum
        coins.sort()
        memo = {}
        def dfs(i, target):
            if (i, target) in memo: return memo[(i,target)]
            if target < 0: return 0
            if target == 0: return 1

            ways = 0
            for j in range(i, len(coins)):
                if j>i and coins[j] == coins[i]:
                    continue
                remainder = target - coins[j]
                ways += dfs(j, remainder)
            memo[(i,target)] = ways
            return ways
        
        return dfs(0, amount)

            


