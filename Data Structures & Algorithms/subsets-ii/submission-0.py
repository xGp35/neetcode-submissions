class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []
        nums.sort()

        def helper(i , curSet):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return False
            
            curSet.append(nums[i])
            helper(i+1, curSet)
            curSet.pop()

            while i < len(nums) -1 and nums[i] == nums[i+1]:
                i+=1
            helper(i+1, curSet)
        
        helper(0, curSet)
        return subsets
