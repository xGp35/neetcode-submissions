class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(node, visited, prevHeight):
            row,col = node
            if (node in visited or
                row < 0 or col < 0 or row == m or col == n or
                heights[row][col] < prevHeight
            ):
                return

            visited.add(node)
            neighbors = [(row+1,col),(row, col+1),(row-1, col),(row,col-1)]
            for nbr in neighbors:
                r,c = nbr
                dfs(nbr, visited, heights[row][col])


        for r in range(m):
            dfs((r,0), pac, heights[r][0])
            dfs((r,n-1), atl, heights[r][n-1])
        
        for c in range(n):
            dfs((0,c), pac, heights[0][c])
            dfs((m-1,c), atl, heights[m-1][c])

        result = []
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])

        return result