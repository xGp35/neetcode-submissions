class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycle => tree is valid
        
        graph = {c: [] for c in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        
        def bfs_cycle_detect(node):
            queue = deque([(node, None)])
            visited.add(node)

            while queue:
                curr, parent = queue.popleft()

                for nbr in graph[curr]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append((nbr,curr))
                    elif nbr != parent:
                        return True
            
            return False

        if bfs_cycle_detect(0):
            return False
        return len(visited) == n
        
                    
