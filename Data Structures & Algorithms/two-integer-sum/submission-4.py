class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            if num in num_dict:
                return [num_dict[num], i]
            num_dict[target-num] = i
        
        return [0,0]
            
        
        