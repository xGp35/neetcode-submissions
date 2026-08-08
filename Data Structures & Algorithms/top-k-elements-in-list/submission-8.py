class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1
        
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        result= []
        max_freq = max(count.values())
        for i in range(max_freq, -1, -1):
            for elem in freq[i]:
                result.append(elem)
                if len(result) == k: return result