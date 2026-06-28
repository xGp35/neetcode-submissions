class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2: return 0

        memo = [0]*(len(cost)+1)

        memo[0] = 0
        memo[1] = 0

        for i in range(2, len(cost)+1):
            memo[i] = min(cost[i-1] + memo[i-1], cost[i-2] + memo[i-2])

        return memo[len(cost)]
# def minCostClimbingStairs(self, cost: List[int]) -> int:
#     n = len(cost)
#     if n < 2: return 0

#     memo = [float('inf')]*(n+1)

#     memo[0] = 0
#     memo[1] = 0

#     for i in range(2, n+1):
#         memo[i] = min(cost[i-1] + memo[i-1], cost[i-2] + memo[i-2])

#     return memo[n]
