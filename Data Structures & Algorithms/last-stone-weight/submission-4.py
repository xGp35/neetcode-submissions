class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [- weight for weight in stones]

        #Assume you have native maxHeap implementation
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            diff = -(first - second)
            if diff > 0:
                heapq.heappush(maxHeap, -diff)
        
        return 0 if len(maxHeap) == 0 else -maxHeap[0]
            

