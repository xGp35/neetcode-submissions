class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = newRob
        
        return rob2