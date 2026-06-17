class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        result = []

        pacific = set()
        atlantic = set()

        def dfs(row,col, visited, m, n):
            if (row,col) in visited: return
            visited.add((row,col))
            neighbors = [(row+1, col),(row, col+1), (row-1, col), (row, col-1)]
            for nbr in neighbors:
                nr, nc = nbr
                if ( 0 <= nr < m and
                     0 <= nc < n and
                    heights[nr][nc] >= heights[row][col]
                ):
                    dfs(nr,nc, visited, m, n)

        for r in range(m):
            dfs(r, 0, pacific, m, n)
            dfs(r, n-1, atlantic, m, n)
        
        for c in range(n):
            dfs(0 ,c , pacific, m, n)
            dfs(m-1 ,c , atlantic, m, n)

        for row in range(m):
            for col in range(n):
                if (row,col) in pacific and (row,col) in atlantic:
                    result.append([row,col]) 
        return result

        
        
        