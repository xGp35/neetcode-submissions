class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)

        if l3 != l1 + l2: return False

        memo = {}
        def dfs(i,j):
            if (i, j) in memo: return memo[(i,j)]
            k = i+j
            if i == l1 and j == l2: return True
            
            ans = False
            if i < l1 and s1[i] == s3[k]:
                ans |= dfs(i+1, j)
            if j < l2 and s2[j] == s3[k]:
                ans |= dfs(i, j+1)
            
            memo[(i,j)] = ans
            return ans

        return dfs(0,0)