class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        indegree = {i:0 for i in range(numCourses)}

        for course, prereq in prerequisites:
            indegree[course] += 1
            graph[prereq].append(course)
        
        queue = deque([node for node in graph if indegree[node] == 0])

        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for nbr in graph[curr]:
                indegree[nbr] -= 1
                if indegree[nbr] ==0:
                    queue.append(nbr)

        return result if len(result) == numCourses else []