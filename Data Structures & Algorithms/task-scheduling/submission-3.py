class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = Counter(tasks)
        
        maxHeap = [-freq for freq in freq_map.values()]
        heapq.heapify(maxHeap)

        queue = deque() # Stores (remaining_freq, next_rt)
        timer = 0
        while maxHeap or queue:
            # First fetch all possible values that can be run currently from queue
            if queue and queue[0][1] <= timer:
                rem_freq, next_rt = queue.popleft()
                heapq.heappush(maxHeap, rem_freq)
            # This is where we run the task
            if maxHeap:
                curr_freq = heapq.heappop(maxHeap)
                curr_freq += 1 # Ideally we shuold do currFreq - 1, but python doesn't have a maxHeap so we are dealing with negative numbers
                if curr_freq < 0: # Again python
                    queue.append((curr_freq, timer + n+1))

            timer += 1
        return timer

