class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        numset = set(nums)
        longest = 1
        for num in numset:
            if num-1 not in numset:
                j = 1
                while num+j in numset:
                    j+=1
                    longest = max(longest, j)
        
        return longest
                
