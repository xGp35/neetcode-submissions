class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        # Just create the LCS table
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        res = []
        i, j = m, n
        # Now we construct the string
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                # if characters are same, take from either
                res.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                res.append(str1[i-1])
                i -= 1
            else:
                res.append(str2[j-1])
                j -= 1
        
        # Add remaining characters from str1 if any
        while i > 0:
            res.append(str1[i-1])
            i -= 1
        # Add remaining characters from str2 if any
        while j > 0:
            res.append(str2[j-1])
            j -= 1
        
        return "".join(res[::-1])
