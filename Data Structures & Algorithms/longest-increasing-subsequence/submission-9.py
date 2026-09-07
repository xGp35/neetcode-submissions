class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        T = [1]*len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if T[j] + 1 > T[i]:
                        T[i] = 1 + T[j]
        return max(T)