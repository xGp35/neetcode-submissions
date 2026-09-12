from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        prevRow = [i for i in range(n+1)]
        
        for i in range(m):
            curRow = [-1]*(n+1)
            curRow[0] = i+1
            for j in range(n):
                if word1[i] == word2[j]:
                    curRow[j+1] = prevRow[j]
                else:
                    curRow[j+1] = 1 + min(prevRow[j+1], curRow[j], prevRow[j])
            prevRow = curRow
        return prevRow[n]