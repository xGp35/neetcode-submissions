class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        return sorted(s) == sorted(t)