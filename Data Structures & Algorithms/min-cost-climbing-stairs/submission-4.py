class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mc0 = 0
        mc1 = 0
        for i in range(2,n+1):
            newCost = min(mc1 + cost[i-1], mc0 + cost[i-2])
            mc0 = mc1
            mc1 = newCost
    
        return mc1