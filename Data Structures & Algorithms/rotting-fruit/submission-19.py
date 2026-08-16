class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        queue = deque()
        fresh = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    fresh += 1
        
        time = 0
        if fresh == 0: return 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                neighbors = [(row+1,col),(row,col+1),(row-1,col),(row,col-1)]

                for nbr in neighbors:
                    r, c = nbr
                    if(0<=r<m and 0<=c<n and grid[r][c] == 1):
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append((r,c))

            time += 1
            if fresh == 0:
                return time
            
        return -1