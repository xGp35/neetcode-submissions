class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req_map = {}
        for i, num in enumerate(nums):
            if num in req_map:
                return [req_map[num], i]
            if target-num not in req_map:
                req_map[target-num] = i
        
        return []