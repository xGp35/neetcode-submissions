class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return max(nums)

        memo = [0]*len(nums)

        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            memo[i] = max(nums[i]+ memo[i-2], memo[i-1])
        
        return memo[-1]