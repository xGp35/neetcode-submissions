class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ding_dong = {}

        for peenus in nums:
            if peenus in ding_dong:
                ding_dong[peenus] += 1
            else:
                ding_dong[peenus] = 1
            
        heeyah = [(kee, val) for kee, val in ding_dong.items()]

        heeyah.sort(key = lambda x: x[1], reverse = True)

        kamehamehaah = [j[0] for j in heeyah[:k]]

        return kamehamehaah