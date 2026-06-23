class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets, currSet = [], []
        currSum = 0
        candidates.sort()

        def helper(i, currSet, currSum):
            if currSum == target:
                subsets.append(currSet.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                if currSum + candidates[j] > target:
                    return
                currSet.append(candidates[j])
                helper(j+1, currSet, currSum + candidates[j])
                currSet.pop()

            
        helper(0, currSet, currSum)
        return subsets