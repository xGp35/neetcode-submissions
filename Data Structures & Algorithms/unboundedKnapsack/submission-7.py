class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # bestSum Way
        n = len(profit)
        memo = {}

        def dfs(target): # target is capacity
            if target in memo: return memo[target]
            if target < 0: return None
            if target == 0: return 0

            maxP = 0
            for i in range(n):
                remainder = target - weight[i]
                remainderResult = dfs(remainder)
                if remainderResult is not None:
                    maxP = max(maxP, profit[i] + remainderResult)
            
            memo[target] = maxP
            return maxP
        
        return dfs(capacity)

