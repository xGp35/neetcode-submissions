class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m,n = len(grid), len(grid[0])
        fresh = 0
        visited = set()

        queue = deque()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
                    visited.add((row, col))

        total_fruits = fresh + len(queue)
        time = 0
        done = 0
        
        if fresh == 0:
            return 0

        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        while queue:
            for _ in range(len(queue)):
                row,col = queue.popleft()
                
                for dr, dc in dirs:
                    r = row + dr
                    c = col + dc
                    if (0 <= r < m and 0 <= c < n and
                        grid[r][c] == 1 and (r,c) not in visited
                    ): 
                        visited.add((r,c))
                        queue.append((r,c))
                        fresh -= 1
            time += 1
            if fresh == 0:
                return time               
        return time if fresh ==0 else -1