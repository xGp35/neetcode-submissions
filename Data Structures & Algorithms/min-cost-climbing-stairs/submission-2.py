class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def helper(i):
            if i ==0 or i == 1: return 0
            if i in memo: return memo[i]
            memo[i] = min(helper(i-1) + cost[i-1], helper(i-2) + cost[i-2])
            return memo[i]
        return helper(n)