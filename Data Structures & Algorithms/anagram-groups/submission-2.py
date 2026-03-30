class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bitches = defaultdict(list)

        for elem in strs:
            eelm = ''.join(sorted(elem))
            bitches[eelm].append(elem)
        
        return list(bitches.values())