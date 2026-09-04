class Solution:
    def climbStairs(self, n: int) -> int:
        
        way0 = 1
        way1 = 1
        
        for i in range(2, n+1):
            newWay = way0 + way1
            way0 = way1
            way1 = newWay

        return way1
        