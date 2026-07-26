class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)

        def helper(houses):
            rob0, rob1 = 0, 0

            for num in houses:
                newRob = max(num+rob0, rob1)
                rob0 = rob1
                rob1 = newRob
            
            return rob1
        
        return max(helper(nums[:len(nums)-1]), helper(nums[1:]))
        

            