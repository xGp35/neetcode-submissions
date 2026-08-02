class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Total = sum(nums)
        if Total % 2 == 1: return False
        memo = {}

        def helper(i, sumSet1):
            if (i,sumSet1) in memo: return memo[(i,sumSet1)]
            if i == len(nums):
                return sumSet1 == Total / 2

            # add nums[i] to subset1
            take = helper(i+1, sumSet1 + nums[i])

            # skip nums[i] - imaginarily add to subset2
            skip = helper(i+1, sumSet1)

            memo[(i,sumSet1)] = (take or skip)
            return (take or skip)
        
        return helper(0,0)