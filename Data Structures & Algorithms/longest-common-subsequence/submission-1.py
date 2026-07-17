class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        memo = [[-1]*n for i in range(m)]

        def helper(i,j):
            if i == m or j == n:
                return 0
            
            if memo[i][j] != -1: # if present in cache, return from cache
                return memo[i][j]
            
            if text1[i] == text2[j]:
                memo[i][j] = 1 + helper(i+1, j+1)
            else:
                memo[i][j] = max(helper(i+1,j), helper(i,j+1))
            
            return memo[i][j]
        
        return helper(0,0)