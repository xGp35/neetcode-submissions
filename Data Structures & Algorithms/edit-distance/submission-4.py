class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)
        memo = [[float('inf')]*cols for _ in range(rows)]
        def helper(i, j):
            if i == len(word1): return cols - j
            if j == len(word2): return rows - i
            
            if memo[i][j] < float('inf'): return memo[i][j]
            
            if word1[i] == word2[j]:
                memo[i][j] = helper(i+1, j+1)
            else:
                memo[i][j] = 1 + min(helper(i+1, j+1), helper(i, j+1), helper(i+1, j))

            return memo[i][j]
        
        return helper(0,0)
