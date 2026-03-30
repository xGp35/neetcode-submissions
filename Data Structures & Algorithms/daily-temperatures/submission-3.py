class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0]*n

        for i, temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                result[index] = i-index
            stack.append(i)
        return result
