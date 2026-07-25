class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        # Create the SCS matrix -> scs = len(a) + len(b) - lcs(a,b) 
        for i in range(m+1):
            for j in range(n+1):
                dp[i][j] = i + j - dp[i][j]
                #print(f"dp[{i}][{j}] is {dp[i][j]}") 
        
        res = []
        i, j = m, n
        while i > 0 and j > 0:
            if dp[i-1][j] < dp[i][j]:
                res.append(str1[i-1])
                i = i - 1
            elif dp[i][j-1] < dp[i][j]:
                res.append(str2[j-1])
                j = j - 1
            else:
                res.append(str1[i-1])
                i = i - 1
                j = j - 1
        
        prefix = ""
        if j > 0:
            prefix = str2[:j]
        if i > 0:
            prefix = str1[:i]
        
        #print(prefix)
        
        res.reverse()
        result = prefix + "".join(res)
        return result
