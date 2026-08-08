class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)

        for s in strs:
            count = [0]*26 # 1 for each of a .... z,
            # this could've been a tuple

            for char in s:
                count[ord(char) - ord('a')] += 1
            
            word_dict[tuple(count)].append(s)
        
        return list(word_dict.values())
