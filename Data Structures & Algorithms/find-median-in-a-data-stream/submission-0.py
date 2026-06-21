class MedianFinder:

    def __init__(self):
        self.leftHeap = [] #maxHeap
        self.rightHeap = [] # minHeap

        heapq.heapify(self.leftHeap)
        heapq.heapify(self.rightHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -num)
        if self.leftHeap and self.rightHeap and -self.leftHeap[0] > self.rightHeap[0]:
            heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))
        if len(self.leftHeap) > len(self.rightHeap) + 1:
            heapq.heappush(self.rightHeap, -heapq.heappop(self.leftHeap))
        if len(self.rightHeap) > len(self.leftHeap):
            heapq.heappush(self.leftHeap, -heapq.heappop(self.rightHeap))

    def findMedian(self) -> float:
        if len(self.leftHeap)==0: return 0.0
        if len(self.rightHeap)==0: return -self.leftHeap[0]
        if len(self.leftHeap) == len(self.rightHeap):
            return (-self.leftHeap[0] + self.rightHeap[0])/2
        else:
            return -self.leftHeap[0]

        