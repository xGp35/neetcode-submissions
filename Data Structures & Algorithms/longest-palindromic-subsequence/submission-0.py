class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s_rev = s[::-1]

        n = len(s)

        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n):
            for j in range(n):
                if s[i] == s_rev[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[n][n]
