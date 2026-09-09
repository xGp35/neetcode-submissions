class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for W in range(coin, amount+1):
                dp[W] = dp[W] + dp[W-coin]
        return dp[amount]