class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                maxOnes = max(maxOnes, count)
            elif num == 0:
                count = 0
        
        return maxOnes