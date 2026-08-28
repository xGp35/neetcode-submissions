class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3: return len(nums)
        i = 2

        for j in range(2, len(nums)):
            if nums[j] != nums[i-2]:  # Important to keep i-2 (two value before write pointer.)
                nums[i] = nums[j]
                i += 1
        
        return i
