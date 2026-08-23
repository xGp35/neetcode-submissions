class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        freq_map = defaultdict(int)
        longest = 0

        for r, char_r in enumerate(s):
            freq_map[char_r] += 1

            while len(freq_map) > 2:
                char_l = s[l]
                freq_map[char_l] -= 1
                if freq_map[char_l] == 0:
                    del freq_map[char_l]
                l += 1
            longest = max(longest, r-l+1)

        return longest
