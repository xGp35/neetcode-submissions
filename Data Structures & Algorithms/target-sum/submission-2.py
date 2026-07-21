class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        curSum = 0
        memo = {}

        def helper(i,curSum):
            ways = 0
        
            if i == len(nums):
                if curSum == target: return 1
                else: return 0
            
            if (i,curSum) in memo: return memo[(i,curSum)]

            #decide to (+) ith number
            ways += helper(i+1, curSum + nums[i])

            #decide to (-) ith number
            ways += helper(i+1, curSum - nums[i])

            memo[(i,curSum)] = ways
            return ways

        return helper(0, curSum)
