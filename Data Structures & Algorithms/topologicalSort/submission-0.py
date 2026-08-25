class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree = {c:0 for c in range(n)}
        graph = {c:[] for c in range(n)}

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
         
        queue = deque([node for node in indegree if indegree[node]==0])
        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for nbr in graph[curr]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
        return result if len(result) == n else []
