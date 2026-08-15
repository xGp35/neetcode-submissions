class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])

        START_COLOR = image[sr][sc]
        if START_COLOR == color: return image
        image[sr][sc] = color
        
        def explore(node):
            row, col = node
            #if image[row][col] != START_COLOR: return

            neighbors = [(row+1, col),(row, col +1),(row-1, col),(row, col -1)]
            for nbr in neighbors:
                r, c = nbr
                if (
                    0 <= r < m and
                    0 <= c < n and
                    image[r][c] == START_COLOR
                ):
                    image[r][c] = color
                    explore(nbr)
        
        explore((sr,sc))
        return image

            