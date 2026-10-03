class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        numset = set(nums)
        longest = 1
        for num in numset: # Loop1: iterate over elements of list
            if num-1 not in numset: # Cond1: if lower number was not present this is a starting point for exploration. (Set j = 1, and explore)
                j = 1
                while num+j in numset: # Loop2: iterate of +1 of current_num (in numset. This is O(1) lookup
                    j+=1
                    longest = max(longest, j) # Update result
        
        return longest
                
