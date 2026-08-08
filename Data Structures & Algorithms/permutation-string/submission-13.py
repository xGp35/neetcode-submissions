class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        s1_dict = defaultdict(int)
        for elem in s1:
            s1_dict[elem] += 1
        m = len(s1)
        l = 0
        r = m-1
        current_window_dict = defaultdict(int)
        for i in range(m):
            current_window_dict[s2[i]] += 1

        while r+1 < len(s2):
            if s1_dict == current_window_dict:
                return True
            current_window_dict[s2[l]] -= 1
            if current_window_dict[s2[l]] == 0:
                del current_window_dict[s2[l]]
            current_window_dict[s2[r+1]] += 1
            l += 1
            r += 1
        if s1_dict == current_window_dict:
            return True
        return False
