class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False

        m, n = len(s1), len(s2)

        prevRow = [False]*(n+1)
        prevRow[n] = True

        for j in range(n-1, -1,-1):
            if s3[m+j] == s2[j]:
                prevRow[j] = prevRow[j+1]

        for i in range(m-1,-1,-1):
            curRow = [False] * (n+1)
            for j in range(n,-1,-1):
                k = i+j
                if i < m and s3[k] == s1[i]:
                    curRow[j] = prevRow[j]
                if j < n and s3[k] == s2[j]:
                    curRow[j] |= curRow[j+1]
            prevRow = curRow
                    
        return prevRow[0]
