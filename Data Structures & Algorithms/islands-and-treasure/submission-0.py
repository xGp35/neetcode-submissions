class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    self.explore((row, col), grid, m, n)
        return
    
    def explore(self, node, grid, m, n):
        visited = {node}
        queue = deque([(node, 0)])
        while queue:
            node, depth = queue.popleft()
            row, col = node
            neighbors = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]
            for nbr in neighbors:
                r,c = nbr
                if (0<= r < m and  
                    0<= c < n and 
                    grid[r][c] != -1 and
                    nbr not in visited
                ):
                    visited.add(nbr)
                    grid[r][c] = min(grid[r][c], depth + 1)
                    queue.append((nbr, depth + 1))
        