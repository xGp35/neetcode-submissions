class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1: return 0
        visited = set()

        def explore(node):
            if node in visited: return 0
            row, col = node
            if row == m - 1 and col == n-1: return 1
            visited.add(node)

            count = 0

            neighbors = [(row+1, col),(row, col+1),(row-1, col),(row, col-1)]

            for nbr in neighbors:
                r, c = nbr
                if (
                    0 <= r < m and
                    0 <= c < n and
                    grid[r][c] == 0 and
                    nbr not in visited
                ):
                    count += explore(nbr)
            visited.remove(node)

            return count
        
        return explore((0,0))