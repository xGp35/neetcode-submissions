class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, curSet = [], []
        
        def helper(i):
            subsets.append(curSet.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                curSet.append(nums[j])
                helper(j+1)
                curSet.pop()
        
        helper(0)
        return subsets
