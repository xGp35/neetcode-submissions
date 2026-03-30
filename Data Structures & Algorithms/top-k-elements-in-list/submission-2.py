class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ding_dong = Counter(nums)

        return [num for num, _ in ding_dong.most_common(k)]