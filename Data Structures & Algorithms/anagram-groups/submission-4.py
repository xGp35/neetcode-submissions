class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)

        for elem in strs:
            eelm = "".join(sorted(elem))
            word_dict[eelm].append(elem)
        
        result = []

        for _, val in word_dict.items():
            result.append(val)
        
        return result