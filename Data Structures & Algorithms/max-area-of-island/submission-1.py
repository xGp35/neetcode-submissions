class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        
        def explore(node):
            if node in visited: return 0

            visited.add(node)
            size = 1

            row, col = node
            neighbors = [(row+1, col),(row, col+1),(row-1, col),(row, col-1)]

            for nbr in neighbors:
                r,c = nbr
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
