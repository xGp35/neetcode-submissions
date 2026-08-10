class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # By problem guranteee, there will always be a cycle, so we don't need to check if cycle didn't exist. like while if fast is None or fast.next is None check isn't required.

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
