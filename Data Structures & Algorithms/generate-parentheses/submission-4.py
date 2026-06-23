class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        currSet = []
        openB, closeB = 0, 0
        result = []
        def helper(currSet, openB, closeB):
            if openB > n or openB < closeB:
                return

            if openB == n and openB == closeB:
                result.append(''.join(currSet))
                return
            
            # Decision to add '('
            currSet.append('(')
            helper(currSet, openB+1, closeB)
            currSet.pop()

            #Decision to add ')'
            currSet.append(')')
            helper(currSet, openB, closeB+1)
            currSet.pop()
        
        helper(currSet, 0, 0)
        return result
