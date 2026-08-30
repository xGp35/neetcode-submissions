class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        def find(node):
            if arr[node] != node:
                arr[node] = find(arr[node])
            return arr[node]
        
        def union(nodeA, nodeB):
            rootA = find(nodeA)
            rootB = find(nodeB)

            if rootA == rootB: 
                return True # cycle exists => not valid tree

            if size[rootA] > size[rootB]:
                arr[rootB] = arr[rootA]
                size[rootA] += size[rootB]
            else:
                arr[rootA] = arr[rootB]
                size[rootB] += size[rootA]
        
        arr = [i for i in range(n)]
        size = [1]*n

        for u, v in edges:
            if union(u,v):
                return False
       
        return True



                    
