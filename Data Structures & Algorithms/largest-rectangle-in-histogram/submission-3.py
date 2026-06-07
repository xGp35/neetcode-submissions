class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #pair of (start_index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                max_area = max(max_area, height*width)
                start = index

            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights)-i))
        return max_area