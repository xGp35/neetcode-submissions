# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortR(pairs, 0, len(pairs)-1)

    def quickSortR(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        pivot = arr[e]
        left = s

        # Partition Step
        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
        
        arr[e] = arr[left]
        arr[left] = pivot

        self.quickSortR(arr, s, left-1)
        self.quickSortR(arr, left+1, e)

        return arr
             
