class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)

        def helper(i, curSet):
            if i == n:
                subsets.append(curSet.copy())
                return
            
            # decision to take nums[i]
            curSet.append(nums[i])
            helper(i+1, curSet)
            curSet.pop()

            # decision to not take nums[i]
            helper(i+1, curSet)
        
        helper(0, [])
        return subsets
