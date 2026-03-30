class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bitches = {}
        for elem in strs:
            eelm = ''.join(sorted(elem))
            if eelm in bitches:
                bitches[eelm].append(elem)
            else:
                bitches[eelm] = [elem]
        result = []
        for k, v in bitches.items():
            result.append(v)
        return result