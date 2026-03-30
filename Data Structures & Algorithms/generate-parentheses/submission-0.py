class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s, left, right):
            # If the current string has reached the desired length (2 * n)
            if len(s) == 2*n:
                result.append(s)
                return
            # left is the number of left brackets used so far
            # right is the number of right brackets used so far

            # backtrack means both of these conditions will run but at different times.
            # in one call first if will run, that will have branched subroutines
            # once the branches complte execution, 
            # the execution of the second if block will start
            # That is basically backtracking, 
            # Solution, subroutines execute and control then comes back to orignal routine
            # from which new things again start branching out 

            if left < n:
                backtrack(s+'(', left+1, right)
            if right < left:
                backtrack(s+')', left, right+1)
        
        result = []
        backtrack("", 0, 0)
        return result