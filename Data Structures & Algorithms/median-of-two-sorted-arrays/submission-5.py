class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2: 
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        # Binary search is on how many elements to picke from array1
        low, high = 0, n1

        while low <= high:
            mid1 = low + (high-low)//2 # No. of elements to take from arr1
            mid2 = (n1+n2+1)//2 - mid1 # No. of elements to take from arr2

            l1 = nums1[mid1-1] if mid1 > 0 else float('-inf')
            l2 = nums2[mid2-1] if mid2 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < n1 else float('inf')
            r2 = nums2[mid2] if mid2 < n2 else float('inf')

            if (l1 <= r2 and l2 <= r1):
                break

            elif (l1 > r2):
                high = mid1-1
            elif (l2 > r1):
                low = mid1 + 1
            
        if (n1+n2) % 2 != 0: median = max(l1,l2)
        else:
            median = (max(l1,l2) + min(r1,r2))/2
        
        return median