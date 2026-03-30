class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])
        parent = [i for i in range(rows * cols + 1)]
        size = [1] * (rows * cols + 1)

        dummy = rows * cols   # extra node

        def find(x):
            root = x
            while parent[root] != root:
                root = parent[root]

            while parent[x] != root:
                nxt = parent[x]
                parent[x] = root
                x = nxt
            return root

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] >= size[rb]:
                parent[rb] = ra
                size[ra] += size[rb]
            else:
                parent[ra] = rb
                size[rb] += size[ra]

        def node(r, c):
            return r * cols + c

        # Step 1: Union border O's with dummy
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':

                    # border cell
                    if r in (0, rows-1) or c in (0, cols-1):
                        union(node(r, c), dummy)

                    # union with right & down neighbours
                    for dr, dc in [(0, 1), (1, 0)]:
                        nr, nc = r + dr, c + dc
                        if nr < rows and nc < cols and board[nr][nc] == 'O':
                            union(node(r, c), node(nr, nc))

        # Step 2: Flip surrounded O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and find(node(r, c)) != find(dummy):
                    board[r][c] = 'X'