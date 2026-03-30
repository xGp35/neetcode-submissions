class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # so any cycle detected => not valid tree
        # Cycle detection in undirected Graph = > BFS + visited
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = {0}
        queue = deque([(0,-1)])

        while queue:
            curr, parent = queue.popleft()
            for nbr in graph[curr]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append((nbr, curr))
                elif nbr != parent:
                    return False
        
        return True if len(visited) == n else False
                

