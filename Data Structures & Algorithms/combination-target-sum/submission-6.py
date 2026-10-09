class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # This is a all Sum type solution, not the usual one
        # Get the usual one from previous submissions
        
        def dfs(i, targetSum):
            if targetSum == 0: return [[]]
            if targetSum < 0: return []

            result = []

            for j in range(i, len(nums)):
                remainder = targetSum - nums[j]
                remainderWays = dfs(j, remainder)
                # we use j and not j+1 as we can reuse
                for way in remainderWays:
                    result.append([nums[j]] + way)
            
            return result

        return dfs(0,target)