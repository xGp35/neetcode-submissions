class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycle => tree is valid
        
        graph = {c: [] for c in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = {0}
        queue = deque([(0, -1)])

        while queue:
            curr, parent = queue.popleft()

            for nbr in graph[curr]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append((nbr,curr))
                elif nbr != parent:
                    return False

        return len(visited) == n
        
                    
