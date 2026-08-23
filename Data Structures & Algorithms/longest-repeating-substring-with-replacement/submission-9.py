class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        longest = 0
        freq_map = defaultdict(int)

        for r in range(len(s)):
            char_r = s[r]
            freq_map[char_r] += 1
            maxf = max(freq_map.values())

            while r-l+1 - maxf > k:
                char_l = s[l]
                freq_map[char_l] -= 1
                l += 1
            if (r-l+1) > longest:
                longest = r-l+1

        return longest
