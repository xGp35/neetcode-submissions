class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        cooldown = deque() # [next_available_time, -count]
        schedule = []

        while maxHeap or cooldown:
            time += 1
            while cooldown and cooldown[0][0] <= time:
                available_time, count = cooldown.popleft()
                heapq.heappush(maxHeap, count)
            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1
                if count < 0:
                    cooldown.append((time+n+1, count))
        return time
            
