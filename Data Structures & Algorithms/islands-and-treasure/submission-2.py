class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        MAX_INT = 2147483647
        m, n = len(grid), len(grid[0])

        queue = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queue.append((row,col))
            
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        while queue:
            row,col = queue.popleft()

            for dr, dc in dirs:
                r = row + dr
                c = col + dc
                if(
                    0<=r<m and 0<=c<n and 
                    grid[r][c] == MAX_INT
                ):
                    grid[r][c] = grid[row][col] + 1  
                    queue.append((r,c))
        

        
        



