class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo: return memo[i]
            if i >= len(nums): return 0

            # On the current house number i:
            profit_if_include = nums[i] + dfs(i+2)
            profit_if_exclude = dfs(i+1)

            memo[i] = max(profit_if_include, profit_if_exclude)
            return memo[i]
        
        return dfs(0)