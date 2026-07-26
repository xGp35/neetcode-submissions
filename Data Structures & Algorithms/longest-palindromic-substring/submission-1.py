class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        longestSub = ""
        for i in range(len(s)):
            
            # For odd length palindromes
            l, r = i, i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if (r-l+1 > longest):
                    longest = r-l+1
                    longestSub = s[l:r+1]
                l -= 1
                r += 1   

            # For even length palindromes
            l, r = i, i+1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                if (r-l+1 > longest):
                    longest = r-l+1
                    longestSub = s[l:r+1]
                l -= 1
                r += 1     

        return longestSub