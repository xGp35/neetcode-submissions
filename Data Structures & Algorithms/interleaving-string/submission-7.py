class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False
        
        m, n = len(s1), len(s2)
        memo = [[False]*(n+1) for _ in range(m+1)]

        memo[m][n] = True

        for i in range(m, -1,-1):
            for j in range(n,-1,-1):
                if i < m and s3[i+j] == s1[i]:
                    memo[i][j] = memo[i+1][j]

                if j < n and s3[i+j] == s2[j]:
                    memo[i][j] = memo[i][j+1]
        
        return memo[0][0]