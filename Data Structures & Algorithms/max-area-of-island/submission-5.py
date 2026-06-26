class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        visited = set()
        max_size = 0
        m, n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_size = max(max_size, self.explore((row, col), visited, grid, m, n))
        
        return max_size
    
    def explore(self, node, visited, grid, m, n):
        stack = [node]
        visited.add(node)
        size = 0

        while stack:
            row, col = stack.pop()
            size += 1
            neighbors = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]

            for nbr in neighbors:
                r,c = nbr
                if(
                    0 <= r < m and
                    0 <= c < n and
                    grid[r][c] == 1 and
                    nbr not in visited
                ):
                    visited.add(nbr)
                    stack.append(nbr)
        return size













                    