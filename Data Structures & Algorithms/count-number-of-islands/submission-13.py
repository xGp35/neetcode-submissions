class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def explore(node):
            row,col = node
            grid[row][col] = '0'

            neighbors = [(row+1,col),(row, col+1),(row-1,col),(row,col-1)]

            for nbr in neighbors:
                r, c = nbr
                if (0<=r<m and 0<=c<n and grid[r][c] == '1'):
                    explore(nbr)
        
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    explore((row,col))
                    count += 1
        
        return count

