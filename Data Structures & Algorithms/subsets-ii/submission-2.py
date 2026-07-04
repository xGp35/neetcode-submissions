class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        currSet, subsets = [], []
        nums.sort()

        def helper(i):
            if i >= len(nums):
                subsets.append(currSet.copy())
                return

            # Decision to take nums[i]
            currSet.append(nums[i])
            helper(i+1)
            currSet.pop()

            # Decision to NOT take nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1)
        
        helper(0)
        return subsets