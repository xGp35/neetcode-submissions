class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False
        memo = {}
        def helper(i,j):
            k = i+j
            if k == len(s3): return True

            if (i,j) in memo: return memo[(i,j)]

            ans = False

            if i < len(s1) and s3[k] == s1[i]:
                ans = helper(i+1, j)
            if j < len(s2) and s3[k] == s2[j]:
                ans = ans or helper(i, j+1)
            
            memo[(i,j)] = ans
            return ans
        
        return helper(0,0)