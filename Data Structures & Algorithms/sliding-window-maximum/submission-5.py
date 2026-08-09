class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        for i in range(k):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        
        result = [nums[dq[0]]]

        for r in range(k, len(nums)):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            if dq[0] <= r-k:
                dq.popleft()
            result.append(nums[dq[0]])
        
        return result