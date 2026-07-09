class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [0] * len(nums)

        memo[0] = nums[0]
        curSum = memo[0]

        for i in range(1, len(nums)):
            memo[i] = max(memo[i-1]+nums[i], nums[i])
        
        return max(memo)