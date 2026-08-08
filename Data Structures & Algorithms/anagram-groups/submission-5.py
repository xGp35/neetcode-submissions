class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)

        for elem in strs:
            eelm = "".join(sorted(elem))
            word_dict[eelm].append(elem)
        
        result = []

        for val in word_dict.values():
            result.append(val)
        
        return result