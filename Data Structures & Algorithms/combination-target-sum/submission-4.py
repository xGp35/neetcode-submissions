class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = []
        curSet = []

        def helper(i, curSet, targetSum):
            if targetSum == 0:
                subsets.append(curSet.copy())
                return
            if targetSum < 0 or i >= len(nums):
                return
            
            # take nums[i]
            curSet.append(nums[i])
            helper(i, curSet, targetSum - nums[i])
            curSet.pop()

            # skip nums[i]
            helper(i+1, curSet, targetSum)

        helper(0, curSet, target)
        return subsets
            