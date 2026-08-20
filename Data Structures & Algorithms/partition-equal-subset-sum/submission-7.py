class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        target = total / 2
        memo = {}
        def helper(i, targ):
            if (i,targ) in memo: return memo[(i,targ)]
            if targ == 0: return True
            if targ < 0 or i >= len(nums): return False

            ans = False
            #take
            ans |= helper(i+1, targ-nums[i])

            #skip
            ans |= helper(i+1, targ)

            memo[(i,targ)] = ans
            return ans
        
        return helper(0, target)

            
