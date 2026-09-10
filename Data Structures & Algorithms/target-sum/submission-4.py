class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def helper(i, curSum):
            if i == len(nums):
                if curSum == target: return 1
                else: return 0
            
            if (i, curSum) in memo: return memo[(i, curSum)]

            ways = 0

            # decision to add nums[i]
            ways += helper(i+1, curSum+nums[i])

            # decision to subtract nums[i]
            ways += helper(i+1, curSum-nums[i])

            memo[(i,curSum)] = ways
            return ways
        
        return helper(0,0)