class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        arr = list(range(n))
        size = [1]*n
        def find(node):
            if node != arr[node]:
                arr[node] = find(arr[node])
            return arr[node] 
        def union(nodeA, nodeB):
            keyA = find(nodeA)
            keyB = find(nodeB)

            if keyA == keyB:
                return True
            
            if size[keyA] >= size[keyB]:
                arr[keyB] = keyA
                size[keyA] += size[keyB]
            else:
                arr[keyA] = keyB
                size[keyB] += size[keyA]
        
        for u,v in edges:
            if union(u, v):
                return [u,v]
        
        return []