class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2): return False
        memo = {}
        def helper(i,j):
            k = i+j
            if i == len(s1):
                if s2[j:] == s3[k:]:
                    return True
                else:
                    return False
            if j == len(s2):
                if s1[i:] == s3[k:]:
                    return True
                else:
                    return False
            
            
            if (i,j) in memo: return memo[(i,j)]

            ans = False
            
            if s3[k] == s1[i]:
                ans = ans or helper(i + 1, j)

            if s3[k] == s2[j]:
                ans = ans or helper(i, j + 1)
            
            memo[(i,j)] = ans
            return memo[(i,j)]
        
        return helper(0,0)