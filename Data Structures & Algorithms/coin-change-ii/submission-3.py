class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m, n = len(coins), amount
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 1 # This is initialized to 1 as we can create amount 0 in 1 way
        # 1st row is all zeros anyways so nothing to do there

        for i in range(1, m+1):
            for W in range(1, n+1):
                # skip
                skip = dp[i-1][W]
                #take
                include = 0
                remainingCapacity = W - coins[i-1]
                if remainingCapacity >= 0:
                    include = dp[i][remainingCapacity] # No of ways to take remaining capacity coins

                dp[i][W] = skip + include # Here its add, in unbounded knapsack it was max
        return dp[m][n]

            


