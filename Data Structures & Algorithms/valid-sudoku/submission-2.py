class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowset = set()
            for j in range(9):
                if board[i][j] in rowset and board[i][j] != '.':
                    return False
                rowset.add(board[i][j])
        
        for j in range(9):
            colset = set()
            for i in range(9):
                if board[i][j] in colset and board[i][j] != '.':
                    return False
                colset.add(board[i][j])
        
        for rowoffset in range(0,9,3):
            for coloffset in range(0,9,3):
                boxset = set()
                for i in range(rowoffset, rowoffset+3):
                    for j in range(coloffset, coloffset+3):
                        if board[i][j] in boxset and board[i][j] != '.':
                            return False
                        boxset.add(board[i][j])
        
        return True
        