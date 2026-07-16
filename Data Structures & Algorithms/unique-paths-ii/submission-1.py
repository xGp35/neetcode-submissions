class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        cache = [[0]*(cols+1) for i in range(rows+1)]

        if obstacleGrid[0][0] == 1 or obstacleGrid[rows-1][cols-1] == 1:
            return 0
        
        cache[rows-1][cols-1] = 1

        for r in range(rows-1, -1 ,-1):
            for c in range(cols-1, -1,-1):
                if obstacleGrid[r][c] == 1:
                    cache[r][c] = 0
                else:    
                    cache[r][c] += (cache[r+1][c] + cache[r][c+1])
                    # We do += instead of =  
                    # to avoid overwriting cache[rows-1][cols-1]
                    # which was initialized to 1

        return cache[0][0]
