class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        subsets, curSet = [], []

        def helper(i, curSet, targetSum):
            if targetSum == 0:
                subsets.append(curSet.copy())
                return
            
            if i >= len(nums) or targetSum < 0:
                return 
            
            curSet.append(nums[i])
            helper(i+1, curSet, targetSum - nums[i])
            curSet.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(i+1, curSet, targetSum)

        helper(0, curSet, target)
        return subsets