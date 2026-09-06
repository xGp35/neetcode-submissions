class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        def helper(l, r):
            nonlocal start 
            nonlocal end
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > (end-start+1):
                    start = l
                    end = r
                l-=1
                r+=1
        
        for i in range(len(s)):
            helper(i,i)
            helper(i,i+1)
        
        return s[start:end+1]