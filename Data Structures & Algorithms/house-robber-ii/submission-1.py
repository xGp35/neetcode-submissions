class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return max(nums)

        def house_robber(numbers):
            rob1, rob2 = 0, 0

            for num in numbers:
                newRob = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2

        return max(house_robber(nums[1:]), house_robber(nums[:-1]))
        



        
            
