class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)

        def has_cycle(graph):
            visited = set()
            visiting = set()

            all_nodes = list(graph)
            for node in all_nodes:
                if node not in visited:
                    if cycleDetect(node, graph, visited, visiting):
                        return True
            return False

        def cycleDetect(node, graph, visited, visiting):
            if node in visited: return False
            if node in visiting: return True

            visiting.add(node)
            for nbr in graph[node]:
                if cycleDetect(nbr, graph, visited, visiting):
                    return True
            
            visiting.remove(node)
            visited.add(node)

            return False
        return not has_cycle(graph)