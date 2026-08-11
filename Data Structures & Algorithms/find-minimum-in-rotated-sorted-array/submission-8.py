class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low, high = 0, len(nums) - 1
        # First Valid or Last valid can't be applied.
        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1
        
        return nums[low]