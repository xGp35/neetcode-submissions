class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # We need a minHeap of costs, so we can pick from it when out capital goes over the cost requried for a particular project
        # We need a maxHeap of profits so we can add all projects which can be completed with the current capital limit and then pick the max one from this maxHeap
        # We do this k times and when we pick a prokect we add its profit to our capital.
        costHeap = [(c,p) for c, p in zip(capital, profits)] # minHeap
        profitHeap = [] # maxHeap
        heapq.heapify(costHeap)

        for i in range(k):
            
            # costHeap[0][0] is the capital part of the top of minHeap
            while costHeap and costHeap[0][0] <= w:
                c, p = heapq.heappop(costHeap)
                # We got the projects we can build with current capital, now we push the profits of these projects into the maxHeap.
                heapq.heappush(profitHeap, -p)
            
            # One check before possing from profitHeap, that whether its empty, this can happen if none of the projects are viable from capital POV and we have no projects. We return directly.
            if len(profitHeap) == 0:
                return w

            w += -heapq.heappop(profitHeap)
        
        return w