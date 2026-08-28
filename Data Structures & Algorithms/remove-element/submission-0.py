class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 # Write pointer
        j = 0 # Read Pointer

        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
            j+=1
        return i