class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def explore(node):
            stack = [node]
            visited.add(node)
            cur_size = 0

            while stack:
                row, col= stack.pop()
                
                cur_size += 1

                for dr, dc in dirs:
                    r,c = row + dr, col + dc
                    if(
                        0 <= r < m and
                        0 <= c < n and
                        grid[r][c] == 1 and
                        (r,c) not in visited
                    ):
                        visited.add((r,c))
                        stack.append((r,c))
            
            return cur_size

        for row in range(m):
            for col in range(n):
                if (row, col) not in visited and grid[row][col] == 1:
                    max_area = max(max_area, explore((row,col)))

        return max_area
