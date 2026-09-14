class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, targ):
            if (i, targ) in memo: return memo[(i,targ)]
            if i == len(nums) and targ == 0: return 1
            if i >= len(nums): return 0

            ways = 0
            # add nums[i]
            ways += dfs(i+1, targ - nums[i])

            # subtract nums[i]
            ways += dfs(i+1, targ + nums[i])

            memo[(i,targ)] = ways
            return ways
        return dfs(0, target)
            