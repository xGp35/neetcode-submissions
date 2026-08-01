class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        setSum1 = 0
        Total = sum(nums)
        if Total % 2 == 1: return False
        memo = {}
        
        def helper(i, setSum1):
            if (i, setSum1) in memo: return memo[(i, setSum1)]
            if i == len(nums):
                return setSum1 == Total/2

            # add nums[i] in set 1
            take = helper(i+1, setSum1 + nums[i])
            
            # add nums[i] in set 2 - don't add in set1
            skip = helper(i+1, setSum1)

            memo [(i, setSum1)] = (take or skip)
            return memo [(i, setSum1)]
        
        return helper(0, 0)