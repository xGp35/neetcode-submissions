# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)
        s = 0
        e = len(pairs) - 1
        self.divideRecurse(pairs, s, e)
        return pairs
        
    def divideRecurse(self, arr, s, e):
        if e - s +1 <= 1:
            return arr
        
        m = (s+e) // 2
        self.divideRecurse(arr, s, m) # mth index is incl, s -> 1st element and e points to last element
        self.divideRecurse(arr, m+1, e)
        self.merge(arr, s, m, e)
        return arr

    def merge(self, arr, s, m, e):
        L = arr[s:m+1]
        R = arr[m+1:e+1]

        i, j = 0, 0
        k = s

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        


