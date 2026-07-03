class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, currSet = [], []
        

        def helper(i, nums):
            if i >= len(nums):
                subsets.append(currSet.copy())
                return
            
            # decision to include nums[i]
            currSet.append(nums[i])
            helper(i+1, nums)
            currSet.pop()

            # decision NOT to include nums[i]
            helper(i+1, nums)


        helper(0, nums)
        return subsets