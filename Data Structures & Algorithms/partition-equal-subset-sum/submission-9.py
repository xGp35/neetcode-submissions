class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 == 1: return False

        targetSum = total // 2

        dp = [False]*(targetSum+1)
        dp[0] = True

        for num in nums:
            for W in range(targetSum, num-1, -1):
                dp[W] = dp[W] or dp[W-num]
        
        return dp[targetSum]