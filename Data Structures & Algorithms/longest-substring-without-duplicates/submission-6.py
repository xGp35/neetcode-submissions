class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        # mp will store the last index where each character appeared.
        # When a character repeats, the earliest valid starting point moves to
        # one position after previous occurence.
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r-l +1)
        
        return res
