class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        count = 0
        visited = set()
        for node in graph:
            if node not in visited:
                self.dfs_explore(node, graph, visited)
                count += 1
        
        diff = n - len(graph)
        return count + diff
    
    def dfs_explore(self, node, graph, visited):
        stack = [node]

        while stack:
            curr = stack.pop()
            for nbr in graph[curr]:
                if nbr not in visited:
                    visited.add(nbr)
                    stack.append(nbr)
