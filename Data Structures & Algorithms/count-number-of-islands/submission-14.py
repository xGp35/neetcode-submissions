class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def explore(node):
            row,col = node
            grid[row][col] = '0'

            deltas = [(1,0),(0,1),(-1,0),(0,-1)]

            for dr,dc in deltas:
                r, c = row + dr, col + dc
                if (0<=r<m and 0<=c<n and grid[r][c] == '1'):
                    explore((r,c))
        
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    explore((row,col))
                    count += 1
        
        return count

