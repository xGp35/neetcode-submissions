class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones2 = [-val for val in stones]
        heapq.heapify(stones2)
        while len(stones2) > 1:
            first = heapq.heappop(stones2)
            second = heapq.heappop(stones2)
            if second > first:
                heapq.heappush(stones2, first - second)
        stones2.append(0)
        return -stones2[0]