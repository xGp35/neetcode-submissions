class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_dict = dict(Counter(s1))
        s2_dict = defaultdict(int)

        for r in range(len(s2)):
            char_r = s2[r]
            s2_dict[char_r] += 1

            if r - l + 1 > len(s1):
                char_l = s2[l]
                s2_dict[char_l] -= 1
                # If count of that char goes to zero remove it from s2_dict
                if s2_dict[char_l] == 0:
                    s2_dict.pop(char_l)

                l += 1

            if s1_dict == s2_dict:
                return True

        return False
