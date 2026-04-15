class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        count = 0
        visited = set()
        for row in range(m):
            for col in range(n):
                if (row,col) not in visited and grid[row][col] == "1":
                    self.explore(row, col, visited, grid, m, n)
                    count += 1
        
        return count
        
    def explore(self, row, col, visited, grid, m, n):
        #dfs_explore
        stack = [(row, col)]
        dirs = [(1,0), (0,1), (-1, 0), (0, -1)]

        while stack:
            row, col = stack.pop()
            #neighbors = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]

            for dr, dc  in dirs:
                r, c = row + dr, col + dc
                if (0 <= r < m and
                    0 <= c < n and
                    grid[r][c] == '1' and
                    (r,c) not in visited
                ):
                    visited.add((r,c))
                    stack.append((r,c))




