class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid_time = [[2147000000]*n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    self.explore((row, col), grid, grid_time, m ,n)
        
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and grid_time[row][col] == 2147000000:
                    return -1

        max_time = 0
        for row in range(m):
            for col in range(n):
                if grid_time[row][col] == 2147000000: continue
                else:
                    max_time = max(max_time, grid_time[row][col])
        
        return max_time

    def explore(self, node, grid, grid_time, m, n):
        queue = deque([node])
        visited = {node}
        row, col = node
        time = 0
        grid_time[row][col] = time

        while queue:
            for _ in range(len(queue)):
                node= queue.popleft()
                row, col = node

                neighbors = [(row+1, col),(row, col+1),(row-1, col),(row, col-1)]
                for nbr in neighbors:
                    r, c = nbr
                    if (0 <= r < m and
                        0 <= c < n and
                        grid[r][c] == 1 and
                        nbr not in visited
                    ):
                        grid_time[r][c] = min(grid_time[r][c], time + 1)
                        visited.add(nbr)
                        queue.append(nbr)
            time += 1