class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        memo = {}

        def helper(i, targ):
            if (i,targ) in memo: return memo[(i,targ)]
            if targ < 0: return float('-inf')
            if i == n: return 0

            maxProfit = 0
            take = profit[i] + helper(i+1, targ-weight[i])
            skip = helper(i+1, targ)
            
            memo[(i,targ)] = max(take,skip)
            return memo[(i,targ)]

        return helper(0, capacity)