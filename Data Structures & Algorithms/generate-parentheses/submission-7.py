class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subsets = []
        curSet = []

        def dfs(i, curSet, openB, closeB):
            if closeB > openB: return
            if openB > n: return
            if i == 2*n:
                subsets.append(''.join(curSet))
                return
            
            
            # Add open bracket and DFS
            curSet.append('(')
            dfs(i+1, curSet, openB + 1, closeB)
            curSet.pop()

            # Add close bracket and DFS
            curSet.append(')')
            dfs(i+1, curSet, openB, closeB + 1)
            curSet.pop()
        
        dfs(0, curSet, 0, 0)
        return subsets