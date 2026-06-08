class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # This needs to do a binary search on the second element of the list of tuples
        # And return the previous smallest element.
        def binary_search(tuple_list, target):
            if len(tuple_list) == 0: return -1
            low, high = 0, len(tuple_list) - 1
            ans = -1
            while low <= high:
                mid = low + (high-low)//2
                if tuple_list[mid][1] == target:
                    return mid
                elif tuple_list[mid][1] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                    ans = mid
            return ans

        result = binary_search(self.time_dict[key], timestamp)
        if result == -1:
            return ""
        result = int(result)
        return self.time_dict[key][result][0]


        
