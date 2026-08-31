class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = []
        curSet = []

        def helper(i, targetSum):
            if targetSum == 0: return [[]]
            if targetSum < 0: return []

            result = []

            for j in range(i, len(nums)):
                remainder = targetSum - nums[j]
                remainderWays = helper(j, remainder)
                for possibility in remainderWays:
                    result.append([nums[j]] + possibility)
            
            return result
        
        return helper(0, target)
            