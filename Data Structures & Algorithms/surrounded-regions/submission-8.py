class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        queue = deque()

        for row in range(m):
            for col in range(n):
                if (row == 0 or row == m-1) and board[row][col] == 'O':
                    queue.append((row,col))
                    board[row][col] = 'T'
                if (col == 0 or col == n-1) and board[row][col] == 'O':
                    queue.append((row,col))
                    board[row][col] = 'T'
        # I am doing this using multi source bfs. I assume it can be done via
        # multi source iterative dfs the same way. What about 
        # recursive dfs and union find.
        while queue:
            row,col = queue.popleft()

            neighbors = [(row+1,col),(row,col+1),(row-1,col),(row,col-1)]

            for nbr in neighbors:
                r,c = nbr
                if (0<=r<m and 0<=c<n and board[r][c] == 'O'):
                    board[r][c] = 'T'
                    queue.append((r,c))
        
        # All border islands have been marked T. Now convert all inner islands to 'X'
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'T':
                    board[row][col] = 'O'





                
