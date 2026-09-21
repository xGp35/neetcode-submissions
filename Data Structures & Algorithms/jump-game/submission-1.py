class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_index = len(nums)-1
        for curr_index in range(len(nums)-2, -1, -1):
            if curr_index + nums[curr_index] >= goal_index:
                goal_index = curr_index

        return True if goal_index == 0 else False