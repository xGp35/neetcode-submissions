class Solution:
    def findMin(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1
        min_value = 10000

        

        while low <= high:
            if nums[low] <= nums[high]:
                return nums[low]

            mid = low + (high-low)//2

            if nums[mid] <= nums[high]:
                if high == mid or high == mid+1 or nums[mid]<nums[mid-1]:
                    return nums[mid]
                else:
                    high = mid-1
            elif nums[mid] > nums[high]:
                low = mid + 1
        
        return -1