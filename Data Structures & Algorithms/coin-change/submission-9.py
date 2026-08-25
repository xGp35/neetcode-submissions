class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for W in range(coin, amount+1):
                dp[W] = min(dp[W], 1 + dp[W-coin])
        return dp[amount] if dp[amount] < float('inf') else -1