class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Do a Last valid binary search on the store[key]
        nums = self.store[key]

        low, high = 0, len(nums) - 1
        ans = ""
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid][0] <= timestamp:
                ans = nums[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        
        return ans



