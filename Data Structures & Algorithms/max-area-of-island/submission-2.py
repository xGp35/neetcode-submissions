class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def explore(node):
            if node in visited: return 0

            visited.add(node)
            size = 1

            row, col = node
            
            for dr, dc in dirs:
                r,c = row + dr, col + dc
                if(
                    0 <= r < m and
                    0 <= c < n and
                    grid[r][c] == 1 and
                    (r,c) not in visited
                ):
                    size = size + explore((r,c))
            
            return size

        for row in range(m):
            for col in range(n):
                if (row, col) not in visited and grid[row][col] == 1:
                    max_area = max(max_area, explore((row,col)))

        return max_area
