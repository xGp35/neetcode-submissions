class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                neighbors = [(row+1, col), (row, col+1), (row-1, col), (row, col-1)]
                for nbr in neighbors:
                    r,c = nbr
                    if(0 <= r < m and
                        0 <= c < n and
                        grid[r][c] == 1
                    ):
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append(nbr)

            time += 1
        
        return -1 if fresh > 0 else time