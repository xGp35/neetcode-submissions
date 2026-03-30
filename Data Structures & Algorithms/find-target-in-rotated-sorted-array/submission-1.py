class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[high]:
                # Right segment is the sorted segment
                if nums[mid]< target <= nums[high] :
                    low = mid + 1
                else:
                    high = mid
            else:
                # Mid element is greater than the right, implies left is sorted
                if nums[low] <= target < nums[mid] :
                    high = mid
                else:
                    low = mid + 1 
        
        return -1