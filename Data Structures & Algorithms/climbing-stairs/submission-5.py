class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)

        dp[0] = 1 # Num of ways to climb 0 steps -> 1 (don't climb at all)
        dp[1] = 1 # Num of ways to climb 1 step -> 1 (take 1 step)
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        