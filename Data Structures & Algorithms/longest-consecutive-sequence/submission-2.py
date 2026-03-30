class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution using sets -> O(n)
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                j=0
                while (num+j) in numSet:
                    j += 1
                longest = max(j,longest)
        return longest   

        
        # # Solution using sorting -> O(nlogn)
        # if len(nums) <= 1:
        #     return len(nums)
        # sorted_nums = sorted(list(set(nums)))
        # diff_array = [0]*(len(nums)-1)
        # for i in range(len(sorted_nums)-1):
        #     diff_array[i] = sorted_nums[i+1] - sorted_nums[i]
        
        # #Find longest sequence of 1's in diff_array
        # curr_longest = 0
        # max_longest = 0
        # for elem in diff_array:
        #     if elem == 1:
        #         curr_longest+=1
        #         max_longest = max(max_longest,curr_longest)
        #     else:
        #         curr_longest = 0
        # return max_longest+1   
