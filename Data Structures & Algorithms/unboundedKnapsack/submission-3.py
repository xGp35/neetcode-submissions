class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        memo = {}

        def dfs(i, capacity):
            if (i, capacity) in memo: return memo[(i,capacity)]
            if i == n: return 0

            skip = dfs(i+1, capacity)
            include = 0
            remainingCapacity = capacity - weight[i]
            if remainingCapacity >= 0:
                include = profit[i] + dfs(i, remainingCapacity)
            
            memo[(i,capacity)] = max(skip,include)
            return max(skip,include)
        
        return dfs(0, capacity)
