class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        # fixed window
        # slide means l+=1, r+=1
        # set of current elements in window.
        if len(s) < k: return 0

        freq_map = defaultdict(int)
        l = 0
        count = 0

        for i in range(k):
            freq_map[s[i]] += 1
        if len(freq_map) == k: count += 1

        for r in range(k,len(s)):
            freq_map[s[r]] += 1
            freq_map[s[l]] -= 1
            if freq_map[s[l]] == 0: del freq_map[s[l]]
            l += 1

            if len(freq_map) == k: count += 1
        return count