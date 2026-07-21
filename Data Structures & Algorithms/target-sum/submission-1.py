class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways, curSum = 0, 0

        def helper(i,curSum):
            nonlocal ways
        
            if i == len(nums):
                if curSum == target:
                    ways += 1
                return

            #decide to (+) ith number
            helper(i+1, curSum + nums[i])

            #decide to (-) ith number
            helper(i+1, curSum - nums[i])

        helper(0, curSum)
        return ways
