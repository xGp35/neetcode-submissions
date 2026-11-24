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
        minL, minR = 0, len(s) - 1 # These are the correct indices which will give the minimum length substring of s which has all chars of t.

        for r in range(len(s)):
            # add s[r] is two stepped here
            char_r = s[r] # just renaming
            s_map[char_r] += 1 # Step 1 - increasing dict count by 1
            if s_map[char_r] == t_map[char_r]: have += 1 # Step2 - if by adding current element to s_map our entry of s_map and t_map for that char becomes equal -> we increase the have.

# This while loop will run only on 2 conditions:
# 1. First time our s_map will get all chars required (the frequency of each charcter need not be necessarity equal to t_map, it can be greater)
# 2. After first match complete, it encounters a charcter that was present in t_map but also in s_map, so now the count of that character has increased.

# note - if a charcter of t_map comes in s_map more frequently than in t_map, before atleast all characters have satisfied their quotas, then the whiel loop will not run.

            while have == need and (s[l] not in t_map or s_map[s[l]] > t_map[s[l]]) :
                s_map[s[l]] -= 1
                l+=1
            if have == need and (r-l+1) < (minR-minL +1):
                minL, minR = l, r
        
        return s[minL:minR+1] if have == need else ""
