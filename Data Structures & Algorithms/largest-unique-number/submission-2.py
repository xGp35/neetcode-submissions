class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)

        for i in range(1000, -1, -1):
            if freq[i] == 1:
                return i
        
        return -1
