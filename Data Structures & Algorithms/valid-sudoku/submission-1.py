class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row-wise validation
        for i in range(9):
            row_set = set()
            for j in range(9):
                if board[i][j] in row_set and board[i][j] != '.':
                    return False
                else:
                    row_set.add(board[i][j])
        #Column-wise validation
        for i in range(9):
            column_set = set()
            for j in range(9):
                if board[j][i] in column_set and board[j][i] != '.':
                    return False
                else:
                    column_set.add(board[j][i])
        #Box wise validation
        for row_offset in range(0,9,3):
            for col_offset in range(0,9,3):
                box_set = set()
                for i in range(row_offset, row_offset+3):
                    for j in range(col_offset, col_offset+3):
                        if board[i][j] in box_set and board[i][j] != '.':
                            return False
                        else:
                            box_set.add(board[i][j])
        return True