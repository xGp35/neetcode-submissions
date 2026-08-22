class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        suffix = -1
        for i in range(n-1,-1,-1):
            temp = arr[i]
            arr[i] = suffix
            suffix = max(temp,suffix)
        
        return arr