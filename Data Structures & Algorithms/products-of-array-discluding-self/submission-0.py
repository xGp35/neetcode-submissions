class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_zeroes = nums.count(0)

        if num_zeroes > 1:
            return [0]*n
        elif num_zeroes == 1:
            zero_index = nums.index(0) 
            product = 1
            for i in range(n):
                if i ==zero_index:
                    continue
                product *= nums[i]
            prod_array = [0]*n
            prod_array[zero_index] = product
            return prod_array
        product = 1
        for elem in nums:
            product = product*elem
        product_array = [1]*n
        for i, elem in enumerate(nums):
            product_array[i] = product//elem
        return product_array