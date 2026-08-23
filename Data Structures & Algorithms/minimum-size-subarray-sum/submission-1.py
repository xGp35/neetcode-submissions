class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curSum = 0
        shortest = float('inf')
        
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                shortest = min(shortest, r-l+1)
                curSum -= nums[l]
                l+=1

        return shortest if shortest < float('inf') else 0