class Solution:
    def climbStairs(self, n: int) -> int:
        
        way1 = 1
        way2 = 1
        for _ in range(1,n):
            newWay = way1 + way2
            way1 = way2
            way2= newWay
        
        return way2