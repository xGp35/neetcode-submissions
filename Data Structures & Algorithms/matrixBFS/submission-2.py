class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        # TODO: Do this by modifying the grid.
        m, n = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[m-1][n-1] != 0: return -1
        start = (0,0)
        depth = 0
        queue = deque([(start,depth)])
        grid[0][0] = 1

        while queue:
            curr, depth = queue.popleft()
            row, col = curr # What are practical disadvantages of doing it this way?
            if row == m-1 and col == n-1:
                return depth

            neighbors = [(row+1, col),(row, col+1),(row-1,col),(row, col-1)]
            for nbr in neighbors:
                r, c = nbr
                if (
                    0 <= r < m and
                    0 <= c < n and
                    grid[r][c] == 0
                ):
                    queue.append((nbr,depth+1))
                    grid[r][c] = 1
        
        return -1

