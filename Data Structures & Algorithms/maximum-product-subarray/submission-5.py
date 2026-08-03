class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        maxP = float('-inf')

        for num in nums:
            temp = curMax*num
            curMax = max(num, curMax*num, curMin*num)
            curMin = min(num, temp, curMin*num)

            maxP = max(maxP, curMax)
        return maxP