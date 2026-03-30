class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def has_path(src, dst, graph):
            stack = [src]
            visited = {src}

            while stack:
                curr = stack.pop()
                if curr == dst: return True
                
                for nbr in graph.get(curr, []):
                    if nbr not in visited:
                        visited.add(nbr)
                        stack.append(nbr)
            return False
        
        for u,v in edges:
            if has_path(u,v,graph):
                return [u,v]
            
            graph[u].append(v)
            graph[v].append(u)
        
        return []

