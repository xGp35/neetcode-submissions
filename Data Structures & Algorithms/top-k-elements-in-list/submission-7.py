class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = Counter(nums)

        return [k for k, _ in freq_count.most_common(k)]