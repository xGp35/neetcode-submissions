class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = largest = nums[0]

        for i, elem in enumerate(nums[1:]):
            curr_sum += elem
            if elem > curr_sum:
                curr_sum = elem
                
            if curr_sum > largest:
                largest = curr_sum

        return largest