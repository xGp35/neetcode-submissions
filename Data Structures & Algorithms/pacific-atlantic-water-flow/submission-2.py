class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pacific_set = set()
        atlantic_set = set()

        
            
        def explore(row,col, visited):
            if (row,col) in visited: return
            visited.add((row,col))
            neighbors = [(row+1,col),(row,col+1),(row-1,col),(row,col-1)]

            for nbr in neighbors:
                r, c = nbr
                if(0<=r<m and 0<=c<n and heights[r][c] >= heights[row][col] and
                    nbr not in visited
                ):
                    explore(r,c, visited)
        
        for row in range(m):
            explore(row,0, pacific_set)
            explore(row, n-1, atlantic_set)

        for col in range(n):
            explore(0,col, pacific_set)
            explore(m-1, col, atlantic_set)

        
        result = []
        for (row,col) in pacific_set & atlantic_set:
            result.append([row,col])

        return result