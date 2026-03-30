class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ding_dong = {}

        for elem in nums:
            if elem in ding_dong:
                ding_dong[elem] += 1
            else:
                ding_dong[elem] = 1
        
        cobra_kai = [(kee,val) for kee,val in ding_dong.items()]
        
        cobra_kai.sort(key = lambda x: x[1], reverse = True)

        judomaster = [j[0] for j in cobra_kai[:k]]
        return judomaster