class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        #dp = [[0]*(n+1) for _ in range(m+1)]
        # Space Optimized, you can just replace
        # dp[i] with prevRow and dp[i+1] with curRow
        # For ex - dp[i][j] = prevRow[j], dp[i+1][j+1] = curRow[j+1] 
        prevRow = [0]*(n+1)

        for i in range(m):
            curRow = [0]*(n+1)
            for j in range(n):
                if text1[i] == text2[j]:
                    curRow[j+1] = 1 + prevRow[j]
                else:
                    curRow[j+1] = max(curRow[j], prevRow[j+1])
            prevRow = curRow
        
        return prevRow[n]