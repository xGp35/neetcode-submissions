class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subsets, curSet = [], []

        def helper(curSet, openB, closeB):
            if openB > n or closeB > openB:
                return
            
            if openB == n and openB == closeB:
                subsets.append(''.join(curSet))
                return
            
            # Decision to add '('
            curSet.append('(')
            helper(curSet, openB + 1, closeB)
            curSet.pop()

            # Decision to add ')'
            curSet.append(')')
            helper(curSet, openB, closeB +1)
            curSet.pop()
        
        helper(curSet, 0, 0)
        return subsets