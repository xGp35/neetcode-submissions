class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eating_time(k):
            return sum([math.ceil(p/k) for p in piles])
        
        low = 1
        high = max(piles)
        ans = 10**10

        while (low <= high):
            mid = low + (high-low)//2

            hours = eating_time(mid)
            if hours <= h:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans

