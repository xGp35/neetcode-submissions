class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Total = sum(nums)
        if Total % 2 == 1: return False
        memo = {}
        # m is target, n is nums

        def helper(i, target):
            if (i, target) in memo: return memo[(i,target)]
            if target < 0 : return False
            if target == 0: return True
            if i == len(nums): return False
        
            # add nums[i] to subset1
            # skip nums[i] - imaginarily add to subset2
            memo[(i,target)] = (
                helper(i+1, target - nums[i]) or
                helper(i+1, target)
            )
            return memo[(i,target)]
        
        return helper(0,Total/2)