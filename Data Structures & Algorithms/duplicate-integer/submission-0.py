class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_dict = {}
        for elem in nums:
            if elem in dup_dict.keys(): 
                return True
            else:
                dup_dict[elem] = 1
        return False