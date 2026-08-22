class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        ans = [0]*n
        suffix = -1
        for i in range(n-1,-1,-1):
            ans[i] = suffix
            suffix = max(arr[i],suffix)
        
        return ans