class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist_list = []
        for x, y in points:
            dist_i = x ** 2 + y ** 2
            heapq.heappush(dist_list, (-dist_i, [x,y]))
            if len(dist_list) > k:
                heapq.heappop(dist_list)
        
        result = [elem[1] for elem in dist_list]
        return result
        