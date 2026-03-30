class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        stack = deque()
        result = [0]*n
        
        for i, temp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            stack.append(i)
        
        return result
