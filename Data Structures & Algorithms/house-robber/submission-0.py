class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo: return memo[i]
            if i >= len(nums): return 0
            if i == len(nums) - 1: return nums[i]

            max_total = 0
            
            for j in range(i,len(nums)):
                total = nums[j] + max(dfs(j+2), dfs(j+3))
                max_total = max(max_total, total)

            memo[i] = max_total    

            return max_total
        return dfs(0)