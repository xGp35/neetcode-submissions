class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}

        for course, prereq in prerequisites:
            indegree[course] += 1
            graph[prereq].append(course)

        queue = deque([node for node in indegree if indegree[node] == 0])
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)
            for nbr in graph[curr]:
                if indegree[nbr] > 0:
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        queue.append(nbr)
        
        return True if len(result) == numCourses else False