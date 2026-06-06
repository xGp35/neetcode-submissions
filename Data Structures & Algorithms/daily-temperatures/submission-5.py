class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0]*n
        
        for i, temp in enumerate(temperatures):
    
            while stack and temp > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append([temp,i])
        return result
            