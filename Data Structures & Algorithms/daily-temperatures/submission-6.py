class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        nums = temperatures

        result = [0]*len(nums)

        for i, x in enumerate(nums):
            while stack and x > nums[stack[-1]]:
                j = stack.pop()
                # x is the next greater element of nums[j]
                # might sound a bit confusing but - j is the "ith day" of problem statement
                # do something with it
                result[j] = i - j
            stack.append(i)
        
        return result