class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        val0 = 0
        val1 = 0

        for i in range(2,n+1):
            newVal = min(cost[i-1] + val1, cost[i-2] + val0)
            val0 = val1
            val1 = newVal
        
        return val1