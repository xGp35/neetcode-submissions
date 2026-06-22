class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, currSet = [], []
        

        def helper(i, nums, currSet, subsets):
            if i >= len(nums):
                subsets.append(currSet.copy())
                return
            
            # decision to include nums[i]
            currSet.append(nums[i])
            helper(i+1, nums, currSet, subsets)
            currSet.pop()

            # decision NOT to include nums[i]
            helper(i+1, nums, currSet, subsets)


        helper(0, nums, currSet, subsets)
        return subsets