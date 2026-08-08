class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        longest = 0
        char_map = defaultdict(int)

        for r in range(len(s)):
            char_map[s[r]] += 1
            maxf = max(char_map.values())
            while (r-l+1) - maxf > k:
                char_map[s[l]] -= 1
                l += 1
            longest = max(longest, (r-l+1))
        
        return longest