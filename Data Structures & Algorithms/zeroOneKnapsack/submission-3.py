class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = len(profit), capacity

        dp = [[0]*(n+1) for _ in range(m)]

        for row in range(m):
            dp[row][0] = 0
        for col in range(n+1):
            if col - weight[0] >= 0:
                dp[0][col] = profit[0]
        

        for i in range(1,m):
            for W in range(1,n+1): # W is the current capacity we are considering
                
                # decision to skip ith element
                skip = dp[i-1][W]

                # decision to take it
                include = 0   # initialize to zero becz we may decide to skip it
                remainingCapacity = W - weight[i]
                if remainingCapacity >= 0:
                    include = profit[i] + dp[i-1][remainingCapacity]
                
                dp[i][W] = max(skip, include)
        
        return dp[m-1][n]


        
