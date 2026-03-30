class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        arr = list(range(n))
        size = [1]*n
        def find(node):
            root = node

            while arr[root] != root:
                root = arr[root]

            while arr[node] != root:
                next_node = arr[node]
                arr[node] = root
                node = next_node
            return root

        def union(nodeA, nodeB):
            keyA = find(nodeA)
            keyB = find(nodeB)

            if keyA == keyB:
                return

            if size[keyA] >= size[keyB]:
                arr[keyB] = keyA
                size[keyA] += size[keyB]
            else:
                arr[keyA] = keyB
                size[keyB] += size[keyA]
        count = 0
        for u,v in edges:
            union(u,v)
        
        for i in range(n):
            if i == arr[i]:
                count += 1
        return count
