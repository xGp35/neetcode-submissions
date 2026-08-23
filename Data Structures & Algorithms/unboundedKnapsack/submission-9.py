class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = len(profit), capacity

        dp = [[0]*(n+1) for _ in range(m+1)]

        # Fill the first column
        for i in range(m+1):
            dp[i][0] = 0
        # Fill the first row
        for W in range(n+1):
            dp[0][W] = 0

        for i in range(1, m+1): # i = 1 means object 0, so we have to use profit[i-1] and weight[i-1] due to initialization this issue comes
            for W in range(1, n+1):
                #skip
                skip = dp[i-1][W]

                #take
                include = 0 # Use float('-inf') if you have -ve profits
                remainingCapacity = W - weight[i-1]
                if remainingCapacity >= 0:
                    include = profit[i-1] + dp[i][remainingCapacity]

                dp[i][W] = max(include, skip)

        return dp[m][n]


        # # bestSum Way
        # n = len(profit)
        # memo = {}

        # def dfs(target): # target is capacity
        #     if target in memo: return memo[target]
        #     if target < 0: return None
        #     if target == 0: return 0

        #     maxP = 0
        #     for i in range(n):
        #         remainder = target - weight[i]
        #         remainderResult = dfs(remainder)
        #         if remainderResult is not None:
        #             maxP = max(maxP, profit[i] + remainderResult)
            
        #     memo[target] = maxP
        #     return maxP
        
        # return dfs(capacity)

