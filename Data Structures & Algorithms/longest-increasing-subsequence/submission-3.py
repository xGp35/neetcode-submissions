class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        # helper(i, prev_i) = longest increasing subsequence I can build
        # from index i onward, given that the previously selected element 
        # was nums[prev_i].
        def helper(i, prev_i):
            if i == n: return 0

            if (i,prev_i) in memo: return memo[(i,prev_i)]

            dont_take = helper(i+1, prev_i)

            take = float('-inf')
            if prev_i == -1 or nums[i] > nums[prev_i]:
                take = 1 + helper(i+1, i)

            memo[(i,prev_i)] = max(take, dont_take)
            return memo[(i,prev_i)]
        
        return helper(0,-1)


                
