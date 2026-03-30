class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}

        for i, num in enumerate(nums):
            if num in diff_map:
                return [diff_map[num], i]
            diff_map[target-num] = i
        return [0,0]