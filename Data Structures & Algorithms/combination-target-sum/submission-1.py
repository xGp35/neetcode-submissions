class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets, currSet = [], []
        currSum = 0

        def helper(i, currSet, currSum):          
            if currSum == target:
                subsets.append(currSet.copy())
                return

            if  i >= len(nums) or currSum > target:
                return
            
            # decide to take nums[i]
            currSet.append(nums[i])
            helper(i, currSet, currSum + nums[i])
            currSet.pop()

            # decide to not take nums[i]
            helper(i+1, currSet, currSum)


        helper(0, currSet, currSum)
        return subsets
