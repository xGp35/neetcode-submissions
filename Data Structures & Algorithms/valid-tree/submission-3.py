class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        arr = [i for i in range(n)]
        size = [1]*n
        def find(node):
            if arr[node] != node:
                arr[node] = find(arr[node])
            return arr[node]
        def union(nodeA, nodeB):
            rootA = find(nodeA)
            rootB = find(nodeB)

            if rootA == rootB:
                return True
            
            if size[rootA] >= size[rootB]:
                arr[rootB] = rootA
                size[rootA] += size[rootB]
            else:
                arr[rootA] = rootB
                size[rootB] += size[rootA]
        
        for a, b in edges:
            if union(a,b):
                return False
        
        if max(size) != n:
            return False
        return True