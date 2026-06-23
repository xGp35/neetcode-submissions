class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets, currSet = [], []
        currSum = 0
        candidates.sort()

        def helper(i, currSet, currSum):
            if currSum == target:
                subsets.append(currSet.copy())
                return
            
            if i >= len(candidates) or currSum > target:
                return

            currSet.append(candidates[i])
            helper(i+1, currSet, currSum + candidates[i])
            currSet.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            helper(i+1, currSet, currSum)
        
        helper(0, currSet, currSum)
        return subsets