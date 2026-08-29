class MedianFinder:

    def __init__(self):
        self.leftHeap = [] # maxHeap
        self.rightHeap = [] # minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftHeap, -num)
        if len(self.leftHeap) > len(self.rightHeap) + 1:
            val = heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, -val)
        if self.rightHeap and -self.leftHeap[0] > self.rightHeap[0]:
            leftMaxVal = heapq.heappop(self.leftHeap)
            rightMaxVal = heapq.heappop(self.rightHeap)
            heapq.heappush(self.rightHeap, -leftMaxVal)
            heapq.heappush(self.leftHeap, -rightMaxVal)

    def findMedian(self) -> float:
        if len(self.leftHeap) == len(self.rightHeap):
            return (-self.leftHeap[0] + self.rightHeap[0])/2
        else:
            return -self.leftHeap[0]         
        