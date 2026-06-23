class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()
        currSet = []

        def dfs(i, node, currSet):
            if node in visited: return
            row, col = node

            if(row < 0 or col < 0 or row >= m or col >= n or board[row][col] != word[i]):
                return
            
            if i == len(word) - 1:
                return True

            visited.add(node)

            neighbors = [(row+1, col),(row, col+1),(row-1, col),(row, col-1)]

            currSet.append(word[i])
            for nbr in neighbors:
                if dfs(i + 1, nbr, currSet):
                    return True
            currSet.pop()
            visited.remove(node)

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    if dfs(0, (row, col), currSet):
                        return True
        
        return False

