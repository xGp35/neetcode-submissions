class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        t_count = Counter(t)
        s_count = {}

        required = len(t_count)
        formed = 0
        l = 0 

        ans = (float('inf'), None, None)

        for r in range(len(s)):
            char = s[r]
            s_count[char] = s_count.get(char, 0) + 1

            if char in t_count and s_count[char] == t_count[char]:
                formed += 1
            
            while formed == required:
                # update answer
                if r - l + 1 < ans[0]:
                    ans = (r-l+1, l, r+1)
                # shrink window
                left_char = s[l]
                s_count[left_char] -= 1

                if left_char in t_count and s_count[left_char] == t_count[left_char]-1:
                    formed -= 1
                
                l += 1

        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]]




