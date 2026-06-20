class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i in range(len(points)):

            dist = self.find_distance(points[i][0], points[i][1])
            heapq.heappush(maxHeap, (-dist, i))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        result =[points[i] for _, i in maxHeap]
        return result

    def find_distance(self, x, y):
        return math.sqrt(x**2 + y**2)