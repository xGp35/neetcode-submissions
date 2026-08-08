class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        negDiag = set()
        posDiag = set()
        
        board = [['.']*n for _ in range(n)]
        result = []
        
        def helper(r):
            if r == n: # Add to board to the result
                newBoard = ["".join(row) for row in board]
                result.append(newBoard)
                return

            for c in range(n):
                if c in colSet or r+c in posDiag or r-c in negDiag:
                    continue
                colSet.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'

                helper(r+1)

                colSet.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = '.'
        
        helper(0)
        return result

