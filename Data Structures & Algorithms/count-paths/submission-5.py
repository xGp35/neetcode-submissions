class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prevRow = [1]*(n+1)
        prevRow[n] = 0

        for i in range(m-2, -1, -1):
            curRow = [0]*(n+1)
            for j in range(n-1, -1, -1):
                curRow[j] = prevRow[j] + curRow[j+1]
            prevRow = curRow

        return prevRow[0]