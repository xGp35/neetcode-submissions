class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)

        for cap in range(capacity+1):
            for i in range(len(weight)):
                if weight[i] <= cap:
                    dp[cap] = max(dp[cap], profit[i] + dp[cap-weight[i]])
        
        return dp[capacity]