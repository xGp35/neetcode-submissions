class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = float('-inf')
        maxSum = float('-inf')

        for num in nums:
            curSum = max(num+curSum, num)
            maxSum = max(maxSum, curSum)
        
        return maxSum
