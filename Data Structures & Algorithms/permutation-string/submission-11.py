from string import ascii_lowercase
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        anagram = s1
        s = s2
        k = len(anagram)

        anagram_dict = {c:0 for c in ascii_lowercase}
        count_dict = {c:0 for c in ascii_lowercase}

        for i in range(len(anagram)):
            anagram_dict[anagram[i]] += 1
            count_dict[s[i]] += 1
        
        matches = 0
        for c in ascii_lowercase:
            if anagram_dict[c] == count_dict[c]:
                matches += 1
        
        left = 0
        for right in range(k, len(s)):
            if matches == 26: return True

            count_dict[s[right]] += 1
            if count_dict[s[right]] == anagram_dict[s[right]]:
                matches += 1
            elif count_dict[s[right]] == 1 + anagram_dict[s[right]]:
                matches -= 1
            
            count_dict[s[left]] -= 1
            if count_dict[s[left]] == anagram_dict[s[left]]:
                matches += 1
            elif count_dict[s[left]] + 1  == anagram_dict[s[left]]:
                matches -= 1
            left +=1
        return matches == 26