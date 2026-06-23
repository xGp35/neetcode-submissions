class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()

        def dfs(i, node):
            if node in visited: return
            row, col = node

            if(row < 0 or col < 0 or row >= m or col >= n or board[row][col] != word[i]):
                return
            
            if i == len(word) - 1:
                return True

            # This '#' marking is an alternative to maintaining visited.add(node)
            temp = board[row][col]
            board[row][col] = '#'
            found = False

            neighbors = [(row+1, col),(row, col+1),(row-1, col),(row, col-1)]

            for nbr in neighbors:
                if dfs(i + 1, nbr):
                    found = True
                    break
            board[row][col] = temp
            return found

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    if dfs(0, (row, col)):
                        return True
        
        return False

