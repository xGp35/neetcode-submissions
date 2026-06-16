class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):  return ""
        if s == t: return t

        window, t_map = {}, {}

        for c in t:
            t_map[c] = 1 + t_map.get(c,0)

        have, need = 0, len(t_map) # important to use t_map instead of t
        left = 0 
        res, resLen = [-1, -1], float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)
            if char in t_map and t_map[char] == window[char]:
                    have += 1
            
            while have == need:
                # count the result len
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                #  remove elements from the left
                left_char = s[left]
                window[left_char] -= 1
                if left_char in t_map and t_map[left_char] > window[left_char]:
                    have -= 1
                left += 1
        l, r = res
        return s[l: r+1] if resLen < float('inf') else ""

