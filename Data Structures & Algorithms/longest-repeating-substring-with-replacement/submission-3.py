class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counter = defaultdict(int)
        max_len = 0
        left, right = 0, 0

        for right in range(len(s)):
            char_counter[s[right]] += 1
            while (right - left + 1) - char_counter[self.maxfreq(char_counter)] > k:
                char_counter[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
    def maxfreq(self, input_dict):
        return max(input_dict, key = input_dict.get)


        