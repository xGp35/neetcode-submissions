class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair of (start_index, height)
        maxA = 0
        # monotonic increasing stack?? - Yes

        # We add extra 0 at end to make sure we have a
        # smallest elem at end so we can pop. Else there would be 
        # no way to stop a increasing stack
        for i, height in enumerate(heights + [0]):
            start = i
            while stack and height < stack[-1][1]:
                j, popped_ht = stack.pop()
                width = i - j
                area = width * popped_ht
                maxA = max(maxA, area)
                start = j
            # append the height current with index of what I popped.
            stack.append((start, height))
        return maxA
        
        # for i, x in enumerate(nums):
        #     while stack and x < nums[stack[-1]]:
        #         j = stack.pop()
        #         # x is the  next smallest of nums[j]
        #         # whats the area of the largest rectangle that could have been formed starting from j?
        #         # width is i -j
        #         # height is height[j]
        #         # if that area is greater than max Area then update maxArea
        #         # do something with j
        #     stack.append(x)