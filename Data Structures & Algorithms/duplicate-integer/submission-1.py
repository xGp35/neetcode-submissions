class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupset = set()
        for num in nums:
            if num in dupset:
                return True
            dupset.add(num)
        return False
            