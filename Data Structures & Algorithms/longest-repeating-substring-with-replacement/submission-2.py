class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict = {}
        l, r = 0 , 0

        for elem in s:
            count_dict[elem] = 0
        
        def most_freq():
            max_key = max(count_dict, key=count_dict.get)
            return max_key
        
        windowlen = 0
        maxlen = 0

        while r < len(s):
            count_dict[s[r]] += 1
            windowlen += 1
            while windowlen - count_dict[most_freq()] > k:
                count_dict[s[l]] -= 1
                l += 1
                windowlen -= 1
            maxlen = max(maxlen, windowlen)
            r += 1
        return maxlen
        
