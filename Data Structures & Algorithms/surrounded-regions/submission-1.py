class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        m, n = len(board), len(board[0])
        arr = [i for i in range(m * n + 1)]
        size = [1] * (m * n + 1)

        dummy = m * n   # extra node

        def find(node):
            root = node
            while arr[root] != root:
                root = arr[root]

            while arr[node] != root:
                next_node = arr[node]
                arr[node] = root
                node = next_node
            return root

        def union(a, b):
            keyA, keyB = find(a), find(b)
            if keyA == keyB:
                return
            if size[keyA] >= size[keyB]:
                arr[keyB] = keyA
                size[keyA] += size[keyB]
            else:
                arr[keyA] = keyB
                size[keyB] += size[keyA]

        def node(r, c):
            return r * n + c

        dirs = [(0, 1), (1, 0)]
        # Step 1: Union border O's with dummy
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':

                    # Check if it is a border cell
                    if row in (0, m-1) or col in (0, n-1):
                        union(node(row, col), dummy)

                    # union with right & down neighbours
                    
                    for dr, dc in dirs:
                        r = row + dr
                        c = col + dc
                        if (r < m and 
                            c < n and 
                            board[r][c] == 'O'
                        ):
                            union(node(row, col), node(r, c))

        # Step 2: Flip surrounded O's
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O' and find(node(row, col)) != find(dummy):
                    board[row][col] = 'X'