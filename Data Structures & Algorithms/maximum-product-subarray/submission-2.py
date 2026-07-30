class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxP = nums[0]
        curMax, curMin = 1, 1

        for num in nums:
            temp = curMax*num
            curMax = max(num, curMax*num, curMin*num)
            curMin = min(num, temp, curMin*num)

            maxP = max(maxP, curMax)
        
        return maxP


