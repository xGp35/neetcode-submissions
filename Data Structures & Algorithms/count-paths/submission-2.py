class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1]*n for _ in range(m)]

        def helper(i,j):
            if i == m or j == n: return 0
            if memo[i][j] != -1: return memo[i][j]
            if i == m-1 or j == n-1: 
                memo[i][j] = 1
                return 1

            memo[i][j] = helper(i+1,j) + helper(i, j+1)

            return memo[i][j]
        
        return helper(0,0)