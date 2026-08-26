class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studs = Counter(students)

        for s in sandwiches:
            if studs[s] == 0:
                break
            studs[s] -= 1
        
        return sum(studs.values())


