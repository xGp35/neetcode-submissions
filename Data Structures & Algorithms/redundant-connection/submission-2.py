class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        arr = [i for i in range(n)]
        size = [1]*n

        def find(node):
            if arr[node] != node:
                arr[node] = find(arr[node])
            return arr[node]

        def union(a, b):
            keyA = find(a)
            keyB = find(b)

            if keyA == keyB:
                return True
            
            if size[keyA] >= size[keyB]:
                arr[keyB] = keyA
                size[keyA] += size[keyB]
            else:
                arr[keyA] = keyB
                size[keyB] += size[keyA]

        for a, b in edges:
            if union(a, b):
                return[a,b]
        
        

        
