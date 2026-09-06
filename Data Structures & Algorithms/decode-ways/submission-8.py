class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i in memo: return memo[i]
            if i == len(s):
                return 1
            
            ways = 0
            # 2 choices - take 1 char or take 2 char
            #take 1 char
            if s[i] != '0':
                ways += dfs(i+1) # number of ways of decoding the subsequent string
                # not we don't need a plus one because we are not adding a new way, we are just adding a new string to the existing number of ways.
            
            # take 2 char
            if (i+1 < len(s) and 10 <= int(s[i:i+2]) <=26):
                ways += dfs(i+2)
            
            memo[i] = ways
            return ways
        
        return dfs(0)