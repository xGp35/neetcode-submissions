class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        targetSum = total/2
        
        memo = {}
        def dfs(i, target):
            if (i,target) in memo: return memo[(i,target)]
            if target == 0: return True
            if target < 0 or i >= len(nums): return False
            
            #take or skip
            memo[(i,target)]= dfs(i+1, target-nums[i]) or dfs(i+1, target)
            return memo[(i,target)]
        
        return dfs(0, targetSum)

            
