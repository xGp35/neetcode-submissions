class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        l = 0
        maxf = 0
        max_len = 0

        for r in range(len(s)):
            freq_map[s[r]] += 1
            maxf = max(maxf, freq_map[s[r]])

            while (r-l+1) - maxf > k:
                freq_map[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            
        return max_len


        