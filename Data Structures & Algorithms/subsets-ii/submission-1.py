class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []
        nums.sort()

        def helper(i):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return False
            
            curSet.append(nums[i])
            helper(i+1)
            curSet.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1)
        
        helper(0)
        return subsets
