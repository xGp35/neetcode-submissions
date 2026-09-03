class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        negDiagSet = set() # row - col
        posDiagSet = set() # row + col

        board = [["."]*n for _ in range(n)]
        result = []

        def dfs(row):
            if row == n:
                result.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                # check if queen can be placed here. Basically check all validaity conditions wrt to colSet, leftDset and rightDiagSet, ie. if it is present in any of these sets, then we don't need to place a queen here and start dfs. so we imediately return at that point.
                if(col not in colSet and 
                row - col not in negDiagSet and 
                row + col not in posDiagSet):
                    temp = board[row][col]
                    #put a queen here
                    board[row][col] = 'Q'

                    colSet.add(col)
                    negDiagSet.add(row - col)
                    posDiagSet.add(row + col)

                    dfs(row + 1)

                    colSet.remove(col)
                    negDiagSet.remove(row - col)
                    posDiagSet.remove(row + col)

                    board[row][col] = temp

        dfs(0)
        return result   

            