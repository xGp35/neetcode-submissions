class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t): return 0

        m, n = len(s), len(t)
        memo = [[-1]*n for _ in range(m)]
        
        def helper(i,j):
            if j == n:
                return 1
            if i == m:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]

            sum = 0

            if s[i] == t[j]:
                sum += helper(i+1, j+1)
            sum += helper(i+1, j)
            
            memo[i][j] = sum

            return sum
        return helper(0,0)