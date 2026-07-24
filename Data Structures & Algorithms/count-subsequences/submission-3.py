class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t): return 0

        m, n = len(s), len(t)
        memo = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            memo[i][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    memo[i][j] += memo[i+1][j+1]
                memo[i][j] += memo[i+1][j]
        
        return memo[0][0]
        