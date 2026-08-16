class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i:0 for i in range(numCourses)}
        graph = defaultdict(list)
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = deque([key for key in indegree if indegree[key] == 0])

        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)
            for nbr in graph[curr]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
        
        return len(result) == numCourses