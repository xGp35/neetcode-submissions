class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # find all occurences of the first letter. 
        # then start dfs from all of them
        # mark each letter visited when starting dfses from them
        # Then unmark them
        m, n = len(board), len(board[0])
        
        def dfs(i, row, col):
            if i == len(word):
                return True
            if not (0 <= row < m and 0 <= col < n and word[i] == board[row][col]):
                return False
            
            temp = board[row][col]
            board[row][col] = "-1"

            neighbors = [(row+1, col),(row, col+1),(row-1,col),(row, col-1)]

            for nbr in neighbors:
                r,c = nbr
                # if word exists the n dfs will return true
                if dfs(i+1, r,c):
                    return True
            board[row][col] = temp
            return False
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    if dfs(0, row, col):
                        return True
        return False
 