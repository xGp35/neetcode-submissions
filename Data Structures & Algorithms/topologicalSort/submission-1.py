class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        topsort = []
        visited = set()
        visiting = set()

        for u, v in edges:
            graph[u].append(v)
        
        # White-greay-black algorithm
        def dfs(node):
            if node in visiting: return False # cycle detected
            if node in visited: return True   # No cycle found

            visiting.add(node)

            for nbr in graph[node]:
                if not dfs(nbr):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            topsort.append(node)

            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        
        topsort.reverse()
        return topsort
            

        
        # indegree = {c:0 for c in range(n)}
        # graph = {c:[] for c in range(n)}

        # for u, v in edges:
        #     graph[u].append(v)
        #     indegree[v] += 1
         
        # queue = deque([node for node in indegree if indegree[node]==0])
        # result = []
        # while queue:
        #     curr = queue.popleft()
        #     result.append(curr)
        #     for nbr in graph[curr]:
        #         indegree[nbr] -= 1
        #         if indegree[nbr] == 0:
        #             queue.append(nbr)
        # return result if len(result) == n else []
