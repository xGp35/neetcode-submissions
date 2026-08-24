class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Number of distinct combinations - not minimum
        n = len(coins)
        memo = {}
        def dfs(i, target):
            if (i, target) in memo: return memo[(i,target)]
            if i == n or target < 0: return 0
            if target == 0: return 1

            ways = 0
            # dual branch
            ways += dfs(i, target - coins[i]) # take
            ways += dfs(i+1, target) #skip

            # This is unbounded knapsack so skip can go i+1, take stays at i
            # see the first page of copy dsa4, the full recursion tree.
 
            memo[(i,target)] = ways
            return ways
        
        return dfs(0, amount)

            


