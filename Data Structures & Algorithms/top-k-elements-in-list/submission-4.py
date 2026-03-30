class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        arr = [[] for i in range(n+1)]
        num_count = {}

        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)

        for key, val in num_count.items():
            arr[val].append(key)

        result = []
        stop = False
        for i in range(n, 0, -1):
            for num in arr[i]:
                result.append(num)
                if len(result) == k:
                    return result

        
            


