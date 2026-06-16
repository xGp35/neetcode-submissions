class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque([])
        res = []
        left = right = 0
        for right in range(len(nums)):
            curr = nums[right]
            while queue and curr > nums[queue[-1]]:
                queue.pop()
            queue.append(right)
            while queue[0] <= right-k:
                queue.popleft()
            if right >= k-1:
                res.append(nums[queue[0]])
                left += 1 
                
        return res