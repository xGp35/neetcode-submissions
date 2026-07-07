class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return max(nums)

        house_set1 = nums[:n-1]
        house_set2 = nums[1:]

        def helper(numbers):
            rob1, rob2 = 0, 0

            for num in numbers:
                newRob = max(rob1+num, rob2)
                rob1 = rob2
                rob2 = newRob
            
            return rob2

        return max(helper(house_set1), helper(house_set2))




        
            
