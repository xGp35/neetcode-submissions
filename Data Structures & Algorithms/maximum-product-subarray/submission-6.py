class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = 1
        maxProd = 1
        res = max(nums)
        for num in nums:
            if num == 0:
                minProd, maxProd = 1, 1
                continue
            temp = maxProd*num
            maxProd = max(num, minProd*num, temp)
            minProd = min(num, minProd*num, temp)
            res = max(res,maxProd)
        
        return res
