class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        freq_map = {}
        longest = 0

        for r in range(len(s)):
            char_r = s[r]
            freq_map[char_r] = 1 + freq_map.get(char_r, 0)

            while len(freq_map) > k:
                char_l = s[l]
                freq_map[char_l] -= 1
                if freq_map[char_l] == 0:
                    del freq_map[char_l]
                l += 1
            
            if (r-l+1) > longest:
                longest = r-l+1
        
        return longest