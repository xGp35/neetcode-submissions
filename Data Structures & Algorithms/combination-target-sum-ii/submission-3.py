class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curSet, subsets = [], []
        curSum = 0
        candidates.sort()
        
        def helper(i, curSet, curSum):
            # initial conditions
            if curSum == target:
                subsets.append(curSet.copy())
                return
            
            if i > len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if curSum + candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                curSet.append(candidates[j])
                helper(j+1, curSet, curSum + candidates[j])
                curSet.pop()
        
        helper(0, curSet, curSum)
        return subsets