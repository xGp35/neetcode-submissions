class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        
        if n1>n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1 

        low = 0
        high = n1
        n = n1 + n2

        while low <= high:
            mid1 = low + (high-low)//2
            mid2 = (n+1)//2 - mid1

            # Find if valid symetry
            l1 = nums1[mid1-1] if mid1 > 0 else -10**6 
            l2 = nums2[mid2-1] if mid2 > 0 else -10**6
            r1 = nums1[mid1] if mid1 < n1 else 10**6
            r2 = nums2[mid2] if mid2 < n2 else 10**6

            if l1 <= r2 and l2 <= r1:
                #check if odd num of elements
                if n % 2 == 1:
                    return max(l1,l2)
                else:
                    return (max(l1, l2) + min(r1,r2))/2

            elif l1 > r2:
                high = mid1 - 1
            elif l2 > r1:
                low = mid1 + 1

        return 0.0