class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        
        for W in range(1, amount+1):
            for coin in coins:
                remainder = W - coin
                if remainder >= 0:
                    dp[W] = min(dp[W], 1 + dp[remainder])
        print(dp)
        return dp[amount] if dp[amount] < float('inf') else -1
