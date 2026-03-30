class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        def has_cycle_kahn(graph):
            indegree = defaultdict(int)

            # Step 1: compute indegree
            for u in graph:
                for v in graph[u]:
                    indegree[v] += 1

            # include nodes with 0 indegree that may not be in indegree map
            for u in graph:
                if u not in indegree:
                    indegree[u] = 0

            # Step 2: queue for 0 indegree
            queue = deque([u for u in indegree if indegree[u] == 0])

            processed = 0

            # Step 3: BFS
            while queue:
                node = queue.popleft()
                processed += 1

                for nbr in graph.get(node, []):
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        queue.append(nbr)

            # Step 4: cycle check
            return processed != len(indegree)

        return not has_cycle_kahn(graph)
