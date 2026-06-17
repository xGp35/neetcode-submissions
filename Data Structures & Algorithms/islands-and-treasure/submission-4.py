class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n  = len(grid), len(grid[0])
        queue = deque([])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            neighbors = [(row+1, col),(row, col+1),(row-1, col),(row, col -1)]

            for nbr in neighbors:
                r, c = nbr
                if (
                    0 <= r < m and
                    0 <= c < n and
                    grid[r][c] == 2147483647    
                ):
                    grid[r][c] = 1 + grid[row][col]
                    queue.append((r,c))
        
        return