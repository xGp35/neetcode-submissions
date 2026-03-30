class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        visited = set()
        count = 0
        m,n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row,col) not in visited:
                    self.explore((row,col),visited, grid, m, n)
                    count += 1

        return count

    def explore(self, node, visited, grid, m,n):
        stack = [node]
        visited.add(node)

        while stack:
            row, col = stack.pop()
            neighbors = [(row+1, col), (row, col+1), (row-1, col),(row, col-1)]

            for nbr in neighbors:
                r,c = nbr
                if (
                    0 <= r < m and
                    0 <= c < n and
                    grid[r][c] == "1" and
                    nbr not in visited
                ):
                    visited.add(nbr)
                    stack.append(nbr)