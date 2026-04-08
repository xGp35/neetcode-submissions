class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We'll use bucket sort to find this today

        count = {}
        freq = [[] for _ in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        max_freq = max(count.values())
        for i in range(max_freq, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
                 