class TimeMap:

    def __init__(self):
        self.time_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key] = [(value,timestamp)]
        else:
            self.time_dict[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value_list =  self.time_dict.get(key, "")
        #Find the smallest timestamp that is <= given timestamp using binary search.
        # I know array is sorted.
        # So, I need to do binary search on 2nd element of tuple.
        low = 0
        high = len(value_list) - 1

        while low <= high:
            mid = low + (high-low)//2
            if value_list[mid][1] == timestamp:
                return value_list[mid][0]
            elif value_list[mid][1] < timestamp:
                low = mid + 1
            else:
                high = mid - 1
        return value_list[high][0] if high >= 0 else ""
