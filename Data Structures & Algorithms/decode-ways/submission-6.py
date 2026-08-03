class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}
        def helper(i):
            if i in memo: return memo[i]

            ways = 0
            if s[i] != "0":
                ways += helper(i+1)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += helper(i+2)
            
            memo[i] = ways
            return ways
        
        return helper(0)