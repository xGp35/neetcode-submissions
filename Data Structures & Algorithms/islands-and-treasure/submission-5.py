class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m, n = len(grid), len(grid[0])

        queue = deque()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row,col))
        
        depth = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                
                neighbors = [(row+1,col),(row,col+1),(row-1, col),(row,col-1)]

                for nbr in neighbors:
                    r,c = nbr
                    if (0<=r<m and 0<=c<n and grid[r][c] == INF):
                        grid[r][c] = depth + 1
                        queue.append(nbr)
            depth += 1
        

