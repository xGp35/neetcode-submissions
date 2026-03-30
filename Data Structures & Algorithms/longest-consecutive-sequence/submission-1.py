class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        sorted_nums = sorted(list(set(nums)))
        diff_array = [0]*(len(nums)-1)
        for i in range(len(sorted_nums)-1):
            diff_array[i] = sorted_nums[i+1] - sorted_nums[i]
        
        #Find longest sequence of 1's in diff_array
        curr_longest = 0
        max_longest = 0
        for elem in diff_array:
            if elem == 1:
                curr_longest+=1
                max_longest = max(max_longest,curr_longest)
            else:
                curr_longest = 0
        return max_longest+1   
