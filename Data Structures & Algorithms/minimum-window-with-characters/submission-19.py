class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        l = 0

        t_map = defaultdict(int)
        for char in t:
            t_map[char] += 1
        
        s_map = defaultdict(int)
        have = 0
        need = len(t_map)
        minL, minR = 0, len(s) - 1

        for r in range(len(s)):
            char_r = s[r]
            s_map[char_r] += 1
            if s_map[char_r] == t_map[char_r]: have += 1
            while have == need and (s[l] not in t_map or s_map[s[l]] > t_map[s[l]]) :
                s_map[s[l]] -= 1
                l+=1
            if have == need and (r-l+1) < (minR-minL +1):
                minL, minR = l, r
        
        return s[minL:minR+1] if have == need else ""
