class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        m, n = len(s1), len(s2)

        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[m][n] = True

        for i in range(m,-1,-1):
            for j in range(n, -1,-1):
                k = i+j
                if i < m and s1[i] == s3[k]:
                    dp[i][j] = dp[i+1][j] # We dont need |= beacuse ans is false above, so |= always gives same result as =
                if j < n and s2[j] == s3[k]:
                    dp[i][j] |= dp[i][j+1]
                
        return dp[0][0]