class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        freq_sorted = sorted(freq.items(), key=lambda x:x[0], reverse = True)

        for elem in freq_sorted:
            if elem[1] == 1:
                return elem[0]
        
        return -1
