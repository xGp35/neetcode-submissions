class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        for row in range(m):
            for col in range(n):
                if ((row == 0 or col ==0 or
                    row == m-1 or col == n-1) and 
                    board[row][col] == 'O'
                ):
                    self.dfs_explore(row,col, board, m, n)

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'V':
                    board[row][col] = 'O'

    def dfs_explore(self, row,col, board, m, n):
        if board[row][col] in ('V', 'X'):
            return

        board[row][col] = 'V'

        neighbors = [(row+1, col),(row, col+1),(row-1, col),(row, col-1)]

        for nbr in neighbors:
            r,c = nbr
            if (0 <= r < m and 
                0 <= c < n and
                board[r][c] == "O"
            ):
                self.dfs_explore(r, c, board, m, n)
        
