class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist_list = []
        for point in points:
            xi, yi = point[0], point[1]
            dist_i = math.sqrt(xi**2 + yi**2)
            heapq.heappush(dist_list, (-dist_i, point))
            if len(dist_list) > k:
                heapq.heappop(dist_list)
        
        result = [elem[1] for elem in dist_list]
        return result
        