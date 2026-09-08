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

        prevRow = [1]*(n+1)
        prevRow[n] = 0

        for i in range(m-2, -1, -1):
            curRow = [0]*(n+1)
            for j in range(n-1, -1, -1):
                curRow[j] = prevRow[j] + curRow[j+1]
            prevRow = curRow

        return prevRow[0]