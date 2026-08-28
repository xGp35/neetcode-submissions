class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        def dist(x,y):
            return math.sqrt((x)**2 + (y)**2)
        
        for i, point in enumerate(points):
            heapq.heappush(maxHeap, (-dist(point[0],point[1]), i))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [points[i] for _, i in maxHeap]

            