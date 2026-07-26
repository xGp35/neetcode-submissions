class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = {}
        def helper(i,j):
            if j == n: return 1
            if i == m: return 0

            if (i, j) in memo: return memo[(i,j)]

            ways = 0

            if s[i] == t[j]:
                ways += helper(i+1, j+1)
            ways += helper(i+1, j)

            memo[(i,j)] = ways
            return ways
        
        return helper(0,0)
