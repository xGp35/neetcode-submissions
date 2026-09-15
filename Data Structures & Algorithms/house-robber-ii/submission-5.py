class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        nums1 = nums[0:n-1]
        nums2 = nums[1:n]

        def helper(numbers):
            rob1 = 0
            rob2 = 0

            for num in numbers:
                newRob = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = newRob

            return rob2
        
        return max(helper(nums1), helper(nums2))