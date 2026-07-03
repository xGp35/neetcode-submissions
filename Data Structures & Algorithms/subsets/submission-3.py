class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, currSet = [], []
        

        def helper(i):
            if i >= len(nums):
                subsets.append(currSet.copy())
                return
            
            # decision to include nums[i]
            currSet.append(nums[i])
            helper(i+1)
            currSet.pop()

            # decision NOT to include nums[i]
            helper(i+1)


        helper(0)
        return subsets