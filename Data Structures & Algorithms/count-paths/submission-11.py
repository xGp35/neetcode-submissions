class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # There are so many variations of this prevRow and nextRow
        # PrevRow could begin from i = n, where all are 0's
        # here i begin prevrow at i = m-1, where al are 1 expcept
        # nth column which is 0
        # My "grid" so to speark is m*(n+1). You don't need to do this
        # I just found this asymetry gave best time in neetcode.
        # You can go with symetric (m+1)*(n+1), where prevRow is all 0s
        # Or symteric m*n where prevRow is all 1's
        # The (m+1)*(n+1) is more finnicky for this problem due to 
        # needing to initalize the curRow[n-1] = 1 for i == m-1.
        # Just do the normal dp, get the dp diagram, then try space optimizations
        # you'll get a lot of idea on what to do
        memo = [[-1]*n for _ in range(m)]
        def dfs(r, c):
            if r == m or c == n: return 0
            if memo[r][c] != -1: return memo[r][c]
            if r ==m-1 and c == n-1: return 1

            memo[r][c] = dfs(r+1,c) + dfs(r,c+1)
            return memo[r][c]

        return dfs(0,0)