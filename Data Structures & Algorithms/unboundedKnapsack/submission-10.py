class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # bestSum Way - bottomup
        n = len(profit)
        dp = [0]*(capacity+1)

        for W in range(1, capacity+1):
            for i in range(n):
                remainder = W - weight[i]
                if remainder >= 0:
                    dp[W] = max(dp[W], profit[i] + dp[remainder])
        
        return dp[capacity]
        

