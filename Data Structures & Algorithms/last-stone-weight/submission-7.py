class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            heaviest = -heapq.heappop(maxHeap)
            heaviest2 = -heapq.heappop(maxHeap)

            remaining = heaviest - heaviest2
            if remaining != 0:
                heapq.heappush(maxHeap, -remaining)
        
        return -maxHeap[0] if maxHeap else 0
        
                