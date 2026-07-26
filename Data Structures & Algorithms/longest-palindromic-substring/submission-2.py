class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        start, end = 0, 0

        def helper(l, r):
            nonlocal longest, start, end
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if (r-l+1 > longest):
                    longest = r-l+1
                    start, end = l, r
                l -= 1
                r += 1

        for i in range(len(s)):
            helper(i,i)
            helper(i,i+1)

        return s[start:end+1]