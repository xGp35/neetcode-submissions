class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        k = len(s1)
        l = 0

        anagram_dict = {c:0 for c in 'abcdefghijklmnopqrstuvwxyz'} 
        count_dict = {c:0 for c in 'abcdefghijklmnopqrstuvwxyz'}

        for i in range(k):
            anagram_dict[s1[i]] += 1
            count_dict[s2[i]] += 1

        matches = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if anagram_dict[c] == count_dict[c]: matches += 1
        print(matches)
        for r in range(k, len(s2)):
            if matches == 26: return True

            char_r = s2[r]
            count_dict[char_r] += 1

            if anagram_dict[char_r] == count_dict[char_r]:
                matches += 1
            elif anagram_dict[char_r] + 1 == count_dict[char_r]:
                matches -= 1

            char_l = s2[l]
            count_dict[char_l] -= 1

            if anagram_dict[char_l] == count_dict[char_l]:
                matches += 1
            elif anagram_dict[char_l] == count_dict[char_l] + 1:
                matches -= 1
            l+= 1
        print(matches)
        return matches == 26
